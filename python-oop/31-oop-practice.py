"""
OOP PRAKTIK LENGKAP: Library Management System
===============================================
Studi kasus implementasi semua konsep OOP yang sudah dipelajari:
- Class & Object
- Encapsulation & Property
- Inheritance
- Polymorphism
- Magic Methods
- Dataclass
- Design Patterns
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional
from abc import ABC, abstractmethod
from enum import Enum

# ============================================
# ENUMS
# ============================================


class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"


class MemberType(Enum):
    REGULAR = "regular"
    PREMIUM = "premium"
    STUDENT = "student"


class TransactionType(Enum):
    BORROW = "borrow"
    RETURN = "return"
    RESERVE = "reserve"
    FINE = "fine"


# ============================================
# BASE CLASSES & ABSTRACT CLASSES
# ============================================

class Item(ABC):
    """Abstract base class untuk semua item di library"""

    _id_counter = 1000

    def __init__(self, title, author):
        self._id = f"ITEM{Item._id_counter}"
        Item._id_counter += 1
        self._title = title
        self._author = author
        self._status = BookStatus.AVAILABLE

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, BookStatus):
            raise ValueError("Status must be BookStatus enum")
        self._status = new_status

    @abstractmethod
    def borrow_duration(self):
        """Lama peminjaman (hari)"""
        pass

    @abstractmethod
    def fine_per_day(self):
        """Denda per hari"""
        pass

    def __str__(self):
        return f"[{self.id}] {self.title} by {self.author} ({self.status.value})"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', '{self.author}')"


# ============================================
# CONCRETE ITEM CLASSES
# ============================================

class Book(Item):
    """Buku regular"""

    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author)
        self.isbn = isbn
        self.pages = pages

    def borrow_duration(self):
        return 14  # 2 minggu

    def fine_per_day(self):
        return 1000  # Rp1.000/hari


class Magazine(Item):
    """Majalah"""

    def __init__(self, title, author, issue, month):
        super().__init__(title, author)
        self.issue = issue
        self.month = month

    def borrow_duration(self):
        return 7  # 1 minggu

    def fine_per_day(self):
        return 500  # Rp500/hari


class DVD(Item):
    """DVD"""

    def __init__(self, title, director, duration_minutes):
        super().__init__(title, director)
        self.duration_minutes = duration_minutes

    def borrow_duration(self):
        return 3  # 3 hari

    def fine_per_day(self):
        return 2000  # Rp2.000/hari


# ============================================
# MEMBER CLASSES
# ============================================

class Member:
    """Base class untuk member perpustakaan"""

    _member_counter = 1000

    def __init__(self, nama, email, member_type):
        self._id = f"MBR{Member._member_counter}"
        Member._member_counter += 1
        self._nama = nama
        self._email = email
        self._member_type = member_type
        self._borrowed_items = []
        self._transaction_history = []
        self._fine_balance = 0

    @property
    def id(self):
        return self._id

    @property
    def nama(self):
        return self._nama

    @property
    def email(self):
        return self._email

    @property
    def member_type(self):
        return self._member_type

    @property
    def borrowed_items(self):
        return self._borrowed_items.copy()

    @property
    def fine_balance(self):
        return self._fine_balance

    @property
    def max_borrow_limit(self):
        """Polymorphism - akan di-override di subclass"""
        limits = {
            MemberType.REGULAR: 3,
            MemberType.STUDENT: 5,
            MemberType.PREMIUM: 10
        }
        return limits.get(self._member_type, 3)

    def can_borrow(self):
        """Cek apakah bisa meminjam"""
        if len(self._borrowed_items) >= self.max_borrow_limit:
            return False, "Sudah mencapai limit peminjaman"
        if self._fine_balance > 0:
            return False, f"Ada denda yang harus dibayar: Rp{self._fine_balance:,}"
        return True, "OK"

    def borrow_item(self, item, due_date):
        """Pinjam item"""
        self._borrowed_items.append({
            'item': item,
            'borrowed_date': datetime.now(),
            'due_date': due_date
        })

    def return_item(self, item):
        """Kembalikan item"""
        for i, borrowed in enumerate(self._borrowed_items):
            if borrowed['item'].id == item.id:
                del self._borrowed_items[i]
                return borrowed
        return None

    def add_fine(self, amount):
        """Tambah denda"""
        self._fine_balance += amount

    def pay_fine(self, amount):
        """Bayar denda"""
        if amount > self._fine_balance:
            amount = self._fine_balance
        self._fine_balance -= amount
        return amount

    def add_transaction(self, transaction):
        """Tambah riwayat transaksi"""
        self._transaction_history.append(transaction)

    def __str__(self):
        return f"{self.nama} ({self.id}) - {self.member_type.value} | Borrowed: {len(self._borrowed_items)}/{self.max_borrow_limit}"

    def __eq__(self, other):
        if not isinstance(other, Member):
            return NotImplemented
        return self.id == other.id


# ============================================
# TRANSACTION
# ============================================

@dataclass
class Transaction:
    """Transaction record dengan dataclass"""

    transaction_id: str
    member: Member
    item: Optional[Item]
    transaction_type: TransactionType
    date: datetime = field(default_factory=datetime.now)
    amount: float = 0.0
    notes: str = ""

    def __str__(self):
        item_info = f"{self.item.title}" if self.item else "N/A"
        return (f"[{self.transaction_id}] {self.transaction_type.value.upper()} - "
                f"{self.member.nama} - {item_info} - Rp{self.amount:,}")


# ============================================
# LIBRARY SYSTEM (SINGLETON)
# ============================================

class Library:
    """Singleton Library Management System"""

    _instance = None

    def __new__(cls, name="Public Library"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, name="Public Library"):
        if self._initialized:
            return

        self.name = name
        self._items = []
        self._members = []
        self._transactions = []
        self._transaction_counter = 1000
        self._initialized = True

    # Item Management
    def add_item(self, item):
        """Tambah item ke library"""
        self._items.append(item)
        print(f"✓ Item ditambahkan: {item}")

    def get_item(self, item_id):
        """Cari item by ID"""
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def search_items(self, keyword):
        """Cari items by keyword"""
        keyword = keyword.lower()
        results = []
        for item in self._items:
            if (keyword in item.title.lower() or
                    keyword in item.author.lower()):
                results.append(item)
        return results

    def get_available_items(self):
        """List semua item available"""
        return [item for item in self._items if item.status == BookStatus.AVAILABLE]

    # Member Management
    def register_member(self, member):
        """Register member baru"""
        self._members.append(member)
        print(f"✓ Member terdaftar: {member}")

    def get_member(self, member_id):
        """Cari member by ID"""
        for member in self._members:
            if member.id == member_id:
                return member
        return None

    # Transaction Management
    def _generate_transaction_id(self):
        """Generate transaction ID"""
        trans_id = f"TXN{self._transaction_counter}"
        self._transaction_counter += 1
        return trans_id

    def borrow_item(self, member_id, item_id):
        """Proses peminjaman"""
        member = self.get_member(member_id)
        item = self.get_item(item_id)

        if not member:
            return False, "Member tidak ditemukan"
        if not item:
            return False, "Item tidak ditemukan"

        # Validasi member
        can_borrow, message = member.can_borrow()
        if not can_borrow:
            return False, message

        # Validasi item
        if item.status != BookStatus.AVAILABLE:
            return False, f"Item tidak available: {item.status.value}"

        # Process borrowing
        due_date = datetime.now() + timedelta(days=item.borrow_duration())
        member.borrow_item(item, due_date)
        item.status = BookStatus.BORROWED

        # Create transaction
        transaction = Transaction(
            transaction_id=self._generate_transaction_id(),
            member=member,
            item=item,
            transaction_type=TransactionType.BORROW,
            notes=f"Due: {due_date.strftime('%Y-%m-%d')}"
        )
        self._transactions.append(transaction)
        member.add_transaction(transaction)

        print(f"✓ Peminjaman berhasil!")
        print(f"  Item: {item.title}")
        print(f"  Due date: {due_date.strftime('%Y-%m-%d')}")

        return True, "Peminjaman berhasil"

    def return_item(self, member_id, item_id):
        """Proses pengembalian"""
        member = self.get_member(member_id)
        item = self.get_item(item_id)

        if not member or not item:
            return False, "Member atau item tidak ditemukan"

        # Cari borrowed record
        borrowed = member.return_item(item)
        if not borrowed:
            return False, "Item tidak dipinjam oleh member ini"

        # Hitung denda jika terlambat
        due_date = borrowed['due_date']
        now = datetime.now()
        fine_amount = 0

        if now > due_date:
            days_late = (now - due_date).days
            fine_amount = days_late * item.fine_per_day()
            member.add_fine(fine_amount)
            print(f"⚠ Terlambat {days_late} hari. Denda: Rp{fine_amount:,}")

        # Update item status
        item.status = BookStatus.AVAILABLE

        # Create transaction
        transaction = Transaction(
            transaction_id=self._generate_transaction_id(),
            member=member,
            item=item,
            transaction_type=TransactionType.RETURN,
            amount=fine_amount,
            notes=f"Returned on time" if fine_amount == 0 else f"Late {days_late} days"
        )
        self._transactions.append(transaction)
        member.add_transaction(transaction)

        print(f"✓ Pengembalian berhasil!")
        return True, "Pengembalian berhasil"

    def pay_fine(self, member_id, amount):
        """Bayar denda"""
        member = self.get_member(member_id)
        if not member:
            return False, "Member tidak ditemukan"

        paid = member.pay_fine(amount)

        # Create transaction
        transaction = Transaction(
            transaction_id=self._generate_transaction_id(),
            member=member,
            item=None,
            transaction_type=TransactionType.FINE,
            amount=paid,
            notes=f"Fine payment"
        )
        self._transactions.append(transaction)
        member.add_transaction(transaction)

        print(f"✓ Pembayaran denda: Rp{paid:,}")
        print(f"  Sisa denda: Rp{member.fine_balance:,}")
        return True, f"Pembayaran berhasil"

    # Statistics & Reports
    def get_statistics(self):
        """Library statistics"""
        total_items = len(self._items)
        available = len(
            [i for i in self._items if i.status == BookStatus.AVAILABLE])
        borrowed = len(
            [i for i in self._items if i.status == BookStatus.BORROWED])
        total_members = len(self._members)
        total_transactions = len(self._transactions)
        total_fines = sum(m.fine_balance for m in self._members)

        return {
            'total_items': total_items,
            'available': available,
            'borrowed': borrowed,
            'total_members': total_members,
            'total_transactions': total_transactions,
            'total_fines': total_fines
        }

    def print_statistics(self):
        """Print statistics"""
        stats = self.get_statistics()
        print(f"\n{'='*60}")
        print(f"{self.name.upper()} - STATISTICS")
        print(f"{'='*60}")
        print(f"Total Items: {stats['total_items']}")
        print(f"  - Available: {stats['available']}")
        print(f"  - Borrowed: {stats['borrowed']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Total Transactions: {stats['total_transactions']}")
        print(f"Total Outstanding Fines: Rp{stats['total_fines']:,}")
        print(f"{'='*60}\n")


# ============================================
# MAIN PROGRAM - DEMO
# ============================================

def main():
    print("="*60)
    print("LIBRARY MANAGEMENT SYSTEM - DEMO")
    print("="*60)
    print()

    # Create library (singleton)
    lib = Library("Perpustakaan Umum Jakarta")

    # Add items
    print("1. MENAMBAH ITEMS")
    print("-" * 50)
    lib.add_item(Book("Python Crash Course",
                 "Eric Matthes", "978-1593279288", 544))
    lib.add_item(Book("Clean Code", "Robert Martin", "978-0132350884", 464))
    lib.add_item(
        Book("Design Patterns", "Gang of Four", "978-0201633610", 395))
    lib.add_item(Magazine("National Geographic",
                 "Various", "Issue 5", "May 2024"))
    lib.add_item(DVD("The Matrix", "Wachowski", 136))
    print()

    # Register members
    print("2. REGISTRASI MEMBERS")
    print("-" * 50)
    alice = Member("Alice Johnson", "alice@email.com", MemberType.PREMIUM)
    bob = Member("Bob Smith", "bob@email.com", MemberType.STUDENT)
    charlie = Member("Charlie Brown", "charlie@email.com", MemberType.REGULAR)

    lib.register_member(alice)
    lib.register_member(bob)
    lib.register_member(charlie)
    print()

    # Borrow items
    print("3. PEMINJAMAN ITEMS")
    print("-" * 50)
    lib.borrow_item(alice.id, "ITEM1000")  # Python Crash Course
    lib.borrow_item(alice.id, "ITEM1001")  # Clean Code
    lib.borrow_item(bob.id, "ITEM1003")    # National Geographic
    lib.borrow_item(charlie.id, "ITEM1004")  # The Matrix
    print()

    # Try to borrow when fine exists (simulate)
    print("4. SIMULASI DENDA")
    print("-" * 50)
    charlie.add_fine(5000)
    print(f"Denda Charlie ditambahkan: Rp{charlie.fine_balance:,}")
    success, msg = lib.borrow_item(charlie.id, "ITEM1002")
    print(f"Coba pinjam lagi: {msg}")
    print()

    # Pay fine
    print("5. BAYAR DENDA")
    print("-" * 50)
    lib.pay_fine(charlie.id, 5000)
    print()

    # Return items
    print("6. PENGEMBALIAN ITEMS")
    print("-" * 50)
    lib.return_item(alice.id, "ITEM1000")
    lib.return_item(bob.id, "ITEM1003")
    print()

    # Search items
    print("7. PENCARIAN ITEMS")
    print("-" * 50)
    results = lib.search_items("python")
    print(f"Hasil pencarian 'python': {len(results)} item")
    for item in results:
        print(f"  - {item}")
    print()

    # Show available items
    print("8. ITEMS AVAILABLE")
    print("-" * 50)
    available = lib.get_available_items()
    print(f"Total available: {len(available)}")
    for item in available:
        print(f"  - {item}")
    print()

    # Show member info
    print("9. INFO MEMBER")
    print("-" * 50)
    print(alice)
    print(f"  Borrowed items: {len(alice.borrowed_items)}")
    for borrowed in alice.borrowed_items:
        item = borrowed['item']
        due = borrowed['due_date'].strftime('%Y-%m-%d')
        print(f"    - {item.title} (Due: {due})")
    print()

    # Statistics
    lib.print_statistics()


if __name__ == "__main__":
    main()

    print("\n" + "="*60)
    print("KONSEP OOP YANG DIGUNAKAN:")
    print("="*60)
    print("""
    ✓ Class & Object - Book, Magazine, DVD, Member, Library
    ✓ Encapsulation - Private attributes dengan property
    ✓ Inheritance - Item sebagai base class
    ✓ Polymorphism - borrow_duration(), fine_per_day()
    ✓ Abstract Class - Item dengan abstractmethod
    ✓ Magic Methods - __str__, __repr__, __eq__
    ✓ Dataclass - Transaction
    ✓ Enum - BookStatus, MemberType, TransactionType
    ✓ Singleton Pattern - Library
    ✓ Properties - Computed values (max_borrow_limit)
    ✓ Composition - Member has borrowed_items
    """)
