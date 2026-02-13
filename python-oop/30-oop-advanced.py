"""
OOP Part 5: Advanced Concepts
==============================
Dataclass, Static/Class Methods, Design Patterns
"""

# ============================================
# 1. STATIC METHODS vs CLASS METHODS
# ============================================

from enum import Enum
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass, field


class Calculator:
    """Demonstrasi static method dan class method"""

    version = "1.0"

    def __init__(self, name):
        self.name = name

    # Regular instance method
    def tambah_instance(self, a, b):
        """Butuh instance (self)"""
        print(f"{self.name} menghitung...")
        return a + b

    # Static method
    @staticmethod
    def tambah(a, b):
        """
        Tidak butuh instance atau class
        Seperti function biasa, tapi ada dalam class namespace
        """
        return a + b

    @staticmethod
    def kali(a, b):
        return a * b

    # Class method
    @classmethod
    def info_version(cls):
        """
        Menerima class (cls) sebagai parameter pertama
        Bisa akses class attributes/methods
        """
        return f"Calculator version {cls.version}"

    @classmethod
    def create_scientific(cls, name):
        """Factory method - membuat instance dengan preset"""
        return cls(f"Scientific-{name}")


print("1. STATIC METHODS vs CLASS METHODS")
print("-" * 50)

# Static method - bisa dipanggil tanpa instance
print(f"Static method: 5 + 3 = {Calculator.tambah(5, 3)}")
print(f"Static method: 5 * 3 = {Calculator.kali(5, 3)}")
print()

# Class method - akses class info
print(f"Class method: {Calculator.info_version()}")
print()

# Class method sebagai factory
calc = Calculator.create_scientific("Pro")
print(f"Instance dibuat: {calc.name}")
print(f"Instance method: {calc.tambah_instance(10, 5)}")
print()


# ============================================
# 2. DATACLASS (Python 3.7+)
# ============================================


# Tanpa dataclass (verbose)

class PersonTraditional:
    def __init__(self, nama, umur, hobi=None):
        self.nama = nama
        self.umur = umur
        self.hobi = hobi if hobi else []

    def __repr__(self):
        return f"Person(nama={self.nama!r}, umur={self.umur!r}, hobi={self.hobi!r})"

    def __eq__(self, other):
        if not isinstance(other, PersonTraditional):
            return NotImplemented
        return (self.nama, self.umur, self.hobi) == (other.nama, other.umur, other.hobi)

# Dengan dataclass (clean!)


@dataclass
class Person:
    """Dataclass otomatis generate __init__, __repr__, __eq__"""
    nama: str
    umur: int
    hobi: List[str] = field(default_factory=list)  # Mutable default

    def ultah(self):
        """Custom method tetap bisa ditambahkan"""
        self.umur += 1
        print(f"Happy birthday {self.nama}! Now {self.umur} years old")


print("2. DATACLASS")
print("-" * 50)

person1 = Person("Alice", 25, ["reading", "coding"])
person2 = Person("Bob", 30)

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"person1 == person2: {person1 == person2}")
print()

person1.ultah()
print(f"After birthday: {person1}")
print()


# ============================================
# 3. DATACLASS OPTIONS
# ============================================

@dataclass(frozen=True)  # Immutable
class Point:
    x: float
    y: float


@dataclass(order=True)  # Enable comparison operators
class Student:
    nama: str = field(compare=False)  # Tidak dipakai untuk comparison
    ipk: float


@dataclass
class Product:
    nama: str
    harga: float
    stok: int = 0
    # Field dengan metadata
    kategori: str = field(default="General", metadata={
                          "description": "Product category"})

    def __post_init__(self):
        """Dipanggil setelah __init__"""
        if self.harga < 0:
            raise ValueError("Harga tidak boleh negatif")


print("3. DATACLASS OPTIONS")
print("-" * 50)

# Frozen (immutable)
point = Point(3.0, 4.0)
print(f"Point: {point}")
try:
    point.x = 5.0  # ❌ Error - frozen
except Exception as e:
    print(f"Error: {e}")
print()

# Order (sortable)
students = [
    Student("Alice", 3.8),
    Student("Bob", 3.5),
    Student("Charlie", 3.9)
]
print("Before sort:", [f"{s.nama}:{s.ipk}" for s in students])
students.sort()
print("After sort:", [f"{s.nama}:{s.ipk}" for s in students])
print()

# Post init validation
try:
    prod = Product("Laptop", -5000)
except ValueError as e:
    print(f"Validation error: {e}")
print()


# ============================================
# 4. PROPERTY vs ATTRIBUTE
# ============================================

@dataclass
class Employee:
    nama: str
    gaji_pokok: float
    tunjangan: float = 0

    @property
    def gaji_total(self):
        """Computed property"""
        return self.gaji_pokok + self.tunjangan

    @property
    def pajak(self):
        """10% dari gaji total"""
        return self.gaji_total * 0.1

    @property
    def gaji_bersih(self):
        """Gaji total - pajak"""
        return self.gaji_total - self.pajak


print("4. PROPERTY vs ATTRIBUTE")
print("-" * 50)

emp = Employee("John", 5000000, 1000000)
print(f"Nama: {emp.nama}")
print(f"Gaji pokok: Rp{emp.gaji_pokok:,}")
print(f"Tunjangan: Rp{emp.tunjangan:,}")
print(f"Gaji total: Rp{emp.gaji_total:,}")
print(f"Pajak: Rp{emp.pajak:,}")
print(f"Gaji bersih: Rp{emp.gaji_bersih:,}")
print()


# ============================================
# 5. SINGLETON PATTERN
# ============================================

class DatabaseConnection:
    """Singleton - hanya satu instance"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_count = 0
        return cls._instance

    def connect(self):
        self.connection_count += 1
        print(f"Connected! (Total connections: {self.connection_count})")


print("5. SINGLETON PATTERN")
print("-" * 50)

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

print(f"db1 is db2: {db1 is db2}")
print(f"db2 is db3: {db2 is db3}")
print()

db1.connect()
db2.connect()  # Same instance!
print()


# ============================================
# 6. FACTORY PATTERN
# ============================================


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Driving a car 🚗"


class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle 🏍️"


class Truck(Vehicle):
    def drive(self):
        return "Driving a truck 🚚"


class VehicleFactory:
    """Factory untuk membuat vehicle"""

    @staticmethod
    def create_vehicle(vehicle_type):
        vehicles = {
            'car': Car,
            'motorcycle': Motorcycle,
            'truck': Truck
        }

        vehicle_class = vehicles.get(vehicle_type.lower())
        if vehicle_class:
            return vehicle_class()
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")


print("6. FACTORY PATTERN")
print("-" * 50)

# Membuat vehicles menggunakan factory
for vtype in ['car', 'motorcycle', 'truck']:
    vehicle = VehicleFactory.create_vehicle(vtype)
    print(f"{vtype.capitalize()}: {vehicle.drive()}")
print()


# ============================================
# 7. BUILDER PATTERN
# ============================================

@dataclass
class Pizza:
    """Pizza yang akan dibangun"""
    size: str = "medium"
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    olives: bool = False

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        if self.olives:
            toppings.append("olives")

        topping_str = ", ".join(toppings) if toppings else "plain"
        return f"{self.size.capitalize()} pizza with {topping_str}"


class PizzaBuilder:
    """Builder untuk membuat pizza step by step"""

    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size):
        self._pizza.size = size
        return self  # Return self untuk method chaining

    def add_cheese(self):
        self._pizza.cheese = True
        return self

    def add_pepperoni(self):
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self._pizza.mushrooms = True
        return self

    def add_olives(self):
        self._pizza.olives = True
        return self

    def build(self):
        return self._pizza


print("7. BUILDER PATTERN")
print("-" * 50)

# Build pizza dengan method chaining
pizza1 = (PizzaBuilder()
          .set_size("large")
          .add_cheese()
          .add_pepperoni()
          .add_mushrooms()
          .build())

pizza2 = (PizzaBuilder()
          .set_size("small")
          .add_cheese()
          .add_olives()
          .build())

print(f"Pizza 1: {pizza1}")
print(f"Pizza 2: {pizza2}")
print()


# ============================================
# 8. OBSERVER PATTERN
# ============================================

class Subject:
    """Subject yang akan di-observe"""

    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        """Tambah observer"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Hapus observer"""
        self._observers.remove(observer)

    def notify(self):
        """Notify semua observers"""
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        """Update state dan notify observers"""
        self._state = state
        print(f"Subject: State changed to {state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass


class EmailNotifier(Observer):
    def update(self, state):
        print(f"  EmailNotifier: Sending email about {state}")


class SMSNotifier(Observer):
    def update(self, state):
        print(f"  SMSNotifier: Sending SMS about {state}")


class LogNotifier(Observer):
    def update(self, state):
        print(f"  LogNotifier: Logging event - {state}")


print("8. OBSERVER PATTERN")
print("-" * 50)

# Setup subject and observers
subject = Subject()
email = EmailNotifier()
sms = SMSNotifier()
log = LogNotifier()

subject.attach(email)
subject.attach(sms)
subject.attach(log)

# Change state - semua observers di-notify
subject.set_state("Order Placed")
print()
subject.set_state("Order Shipped")
print()


# ============================================
# 9. PRAKTIK: E-COMMERCE SYSTEM
# ============================================


class OrderStatus(Enum):
    """Enum untuk status order"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@dataclass
class OrderItem:
    product_name: str
    quantity: int
    price: float

    @property
    def subtotal(self):
        return self.quantity * self.price


@dataclass
class Order:
    order_id: str
    customer_name: str
    items: List[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)

    def add_item(self, item: OrderItem):
        self.items.append(item)

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)

    @property
    def item_count(self):
        return sum(item.quantity for item in self.items)

    def __str__(self):
        items_str = "\n".join([
            f"  - {item.product_name} x{item.quantity} @ Rp{item.price:,} = Rp{item.subtotal:,}"
            for item in self.items
        ])
        return f"""
Order #{self.order_id}
Customer: {self.customer_name}
Status: {self.status.value}
Created: {self.created_at.strftime('%Y-%m-%d %H:%M')}
Items:
{items_str}
Total: Rp{self.total:,} ({self.item_count} items)
        """.strip()


class OrderFactory:
    """Factory untuk membuat orders"""

    _order_counter = 1000

    @classmethod
    def create_order(cls, customer_name):
        order_id = f"ORD{cls._order_counter}"
        cls._order_counter += 1
        return Order(order_id, customer_name)


class OrderManager:
    """Singleton untuk manage semua orders"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = []
        return cls._instance

    def add_order(self, order):
        self.orders.append(order)
        print(f"✓ Order {order.order_id} ditambahkan")

    def get_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def get_orders_by_status(self, status: OrderStatus):
        return [o for o in self.orders if o.status == status]

    @property
    def total_orders(self):
        return len(self.orders)

    @property
    def total_revenue(self):
        return sum(o.total for o in self.orders)


print("9. PRAKTIK: E-COMMERCE SYSTEM")
print("-" * 50)

# Create orders using factory
order1 = OrderFactory.create_order("Alice")
order1.add_item(OrderItem("Laptop", 1, 10000000))
order1.add_item(OrderItem("Mouse", 2, 200000))

order2 = OrderFactory.create_order("Bob")
order2.add_item(OrderItem("Keyboard", 1, 500000))
order2.add_item(OrderItem("Monitor", 1, 3000000))

# Add to order manager (singleton)
manager = OrderManager()
manager.add_order(order1)
manager.add_order(order2)
print()

# Display orders
print(order1)
print("\n" + "="*50 + "\n")
print(order2)
print("\n" + "="*50 + "\n")

# Update status
order1.status = OrderStatus.PROCESSING
order2.status = OrderStatus.SHIPPED

# Manager statistics
print("ORDER MANAGER STATISTICS:")
print(f"Total orders: {manager.total_orders}")
print(f"Total revenue: Rp{manager.total_revenue:,}")
print(
    f"Pending orders: {len(manager.get_orders_by_status(OrderStatus.PENDING))}")
print(
    f"Processing orders: {len(manager.get_orders_by_status(OrderStatus.PROCESSING))}")
print(
    f"Shipped orders: {len(manager.get_orders_by_status(OrderStatus.SHIPPED))}")
print()


# ============================================
# 10. SUMMARY
# ============================================

print("=" * 60)
print("SUMMARY - ADVANCED OOP CONCEPTS")
print("=" * 60)
print("""
1. STATIC vs CLASS vs INSTANCE METHODS
   Instance method: def method(self, ...)
   - Butuh instance, akses instance data
   
   Static method: @staticmethod def method(...)
   - Tidak butuh instance/class
   - Utility function dalam class namespace
   
   Class method: @classmethod def method(cls, ...)
   - Menerima class sebagai parameter
   - Factory methods, alternative constructors

2. DATACLASS (@dataclass)
   ✓ Auto-generate __init__, __repr__, __eq__
   ✓ Type hints
   ✓ Default values
   ✓ Immutable (frozen=True)
   ✓ Ordering (order=True)
   ✓ Post-init processing (__post_init__)

3. DESIGN PATTERNS

   SINGLETON - Satu instance saja
   - Gunakan __new__ untuk kontrol instance
   - Use case: Database connection, config, logger
   
   FACTORY - Membuat objects
   - Centralize object creation logic
   - Use case: Different product types
   
   BUILDER - Build complex objects step by step
   - Method chaining
   - Use case: Complex configuration objects
   
   OBSERVER - Subscribe to state changes
   - Subject maintains list of observers
   - Use case: Event systems, notifications

4. ENUM - Enumerations
   from enum import Enum
   - Named constants
   - Type-safe choices
   - Better than string constants

5. BEST PRACTICES
   ✓ Use dataclass for data containers
   ✓ Use static methods for utilities
   ✓ Use class methods for factories
   ✓ Singleton sparingly (global state)
   ✓ Factory for object creation logic
   ✓ Builder for complex objects
   ✓ Observer for event-driven systems
   
6. KAPAN PAKAI APA?
   
   Dataclass:
   ✓ Simple data containers
   ✓ Immutable data objects
   ✓ Configuration objects
   
   Static method:
   ✓ Utility functions related to class
   ✓ No access to instance/class needed
   
   Class method:
   ✓ Factory/alternative constructors
   ✓ Access to class variables
   
   Design Patterns:
   ✓ When you have a common problem
   ✓ Don't over-engineer
   ✓ Use when it makes code clearer

7. PYTHON-SPECIFIC FEATURES
   ✓ Properties for computed attributes
   ✓ Dataclasses for less boilerplate
   ✓ Duck typing over strict interfaces
   ✓ Context managers for resources
   ✓ Decorators for cross-cutting concerns
""")
