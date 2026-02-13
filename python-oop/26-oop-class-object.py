"""
OOP Part 1: Class dan Object
=============================
Class adalah blueprint/template untuk membuat object
Object adalah instance dari class
"""

# ============================================
# 1. MEMBUAT CLASS SEDERHANA
# ============================================


class Mobil:
    """Class sederhana untuk merepresentasikan mobil"""
    pass  # Class kosong


# Membuat object dari class Mobil
mobil1 = Mobil()
mobil2 = Mobil()

print("1. MEMBUAT OBJECT")
print(f"mobil1 adalah object dari class: {type(mobil1)}")
print(f"mobil2 adalah object dari class: {type(mobil2)}")
print(f"Apakah mobil1 dan mobil2 object yang sama? {mobil1 is mobil2}")
print()


# ============================================
# 2. CLASS DENGAN ATTRIBUTES (Properties)
# ============================================

class Siswa:
    """Class dengan attributes"""

    # Ini namanya instance attribute (dibuat saat object dibuat)
    def __init__(self, nama, umur, kelas):
        """
        Constructor: Method khusus yang dipanggil saat object dibuat
        self = referensi ke object itu sendiri
        """
        self.nama = nama      # Instance attribute
        self.umur = umur      # Instance attribute
        self.kelas = kelas    # Instance attribute


# Membuat object siswa
siswa1 = Siswa("Budi", 16, "10A")
siswa2 = Siswa("Ani", 17, "11B")

print("2. ATTRIBUTES (Properties)")
print(f"Nama siswa1: {siswa1.nama}")
print(f"Umur siswa1: {siswa1.umur}")
print(f"Kelas siswa1: {siswa1.kelas}")
print()
print(f"Nama siswa2: {siswa2.nama}")
print(f"Umur siswa2: {siswa2.umur}")
print(f"Kelas siswa2: {siswa2.kelas}")
print()


# ============================================
# 3. CLASS DENGAN METHODS (Functions)
# ============================================

class BankAccount:
    """Class dengan methods untuk operasi"""

    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.saldo = saldo_awal

    def setor(self, jumlah):
        """Method untuk menyetor uang"""
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setor: Rp{jumlah:,}")
            print(f"Saldo baru: Rp{self.saldo:,}")
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        """Method untuk menarik uang"""
        if jumlah > self.saldo:
            print(f"Saldo tidak cukup! Saldo Anda: Rp{self.saldo:,}")
        elif jumlah > 0:
            self.saldo -= jumlah
            print(f"Tarik: Rp{jumlah:,}")
            print(f"Saldo baru: Rp{self.saldo:,}")
        else:
            print("Jumlah tarik harus positif!")

    def cek_saldo(self):
        """Method untuk mengecek saldo"""
        print(f"Saldo {self.pemilik}: Rp{self.saldo:,}")
        return self.saldo


print("3. METHODS (Functions dalam Class)")
rekening = BankAccount("John Doe", 1000000)
rekening.cek_saldo()
rekening.setor(500000)
rekening.tarik(300000)
rekening.tarik(2000000)  # Gagal karena saldo tidak cukup
print()


# ============================================
# 4. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ============================================

class Karyawan:
    """Class dengan class attribute dan instance attribute"""

    # CLASS ATTRIBUTE (shared oleh semua instance)
    perusahaan = "PT. Maju Jaya"
    jumlah_karyawan = 0

    def __init__(self, nama, posisi, gaji):
        # INSTANCE ATTRIBUTE (unique untuk setiap instance)
        self.nama = nama
        self.posisi = posisi
        self.gaji = gaji

        # Increment class attribute
        Karyawan.jumlah_karyawan += 1

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Posisi: {self.posisi}")
        print(f"Gaji: Rp{self.gaji:,}")
        print(f"Perusahaan: {Karyawan.perusahaan}")


print("4. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES")
print(f"Jumlah karyawan awal: {Karyawan.jumlah_karyawan}")

karyawan1 = Karyawan("Alice", "Developer", 8000000)
karyawan2 = Karyawan("Bob", "Designer", 7000000)

print(f"Jumlah karyawan setelah hire: {Karyawan.jumlah_karyawan}")
print()

karyawan1.info()
print()
karyawan2.info()
print()

# Class attribute bisa diakses dari class atau instance
print(f"Perusahaan (dari class): {Karyawan.perusahaan}")
print(f"Perusahaan (dari instance): {karyawan1.perusahaan}")
print()


# ============================================
# 5. __str__ dan __repr__ METHODS
# ============================================

class Buku:
    """Class dengan string representation methods"""

    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        """String representation untuk user (human-readable)"""
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"

    def __repr__(self):
        """String representation untuk developer (debugging)"""
        return f"Buku('{self.judul}', '{self.penulis}', {self.tahun})"


print("5. __str__ dan __repr__ METHODS")
buku1 = Buku("Python 101", "Guido van Rossum", 2020)

print(f"str(buku1): {str(buku1)}")      # Memanggil __str__
print(f"repr(buku1): {repr(buku1)}")    # Memanggil __repr__
print(f"print(buku1): {buku1}")         # Default ke __str__ jika ada
print()


# ============================================
# 6. PRAKTIK: MEMBUAT CLASS LENGKAP
# ============================================

class Mahasiswa:
    """Class Mahasiswa dengan berbagai fitur"""

    # Class attribute
    universitas = "Universitas Indonesia"
    total_mahasiswa = 0

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
        self.mata_kuliah = []

        # Update class attribute
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        """Menambah mata kuliah"""
        self.mata_kuliah.append(matkul)
        print(f"Mata kuliah '{matkul}' ditambahkan untuk {self.nama}")

    def update_ipk(self, ipk_baru):
        """Update IPK mahasiswa"""
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            print(f"IPK {self.nama} diupdate menjadi {self.ipk}")
        else:
            print("IPK harus antara 0.0 - 4.0")

    def status_kelulusan(self):
        """Cek status kelulusan berdasarkan IPK"""
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.75:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Lulus"

    def info_lengkap(self):
        """Menampilkan info lengkap mahasiswa"""
        print("=" * 50)
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Universitas: {Mahasiswa.universitas}")
        print(f"IPK: {self.ipk}")
        print(f"Status: {self.status_kelulusan()}")
        if self.mata_kuliah:
            print(f"Mata Kuliah: {', '.join(self.mata_kuliah)}")
        print("=" * 50)

    def __str__(self):
        return f"{self.nama} ({self.nim}) - {self.jurusan}"

    def __repr__(self):
        return f"Mahasiswa('{self.nama}', '{self.nim}', '{self.jurusan}', {self.ipk})"


print("6. PRAKTIK LENGKAP")
print(f"Total mahasiswa awal: {Mahasiswa.total_mahasiswa}")
print()

# Membuat mahasiswa
mhs1 = Mahasiswa("Dewi Sartika", "2101001", "Teknik Informatika")
mhs2 = Mahasiswa("Ahmad Dahlan", "2101002", "Sistem Informasi", 3.75)

# Operasi pada mahasiswa 1
mhs1.tambah_matkul("Pemrograman Python")
mhs1.tambah_matkul("Struktur Data")
mhs1.update_ipk(3.85)
print()

# Operasi pada mahasiswa 2
mhs2.tambah_matkul("Database")
mhs2.tambah_matkul("Jaringan Komputer")
print()

# Tampilkan info
mhs1.info_lengkap()
print()
mhs2.info_lengkap()
print()

print(f"Total mahasiswa akhir: {Mahasiswa.total_mahasiswa}")
print()


# ============================================
# 7. SUMMARY & BEST PRACTICES
# ============================================

print("=" * 60)
print("SUMMARY - KONSEP DASAR OOP")
print("=" * 60)
print("""
1. CLASS = Blueprint/Template untuk membuat object
   - Didefinisikan dengan keyword 'class'
   - Nama class menggunakan PascalCase (ContohNamaClass)

2. OBJECT = Instance dari class
   - Dibuat dengan memanggil class seperti function
   - Setiap object adalah entitas terpisah di memory

3. __init__ = Constructor
   - Method khusus yang dipanggil saat object dibuat
   - Digunakan untuk inisialisasi attributes
   - Parameter pertama selalu 'self'

4. self = Referensi ke object itu sendiri
   - Digunakan untuk mengakses attributes dan methods
   - Harus jadi parameter pertama di semua instance methods

5. ATTRIBUTES = Variables dalam class
   - Instance attributes: unique untuk setiap object
   - Class attributes: shared oleh semua object

6. METHODS = Functions dalam class
   - Operasi yang bisa dilakukan oleh object
   - Parameter pertama selalu 'self'

7. SPECIAL METHODS (dunder methods)
   - __init__: Constructor
   - __str__: String representation untuk user
   - __repr__: String representation untuk developer

BEST PRACTICES:
✓ Nama class: PascalCase (Mobil, BankAccount)
✓ Nama method/attribute: snake_case (cek_saldo, nama_lengkap)
✓ Gunakan docstring untuk dokumentasi
✓ Encapsulate data yang related dalam satu class
✓ Method yang mengubah state gunakan verb (update, add, remove)
✓ Method yang return info gunakan noun (status, info, total)
""")
