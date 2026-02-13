"""
OOP Part 3: Inheritance (Pewarisan)
====================================
Inheritance = Class anak mewarisi properties dan methods dari class parent
Tujuan: Code reuse, hierarchical relationships, polymorphism
"""

# ============================================
# 1. BASIC INHERITANCE
# ============================================

from abc import ABC, abstractmethod


class Hewan:
    """Parent class (Base class / Super class)"""

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def suara(self):
        return "Hewan bersuara"

    def info(self):
        return f"{self.nama} berumur {self.umur} tahun"


class Kucing(Hewan):
    """Child class (Derived class / Sub class)"""
    # Mewarisi semua attributes dan methods dari Hewan
    pass


class Anjing(Hewan):
    """Child class"""
    pass


print("1. BASIC INHERITANCE")
print("-" * 50)

kucing = Kucing("Kitty", 2)
anjing = Anjing("Buddy", 3)

print(f"Kucing: {kucing.info()}")  # Method dari parent
print(f"Anjing: {anjing.info()}")  # Method dari parent
print()

# Cek inheritance
print(f"Apakah kucing instance dari Kucing? {isinstance(kucing, Kucing)}")
print(f"Apakah kucing instance dari Hewan? {isinstance(kucing, Hewan)}")
print(f"Apakah Kucing subclass dari Hewan? {issubclass(Kucing, Hewan)}")
print()


# ============================================
# 2. METHOD OVERRIDING
# ============================================

class Burung(Hewan):
    """Child class dengan method overriding"""

    def suara(self):
        """Override method dari parent"""
        return "Cuit cuit cuit!"

    def terbang(self):
        """Method baru yang tidak ada di parent"""
        return f"{self.nama} sedang terbang"


class Ikan(Hewan):
    """Child class dengan method overriding"""

    def suara(self):
        """Override - ikan tidak bersuara"""
        return "..."

    def berenang(self):
        """Method baru"""
        return f"{self.nama} sedang berenang"


print("2. METHOD OVERRIDING")
print("-" * 50)

burung = Burung("Tweety", 1)
ikan = Ikan("Nemo", 1)

print(f"Suara burung: {burung.suara()}")  # Overridden method
print(f"Burung: {burung.terbang()}")       # New method
print()
print(f"Suara ikan: {ikan.suara()}")      # Overridden method
print(f"Ikan: {ikan.berenang()}")         # New method
print()


# ============================================
# 3. SUPER() - MEMANGGIL METHOD PARENT
# ============================================

class Karyawan:
    """Parent class"""

    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan
        print(f"✓ Karyawan.__init__ dipanggil untuk {nama}")

    def info(self):
        return f"ID: {self.id_karyawan}, Nama: {self.nama}"

    def gaji_pokok(self):
        return 5000000


class Manager(Karyawan):
    """Child class dengan additional attributes"""

    def __init__(self, nama, id_karyawan, departemen):
        # Panggil constructor parent dengan super()
        super().__init__(nama, id_karyawan)
        self.departemen = departemen
        print(f"✓ Manager.__init__ dipanggil untuk departemen {departemen}")

    def info(self):
        # Panggil method parent dan tambahkan info
        parent_info = super().info()
        return f"{parent_info}, Departemen: {self.departemen}"

    def gaji_total(self):
        # Gaji pokok + tunjangan
        pokok = super().gaji_pokok()
        tunjangan = 3000000
        return pokok + tunjangan


print("3. SUPER() - MEMANGGIL METHOD PARENT")
print("-" * 50)

manager = Manager("John Doe", "MGR001", "IT")
print()
print(manager.info())
print(f"Gaji total: Rp{manager.gaji_total():,}")
print()


# ============================================
# 4. MULTIPLE INHERITANCE
# ============================================

class Terbang:
    """Mixin class untuk kemampuan terbang"""

    def terbang(self):
        return f"{self.nama} sedang terbang"

    def mendarat(self):
        return f"{self.nama} mendarat"


class Berenang:
    """Mixin class untuk kemampuan berenang"""

    def berenang(self):
        return f"{self.nama} sedang berenang"

    def menyelam(self):
        return f"{self.nama} menyelam"


class Bebek(Hewan, Terbang, Berenang):
    """Multiple inheritance - bebek bisa terbang dan berenang"""

    def __init__(self, nama, umur):
        super().__init__(nama, umur)

    def suara(self):
        return "Kwek kwek!"


class Pinguin(Hewan, Berenang):
    """Pinguin bisa berenang tapi tidak bisa terbang"""

    def suara(self):
        return "Honk honk!"


print("4. MULTIPLE INHERITANCE")
print("-" * 50)

bebek = Bebek("Donald", 2)
pinguin = Pinguin("Pingu", 3)

print(f"Bebek: {bebek.suara()}")
print(f"- {bebek.terbang()}")
print(f"- {bebek.berenang()}")
print()

print(f"Pinguin: {pinguin.suara()}")
print(f"- {pinguin.berenang()}")
print(f"- {pinguin.menyelam()}")
# pinguin.terbang()  # ❌ Error - tidak punya method ini
print()

# MRO (Method Resolution Order)
print("MRO Bebek:", Bebek.__mro__)
print()


# ============================================
# 5. ABSTRACT BASE CLASS (ABC)
# ============================================


class Shape(ABC):
    """Abstract base class - tidak bisa diinstansiasi"""

    def __init__(self, warna):
        self.warna = warna

    @abstractmethod
    def luas(self):
        """Method abstract - HARUS diimplementasi di child class"""
        pass

    @abstractmethod
    def keliling(self):
        """Method abstract"""
        pass

    def info(self):
        """Concrete method - bisa langsung dipakai"""
        return f"Shape berwarna {self.warna}"


class Persegi(Shape):
    """Concrete class - implement semua abstract methods"""

    def __init__(self, warna, sisi):
        super().__init__(warna)
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi


class Lingkaran(Shape):
    """Concrete class"""

    def __init__(self, warna, radius):
        super().__init__(warna)
        self.radius = radius

    def luas(self):
        return 3.14159 * self.radius ** 2

    def keliling(self):
        return 2 * 3.14159 * self.radius


print("5. ABSTRACT BASE CLASS (ABC)")
print("-" * 50)

# shape = Shape("merah")  # ❌ Error - tidak bisa instantiate abstract class

persegi = Persegi("biru", 5)
lingkaran = Lingkaran("merah", 7)

print(f"Persegi: {persegi.info()}")
print(f"- Luas: {persegi.luas()}")
print(f"- Keliling: {persegi.keliling()}")
print()

print(f"Lingkaran: {lingkaran.info()}")
print(f"- Luas: {lingkaran.luas():.2f}")
print(f"- Keliling: {lingkaran.keliling():.2f}")
print()


# ============================================
# 6. PRAKTIK: EMPLOYEE MANAGEMENT SYSTEM
# ============================================

class Employee(ABC):
    """Abstract base class untuk semua karyawan"""

    employee_count = 0

    def __init__(self, nama, id_karyawan, departemen):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.departemen = departemen
        Employee.employee_count += 1

    @abstractmethod
    def hitung_gaji(self):
        """Setiap tipe karyawan hitung gaji berbeda"""
        pass

    @abstractmethod
    def tipe_karyawan(self):
        """Return tipe karyawan"""
        pass

    def info(self):
        """Info umum karyawan"""
        return f"""
Nama: {self.nama}
ID: {self.id_karyawan}
Departemen: {self.departemen}
Tipe: {self.tipe_karyawan()}
Gaji: Rp{self.hitung_gaji():,}
        """.strip()


class FullTimeEmployee(Employee):
    """Karyawan tetap dengan gaji bulanan"""

    def __init__(self, nama, id_karyawan, departemen, gaji_bulanan):
        super().__init__(nama, id_karyawan, departemen)
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        return self.gaji_bulanan

    def tipe_karyawan(self):
        return "Full-time"


class PartTimeEmployee(Employee):
    """Karyawan paruh waktu - gaji per jam"""

    def __init__(self, nama, id_karyawan, departemen, tarif_per_jam):
        super().__init__(nama, id_karyawan, departemen)
        self.tarif_per_jam = tarif_per_jam
        self.jam_kerja = 0

    def catat_jam_kerja(self, jam):
        """Catat jam kerja"""
        self.jam_kerja += jam
        print(f"✓ {jam} jam kerja dicatat untuk {self.nama}")

    def hitung_gaji(self):
        return self.tarif_per_jam * self.jam_kerja

    def tipe_karyawan(self):
        return "Part-time"

    def reset_jam_kerja(self):
        """Reset jam kerja (biasanya tiap bulan)"""
        self.jam_kerja = 0


class ManagerEmployee(FullTimeEmployee):
    """Manager - inherit dari FullTimeEmployee dengan bonus"""

    def __init__(self, nama, id_karyawan, departemen, gaji_bulanan, jumlah_bawahan):
        super().__init__(nama, id_karyawan, departemen, gaji_bulanan)
        self.jumlah_bawahan = jumlah_bawahan

    def hitung_bonus(self):
        """Bonus berdasarkan jumlah bawahan"""
        return self.jumlah_bawahan * 500000

    def hitung_gaji(self):
        """Override - gaji + bonus"""
        gaji_pokok = super().hitung_gaji()
        bonus = self.hitung_bonus()
        return gaji_pokok + bonus

    def tipe_karyawan(self):
        return f"Manager ({self.jumlah_bawahan} bawahan)"


class Freelancer(Employee):
    """Freelancer - gaji per project"""

    def __init__(self, nama, id_karyawan, departemen):
        super().__init__(nama, id_karyawan, departemen)
        self.projects_completed = []

    def tambah_project(self, nama_project, bayaran):
        """Tambah project yang selesai"""
        self.projects_completed.append({
            'nama': nama_project,
            'bayaran': bayaran
        })
        print(f"✓ Project '{nama_project}' selesai, bayaran: Rp{bayaran:,}")

    def hitung_gaji(self):
        """Total dari semua project"""
        return sum(p['bayaran'] for p in self.projects_completed)

    def tipe_karyawan(self):
        return f"Freelancer ({len(self.projects_completed)} projects)"


print("6. PRAKTIK: EMPLOYEE MANAGEMENT SYSTEM")
print("-" * 50)

# Buat berbagai tipe karyawan
emp1 = FullTimeEmployee("Alice", "FT001", "Engineering", 8000000)
emp2 = PartTimeEmployee("Bob", "PT001", "Support", 50000)
emp3 = ManagerEmployee("Charlie", "MG001", "Engineering", 12000000, 5)
emp4 = Freelancer("Diana", "FL001", "Design")

# Operasi
emp2.catat_jam_kerja(120)  # 120 jam kerja
emp4.tambah_project("Website Redesign", 15000000)
emp4.tambah_project("Mobile App UI", 10000000)
print()

# Tampilkan info semua karyawan
karyawans = [emp1, emp2, emp3, emp4]
for i, emp in enumerate(karyawans, 1):
    print(f"KARYAWAN {i}:")
    print(emp.info())
    print()

print(f"Total karyawan: {Employee.employee_count}")
print()


# ============================================
# 7. POLYMORPHISM DENGAN INHERITANCE
# ============================================

def proses_gaji(employees):
    """Polymorphism - method yang sama, behavior berbeda"""
    print("PROSES GAJI BULANAN")
    print("=" * 50)

    total = 0
    for emp in employees:
        gaji = emp.hitung_gaji()
        total += gaji
        print(f"{emp.nama:15} ({emp.tipe_karyawan():20}): Rp{gaji:>12,}")

    print("=" * 50)
    print(f"{'TOTAL':38}: Rp{total:>12,}")


print("7. POLYMORPHISM")
print("-" * 50)
proses_gaji(karyawans)
print()


# ============================================
# 8. COMPOSITION vs INHERITANCE
# ============================================

# INHERITANCE - "is-a" relationship
class Car:
    def __init__(self, merk):
        self.merk = merk

    def drive(self):
        return f"{self.merk} is driving"


class ElectricCar(Car):  # ElectricCar IS-A Car
    def charge(self):
        return f"{self.merk} is charging"

# COMPOSITION - "has-a" relationship


class Engine:
    def __init__(self, tipe):
        self.tipe = tipe

    def start(self):
        return f"{self.tipe} engine started"


class CarWithComposition:  # Car HAS-A Engine
    def __init__(self, merk, engine_type):
        self.merk = merk
        self.engine = Engine(engine_type)  # Composition

    def start(self):
        return self.engine.start()


print("8. COMPOSITION vs INHERITANCE")
print("-" * 50)

# Inheritance
tesla = ElectricCar("Tesla")
print(f"Inheritance: {tesla.drive()}")
print(f"            {tesla.charge()}")
print()

# Composition
bmw = CarWithComposition("BMW", "V8")
print(f"Composition: {bmw.start()}")
print()


# ============================================
# 9. SUMMARY
# ============================================

print("=" * 60)
print("SUMMARY - INHERITANCE")
print("=" * 60)
print("""
1. INHERITANCE BASICS
   - Child class mewarisi attributes & methods dari parent
   - Syntax: class Child(Parent):
   - isinstance() - cek instance
   - issubclass() - cek subclass

2. METHOD OVERRIDING
   - Child class bisa override method parent
   - Untuk customize behavior
   - Gunakan super() untuk memanggil parent method

3. SUPER()
   - Memanggil method dari parent class
   - Penting di __init__ untuk multiple inheritance
   - super().method_name() untuk method lain

4. MULTIPLE INHERITANCE
   - class Child(Parent1, Parent2, Parent3):
   - Warisi dari beberapa parent
   - MRO (Method Resolution Order) - urutan pencarian method
   - Hati-hati dengan diamond problem

5. ABSTRACT BASE CLASS (ABC)
   - Class yang tidak bisa diinstansiasi langsung
   - Gunakan @abstractmethod untuk force implementation
   - Template untuk child classes
   
6. POLYMORPHISM
   - Same interface, different implementation
   - Method sama, behavior berbeda
   - Duck typing: "If it walks like a duck..."

7. COMPOSITION vs INHERITANCE
   - Inheritance: "is-a" relationship (Dog IS-A Animal)
   - Composition: "has-a" relationship (Car HAS-A Engine)
   - Prefer composition over inheritance (lebih flexible)

8. BEST PRACTICES
   ✓ Single responsibility per class
   ✓ Inheritance untuk "is-a" relationship
   ✓ Composition untuk "has-a" relationship
   ✓ Gunakan ABC untuk interface contracts
   ✓ Keep inheritance hierarchy shallow (max 2-3 levels)
   ✓ Favor composition over deep inheritance
   
9. KAPAN PAKAI INHERITANCE?
   ✓ Clear "is-a" relationship
   ✓ Share behavior across related classes
   ✓ Polymorphic behavior needed
   ✓ Code reuse with modification
   
   JANGAN pakai inheritance untuk:
   ✗ Code reuse saja (gunakan composition)
   ✗ No clear "is-a" relationship
   ✗ Deep hierarchy (>3 levels)
""")
