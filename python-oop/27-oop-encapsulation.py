"""
OOP Part 2: Encapsulation & Property
=====================================
Encapsulation = Menyembunyikan data internal dan mengontrol akses
Property = Cara pythonic untuk getter/setter
"""

# ============================================
# 1. TANPA ENCAPSULATION (Public Attributes)
# ============================================


class RekeningBuruk:
    """Contoh BAD PRACTICE - semua attribute public"""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo


print("1. TANPA ENCAPSULATION - MASALAH")
print("-" * 50)
rekening = RekeningBuruk("John", 1000000)
print(f"Saldo awal: Rp{rekening.saldo:,}")

# MASALAH: Bisa diubah langsung tanpa validasi!
rekening.saldo = -5000000  # Ini tidak masuk akal!
print(f"Saldo setelah diubah sembarangan: Rp{rekening.saldo:,}")
print("❌ Masalah: Tidak ada kontrol, data bisa corrupted!")
print()


# ============================================
# 2. NAMING CONVENTION DI PYTHON
# ============================================

class ContohNaming:
    """
    Python naming convention untuk encapsulation:
    - public: nama_attribute
    - protected: _nama_attribute (convention, masih bisa diakses)
    - private: __nama_attribute (name mangling, lebih sulit diakses)
    """

    def __init__(self):
        self.public_var = "Bisa diakses dari mana saja"
        self._protected_var = "Convention: internal use, tapi masih bisa diakses"
        self.__private_var = "Name mangling: lebih sulit diakses"

    def tampilkan(self):
        print(f"Public: {self.public_var}")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")


print("2. NAMING CONVENTION")
print("-" * 50)
obj = ContohNaming()

# Akses public (normal)
print(f"✓ Akses public: {obj.public_var}")

# Akses protected (masih bisa, tapi convention: jangan!)
print(f"⚠ Akses protected: {obj._protected_var}")

# Akses private (akan error)
try:
    print(obj.__private_var)
except AttributeError as e:
    print(f"❌ Akses private langsung: {e}")

# Private bisa diakses dengan name mangling (tapi jangan!)
print(f"⚠ Akses private dengan mangling: {obj._ContohNaming__private_var}")
print()


# ============================================
# 3. ENCAPSULATION DENGAN GETTER/SETTER
# ============================================

class RekeningDenganMethod:
    """Encapsulation menggunakan getter/setter methods"""

    def __init__(self, pemilik, saldo_awal):
        self._pemilik = pemilik
        self._saldo = saldo_awal

    # GETTER methods
    def get_pemilik(self):
        return self._pemilik

    def get_saldo(self):
        return self._saldo

    # SETTER methods
    def set_saldo(self, saldo_baru):
        if saldo_baru < 0:
            print("❌ Error: Saldo tidak boleh negatif!")
            return False
        self._saldo = saldo_baru
        print(f"✓ Saldo berhasil diupdate: Rp{self._saldo:,}")
        return True

    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            return True
        return False

    def tarik(self, jumlah):
        if jumlah > self._saldo:
            print("❌ Saldo tidak cukup!")
            return False
        if jumlah > 0:
            self._saldo -= jumlah
            return True
        return False


print("3. ENCAPSULATION DENGAN GETTER/SETTER")
print("-" * 50)
rek = RekeningDenganMethod("Jane", 1000000)

# Akses dengan getter
print(f"Pemilik: {rek.get_pemilik()}")
print(f"Saldo: Rp{rek.get_saldo():,}")

# Update dengan setter (ada validasi)
rek.set_saldo(2000000)  # ✓ Valid
rek.set_saldo(-500000)  # ❌ Invalid

# Operasi dengan method
rek.setor(500000)
print(f"Saldo setelah setor: Rp{rek.get_saldo():,}")
print()


# ============================================
# 4. PROPERTY DECORATOR (CARA PYTHONIC)
# ============================================

class RekeningProperty:
    """Encapsulation menggunakan @property decorator (RECOMMENDED)"""

    def __init__(self, pemilik, saldo_awal):
        self._pemilik = pemilik
        self._saldo = saldo_awal
        self._transaksi = []

    # PROPERTY GETTER (read-only dari luar)
    @property
    def pemilik(self):
        """Getter untuk pemilik"""
        return self._pemilik

    @property
    def saldo(self):
        """Getter untuk saldo"""
        return self._saldo

    @property
    def total_transaksi(self):
        """Computed property - dihitung on-the-fly"""
        return len(self._transaksi)

    # PROPERTY SETTER
    @pemilik.setter
    def pemilik(self, nama_baru):
        """Setter untuk pemilik dengan validasi"""
        if not nama_baru or len(nama_baru.strip()) == 0:
            raise ValueError("Nama pemilik tidak boleh kosong!")
        self._pemilik = nama_baru

    # Methods untuk operasi
    def setor(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah setor harus positif!")
        self._saldo += jumlah
        self._transaksi.append(f"Setor: +Rp{jumlah:,}")
        return True

    def tarik(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah tarik harus positif!")
        if jumlah > self._saldo:
            raise ValueError("Saldo tidak cukup!")
        self._saldo -= jumlah
        self._transaksi.append(f"Tarik: -Rp{jumlah:,}")
        return True

    def riwayat_transaksi(self):
        """Menampilkan riwayat transaksi"""
        if not self._transaksi:
            print("Belum ada transaksi")
        else:
            print("Riwayat Transaksi:")
            for i, trans in enumerate(self._transaksi, 1):
                print(f"  {i}. {trans}")


print("4. PROPERTY DECORATOR (PYTHONIC WAY)")
print("-" * 50)
rek_prop = RekeningProperty("Alice", 1000000)

# Akses seperti attribute (bukan method!)
print(f"Pemilik: {rek_prop.pemilik}")  # Tidak perlu ()
print(f"Saldo: Rp{rek_prop.saldo:,}")
print()

# Operasi
rek_prop.setor(500000)
rek_prop.tarik(200000)
rek_prop.setor(1000000)
print(f"Saldo akhir: Rp{rek_prop.saldo:,}")
print(f"Total transaksi: {rek_prop.total_transaksi}")
print()
rek_prop.riwayat_transaksi()
print()

# Update pemilik (setter)
rek_prop.pemilik = "Alice Cooper"
print(f"Pemilik baru: {rek_prop.pemilik}")

# Validasi setter
try:
    rek_prop.pemilik = ""  # Invalid!
except ValueError as e:
    print(f"❌ Error: {e}")
print()


# ============================================
# 5. READ-ONLY PROPERTIES
# ============================================

class Person:
    """Class dengan read-only properties"""

    def __init__(self, nama_depan, nama_belakang, tahun_lahir):
        self._nama_depan = nama_depan
        self._nama_belakang = nama_belakang
        self._tahun_lahir = tahun_lahir

    @property
    def nama_lengkap(self):
        """Read-only: computed dari nama_depan dan nama_belakang"""
        return f"{self._nama_depan} {self._nama_belakang}"

    @property
    def umur(self):
        """Read-only: dihitung dari tahun lahir"""
        from datetime import datetime
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self._tahun_lahir

    @property
    def nama_depan(self):
        return self._nama_depan

    @nama_depan.setter
    def nama_depan(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        self._nama_depan = nama

    @property
    def nama_belakang(self):
        return self._nama_belakang

    @nama_belakang.setter
    def nama_belakang(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        self._nama_belakang = nama

    def info(self):
        print(f"Nama: {self.nama_lengkap}")
        print(f"Umur: {self.umur} tahun")


print("5. READ-ONLY PROPERTIES")
print("-" * 50)
person = Person("John", "Doe", 1990)
person.info()
print()

# Update nama depan dan belakang
person.nama_depan = "Jane"
person.nama_belakang = "Smith"
person.info()
print()

# nama_lengkap adalah READ-ONLY (tidak ada setter)
try:
    person.nama_lengkap = "Other Name"  # ❌ Akan error!
except AttributeError as e:
    print(f"❌ Error: {e}")
print()


# ============================================
# 6. PRAKTIK: PRODUCT INVENTORY SYSTEM
# ============================================

class Product:
    """Class Product dengan encapsulation penuh"""

    _id_counter = 1000  # Class attribute untuk auto-increment ID

    def __init__(self, nama, harga, stok=0):
        self._id = Product._id_counter
        Product._id_counter += 1

        self._nama = nama
        self._harga = harga
        self._stok = stok
        self._terjual = 0

    # Read-only properties
    @property
    def id(self):
        """Product ID (read-only)"""
        return self._id

    @property
    def terjual(self):
        """Total terjual (read-only)"""
        return self._terjual

    @property
    def revenue(self):
        """Total revenue (computed, read-only)"""
        return self._terjual * self._harga

    # Read-write properties
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama_baru):
        if not nama_baru or len(nama_baru.strip()) == 0:
            raise ValueError("Nama produk tidak boleh kosong!")
        self._nama = nama_baru

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            raise ValueError("Harga tidak boleh negatif!")
        self._harga = harga_baru

    @property
    def stok(self):
        return self._stok

    # Methods untuk operasi
    def tambah_stok(self, jumlah):
        """Menambah stok produk"""
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif!")
        self._stok += jumlah
        print(f"✓ Stok {self._nama} ditambah {jumlah} unit")

    def jual(self, jumlah):
        """Menjual produk"""
        if jumlah <= 0:
            raise ValueError("Jumlah harus positif!")
        if jumlah > self._stok:
            raise ValueError(f"Stok tidak cukup! Tersedia: {self._stok}")

        self._stok -= jumlah
        self._terjual += jumlah
        total = jumlah * self._harga
        print(f"✓ Terjual {jumlah} {self._nama} = Rp{total:,}")
        return total

    def info(self):
        """Menampilkan info produk"""
        print(f"ID: {self.id}")
        print(f"Nama: {self.nama}")
        print(f"Harga: Rp{self.harga:,}")
        print(f"Stok: {self.stok} unit")
        print(f"Terjual: {self.terjual} unit")
        print(f"Revenue: Rp{self.revenue:,}")

    def __str__(self):
        return f"{self.nama} (ID: {self.id}) - Rp{self.harga:,} | Stok: {self.stok}"


print("6. PRAKTIK: PRODUCT INVENTORY SYSTEM")
print("-" * 50)

# Membuat produk
laptop = Product("Laptop Gaming", 15000000, 10)
mouse = Product("Gaming Mouse", 500000, 50)

print("PRODUK 1:")
laptop.info()
print()

print("PRODUK 2:")
mouse.info()
print()

# Operasi
print("TRANSAKSI:")
laptop.tambah_stok(5)
laptop.jual(3)
mouse.jual(10)
print()

# Update harga
laptop.harga = 14000000
print(f"Harga laptop diupdate: Rp{laptop.harga:,}")
print()

# Info akhir
print("INFO AKHIR:")
print(laptop)
print(mouse)
print()


# ============================================
# 7. PROPERTY DELETER (Bonus)
# ============================================

class Cache:
    """Contoh penggunaan property deleter"""

    def __init__(self):
        self._data = {}

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, key_value):
        key, value = key_value
        self._data[key] = value
        print(f"✓ Data '{key}' disimpan")

    @data.deleter
    def data(self):
        """Clear all cached data"""
        count = len(self._data)
        self._data.clear()
        print(f"✓ {count} item cache dihapus")


print("7. PROPERTY DELETER")
print("-" * 50)
cache = Cache()

# Set data
cache.data = ("user1", {"name": "John", "age": 30})
cache.data = ("user2", {"name": "Jane", "age": 25})
print(f"Cache data: {cache.data}")

# Delete (clear cache)
del cache.data
print(f"Cache setelah dihapus: {cache.data}")
print()


# ============================================
# 8. SUMMARY
# ============================================

print("=" * 60)
print("SUMMARY - ENCAPSULATION & PROPERTY")
print("=" * 60)
print("""
1. ENCAPSULATION
   - Menyembunyikan internal data
   - Kontrol akses melalui methods/properties
   - Validasi data sebelum diubah

2. NAMING CONVENTION
   - public: nama_attribute (normal)
   - protected: _nama_attribute (convention: internal use)
   - private: __nama_attribute (name mangling)

3. PROPERTY DECORATOR (@property)
   ✓ Cara pythonic untuk getter/setter
   ✓ Akses seperti attribute, tapi dengan kontrol
   ✓ Bisa computed (dihitung on-the-fly)
   
   @property              → getter (read)
   @nama.setter           → setter (write)
   @nama.deleter          → deleter (delete)

4. READ-ONLY PROPERTY
   - Hanya buat @property (getter)
   - Jangan buat setter
   - Biasanya untuk computed values

5. BEST PRACTICES
   ✓ Gunakan @property untuk public interface
   ✓ Protected (_) untuk internal attributes
   ✓ Validasi input di setter
   ✓ Computed properties untuk derived values
   ✓ Keep methods simple and focused
   
6. KAPAN PAKAI PROPERTY?
   ✓ Ketika butuh validasi saat set value
   ✓ Ketika value computed dari data lain
   ✓ Ketika ingin backward compatibility
   ✓ Ketika ingin logging/tracking changes
   
   JANGAN pakai property untuk:
   ✗ Simple data container (gunakan dataclass)
   ✗ Heavy computation (gunakan method)
   ✗ Side effects yang kompleks (gunakan method)
""")
