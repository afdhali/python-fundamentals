"""
OOP Part 4: Polymorphism & Magic Methods
=========================================
Polymorphism = Kemampuan object berbeda merespon method yang sama dengan cara berbeda
Magic Methods = Special methods dengan __ (dunder) untuk operator overloading
"""

# ============================================
# 1. POLYMORPHISM BASICS
# ============================================


class Anjing:
    def suara(self):
        return "Guk guk!"

    def jenis(self):
        return "Anjing"


class Kucing:
    def suara(self):
        return "Meow!"

    def jenis(self):
        return "Kucing"


class Burung:
    def suara(self):
        return "Cuit cuit!"

    def jenis(self):
        return "Burung"


def buat_suara(hewan):
    """Polymorphic function - menerima object apapun yang punya method suara()"""
    print(f"{hewan.jenis()}: {hewan.suara()}")


print("1. POLYMORPHISM BASICS")
print("-" * 50)

anjing = Anjing()
kucing = Kucing()
burung = Burung()

# Polymorphism - same method, different behavior
buat_suara(anjing)
buat_suara(kucing)
buat_suara(burung)
print()

# List polymorphism
hewan_list = [anjing, kucing, burung]
for hewan in hewan_list:
    buat_suara(hewan)
print()


# ============================================
# 2. DUCK TYPING
# ============================================

class Bebek:
    def terbang(self):
        return "Bebek terbang"

    def suara(self):
        return "Kwek kwek!"


class Pesawat:
    def terbang(self):
        return "Pesawat terbang"

    def suara(self):
        return "Wuuuussshhh!"


class Superman:
    def terbang(self):
        return "Superman terbang"

    def suara(self):
        return "Up, up and away!"


def terbang_sekarang(obj):
    """
    Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck"
    Tidak peduli tipe object, asal punya method yang dibutuhkan
    """
    print(f"- {obj.terbang()}")
    print(f"- {obj.suara()}")


print("2. DUCK TYPING")
print("-" * 50)

bebek = Bebek()
pesawat = Pesawat()
superman = Superman()

terbang_sekarang(bebek)
print()
terbang_sekarang(pesawat)
print()
terbang_sekarang(superman)
print()


# ============================================
# 3. OPERATOR OVERLOADING - COMPARISON
# ============================================

class Mahasiswa:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.ipk = ipk

    # Comparison operators
    def __eq__(self, other):
        """Equal to (==)"""
        return self.ipk == other.ipk

    def __ne__(self, other):
        """Not equal to (!=)"""
        return self.ipk != other.ipk

    def __lt__(self, other):
        """Less than (<)"""
        return self.ipk < other.ipk

    def __le__(self, other):
        """Less than or equal to (<=)"""
        return self.ipk <= other.ipk

    def __gt__(self, other):
        """Greater than (>)"""
        return self.ipk > other.ipk

    def __ge__(self, other):
        """Greater than or equal to (>=)"""
        return self.ipk >= other.ipk

    def __str__(self):
        return f"{self.nama} (IPK: {self.ipk})"


print("3. OPERATOR OVERLOADING - COMPARISON")
print("-" * 50)

mhs1 = Mahasiswa("Alice", 3.8)
mhs2 = Mahasiswa("Bob", 3.5)
mhs3 = Mahasiswa("Charlie", 3.8)

print(f"{mhs1} == {mhs3}: {mhs1 == mhs3}")
print(f"{mhs1} != {mhs2}: {mhs1 != mhs2}")
print(f"{mhs1} > {mhs2}: {mhs1 > mhs2}")
print(f"{mhs2} < {mhs1}: {mhs2 < mhs1}")
print()

# Sorting dengan operator
mahasiswa_list = [mhs1, mhs2, mhs3]
print("Sebelum sorting:", [str(m) for m in mahasiswa_list])
mahasiswa_list.sort()
print("Setelah sorting:", [str(m) for m in mahasiswa_list])
print()


# ============================================
# 4. OPERATOR OVERLOADING - ARITHMETIC
# ============================================

class Vector2D:
    """Vector 2D dengan operator overloading"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Arithmetic operators
    def __add__(self, other):
        """Addition (+)"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtraction (-)"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiplication with scalar (*)"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """Division (/)"""
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __abs__(self):
        """Absolute value / magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __neg__(self):
        """Negation (-)"""
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


print("4. OPERATOR OVERLOADING - ARITHMETIC")
print("-" * 50)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 / 2 = {v1 / 2}")
print(f"|v1| = {abs(v1)}")
print(f"-v1 = {-v1}")
print()


# ============================================
# 5. CONTAINER MAGIC METHODS
# ============================================

class Playlist:
    """Custom container dengan magic methods"""

    def __init__(self, nama):
        self.nama = nama
        self.lagu = []

    def __len__(self):
        """len() function"""
        return len(self.lagu)

    def __getitem__(self, index):
        """Indexing and slicing (playlist[0])"""
        return self.lagu[index]

    def __setitem__(self, index, value):
        """Assignment (playlist[0] = "new song")"""
        self.lagu[index] = value

    def __delitem__(self, index):
        """del playlist[0]"""
        del self.lagu[index]

    def __contains__(self, item):
        """'in' operator"""
        return item in self.lagu

    def __iter__(self):
        """Make it iterable (for loop)"""
        return iter(self.lagu)

    def tambah(self, lagu):
        """Tambah lagu"""
        self.lagu.append(lagu)

    def __str__(self):
        return f"Playlist '{self.nama}' ({len(self)} lagu)"


print("5. CONTAINER MAGIC METHODS")
print("-" * 50)

playlist = Playlist("My Favorites")
playlist.tambah("Song A")
playlist.tambah("Song B")
playlist.tambah("Song C")

print(playlist)
print(f"Jumlah lagu: {len(playlist)}")
print(f"Lagu pertama: {playlist[0]}")
print(f"'Song B' in playlist: {'Song B' in playlist}")
print(f"'Song Z' in playlist: {'Song Z' in playlist}")
print()

print("Iterasi playlist:")
for i, lagu in enumerate(playlist, 1):
    print(f"  {i}. {lagu}")
print()

# Slicing
print(f"Slicing [1:]: {playlist[1:]}")
print()


# ============================================
# 6. CALLABLE OBJECTS
# ============================================

class Multiplier:
    """Object yang bisa dipanggil seperti function"""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Make object callable"""
        return x * self.factor


class Formatter:
    """Formatter yang bisa dipanggil"""

    def __init__(self, prefix="", suffix=""):
        self.prefix = prefix
        self.suffix = suffix

    def __call__(self, text):
        return f"{self.prefix}{text}{self.suffix}"


print("6. CALLABLE OBJECTS")
print("-" * 50)

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print()

bold = Formatter("<b>", "</b>")
italic = Formatter("<i>", "</i>")

print(f"bold('Hello') = {bold('Hello')}")
print(f"italic('World') = {italic('World')}")
print()


# ============================================
# 7. CONTEXT MANAGER
# ============================================

class FileManager:
    """Custom context manager dengan __enter__ dan __exit__"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Called when entering 'with' block"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block"""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False


class Timer:
    """Context manager untuk timing"""

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, *args):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Elapsed time: {self.elapsed:.4f} seconds")


print("7. CONTEXT MANAGER")
print("-" * 50)

# Menggunakan context manager
with FileManager('/tmp/test.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a test.\n")
print()

with Timer():
    # Simulate some work
    total = sum(range(1000000))
    print(f"Sum calculated: {total}")
print()


# ============================================
# 8. PRAKTIK: SHOPPING CART SYSTEM
# ============================================

class Product:
    """Product dengan operator overloading"""

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama} (Rp{self.harga:,})"

    def __repr__(self):
        return f"Product('{self.nama}', {self.harga})"

    def __eq__(self, other):
        """Products equal if same name and price"""
        return self.nama == other.nama and self.harga == other.harga

    def __hash__(self):
        """Make it hashable for use in sets/dicts"""
        return hash((self.nama, self.harga))


class CartItem:
    """Item in cart with quantity"""

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self):
        return self.product.harga * self.quantity

    def __add__(self, other):
        """Add quantities"""
        if isinstance(other, CartItem) and self.product == other.product:
            return CartItem(self.product, self.quantity + other.quantity)
        raise ValueError("Cannot add different products")

    def __mul__(self, factor):
        """Multiply quantity"""
        return CartItem(self.product, self.quantity * factor)

    def __str__(self):
        return f"{self.product.nama} x{self.quantity} = Rp{self.subtotal:,}"


class ShoppingCart:
    """Shopping cart with magic methods"""

    def __init__(self):
        self.items = []

    def __len__(self):
        """Total items in cart"""
        return sum(item.quantity for item in self.items)

    def __getitem__(self, index):
        """Get item by index"""
        return self.items[index]

    def __iter__(self):
        """Iterate through items"""
        return iter(self.items)

    def __contains__(self, product):
        """Check if product in cart"""
        return any(item.product == product for item in self.items)

    def __iadd__(self, cart_item):
        """+= operator to add items"""
        # Check if product already in cart
        for i, item in enumerate(self.items):
            if item.product == cart_item.product:
                self.items[i] = item + cart_item
                return self
        self.items.append(cart_item)
        return self

    def __bool__(self):
        """Cart is True if has items"""
        return len(self.items) > 0

    @property
    def total(self):
        """Total price"""
        return sum(item.subtotal for item in self.items)

    def __str__(self):
        if not self.items:
            return "Cart is empty"

        result = "SHOPPING CART:\n"
        result += "-" * 50 + "\n"
        for i, item in enumerate(self.items, 1):
            result += f"{i}. {item}\n"
        result += "-" * 50 + "\n"
        result += f"Total: Rp{self.total:,} ({len(self)} items)"
        return result


print("8. PRAKTIK: SHOPPING CART SYSTEM")
print("-" * 50)

# Create products
laptop = Product("Laptop", 10000000)
mouse = Product("Mouse", 200000)
keyboard = Product("Keyboard", 500000)

# Create cart
cart = ShoppingCart()

# Add items using += operator
cart += CartItem(laptop, 1)
cart += CartItem(mouse, 2)
cart += CartItem(keyboard, 1)

print(cart)
print()

# Check if product in cart
print(f"Laptop in cart: {laptop in cart}")
print(f"Total items: {len(cart)}")
print()

# Add more of existing product
cart += CartItem(mouse, 3)
print("After adding 3 more mice:")
print(cart)
print()

# Iterate through cart
print("Individual items:")
for item in cart:
    print(f"  - {item}")
print()


# ============================================
# 9. SUMMARY
# ============================================

print("=" * 60)
print("SUMMARY - POLYMORPHISM & MAGIC METHODS")
print("=" * 60)
print("""
1. POLYMORPHISM
   - Same interface, different implementation
   - Duck typing: "If it walks like a duck..."
   - Tidak perlu inheritance untuk polymorphism

2. COMPARISON OPERATORS
   __eq__(self, other)     # ==
   __ne__(self, other)     # !=
   __lt__(self, other)     # <
   __le__(self, other)     # <=
   __gt__(self, other)     # >
   __ge__(self, other)     # >=

3. ARITHMETIC OPERATORS
   __add__(self, other)    # +
   __sub__(self, other)    # -
   __mul__(self, other)    # *
   __truediv__(self, other)# /
   __floordiv__(self, other)# //
   __mod__(self, other)    # %
   __pow__(self, other)    # **
   __neg__(self)           # -x
   __abs__(self)           # abs(x)

4. CONTAINER METHODS
   __len__(self)           # len()
   __getitem__(self, key)  # obj[key]
   __setitem__(self, key, val) # obj[key] = val
   __delitem__(self, key)  # del obj[key]
   __contains__(self, item)# item in obj
   __iter__(self)          # for item in obj

5. STRING REPRESENTATION
   __str__(self)           # str(), print()
   __repr__(self)          # repr(), debugging
   __format__(self, spec)  # format()

6. CALLABLE & CONTEXT
   __call__(self, ...)     # obj()
   __enter__(self)         # with obj:
   __exit__(self, ...)     # exit with block

7. OTHER USEFUL MAGIC METHODS
   __bool__(self)          # bool(), if obj:
   __hash__(self)          # hash(), set/dict
   __sizeof__(self)        # sys.getsizeof()

8. BEST PRACTICES
   ✓ Implement related operators together
   ✓ __eq__ and __hash__ together for hashable
   ✓ Return NotImplemented for incompatible types
   ✓ __str__ user-friendly, __repr__ developer-friendly
   ✓ Use @property for computed attributes
   ✓ Context managers for resource management

9. KAPAN PAKAI MAGIC METHODS?
   ✓ Custom containers/collections
   ✓ Mathematical objects (vectors, matrices)
   ✓ Domain-specific operators
   ✓ Resource management (files, connections)
   ✓ Custom string formatting
   
   JANGAN pakai jika:
   ✗ Membingungkan/tidak intuitif
   ✗ Built-in methods sudah cukup
   ✗ Over-engineering simple classes
""")
