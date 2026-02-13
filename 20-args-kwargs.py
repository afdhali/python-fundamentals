# Nama     Ditulis di def           Dikumpulkan jadi                    Bisa dipakai untuk                  Contoh pemanggilan
# *args    *args                    tuple                               banyak argumen posisional           "func(1, 2, 3, 4)"
# **kwargs **kwargs                 dictionary                          banyak argumen keyword              "func(a=10, b=""hai"", c=True)"
# Biasa    "x, y, z"                variabel terpisah                   argumen wajib / jumlah pasti        "func(5, ""halo"", True)"

# ==================== *args ========================================
def jumlahkan_semua(*args):
    print(args)           # tuple
    print(type(args))     # <class 'tuple'>

    total = 0
    for angka in args:
        total += angka
    return total


# Cara panggil
print(jumlahkan_semua(5, 10))              # 15
print(jumlahkan_semua(1, 2, 3, 4, 5))      # 15
print(jumlahkan_semua(10))                 # 10
print(jumlahkan_semua())                   # 0  (args jadi tuple kosong)


# ================== **kwargs ======================================
def tampilkan_profil(**kwargs):
    print(kwargs)              # dictionary
    print(type(kwargs))        # <class 'dict'>

    for key, value in kwargs.items():
        print(f"{key:10} : {value}")


# Cara panggil
tampilkan_profil(nama="Afdhali", umur=20, kota="Jakarta")
# Output:
# {'nama': 'Afdhali', 'umur': 20, 'kota': 'Jakarta'}
# nama       : Afdhali
# umur       : 20
# kota       : Jakarta

tampilkan_profil(nama="Budi", hobi="gaming", makanan_favorit="nasi goreng")


# ================= *args & **kwargs ==================================
def pesan_makanan(nama_pemesan, *makanan, **info_tambahan):
    print(f"Pemesan     : {nama_pemesan}")
    print("Pesanan     :", ", ".join(makanan))

    if info_tambahan:
        print("Info tambahan:")
        for k, v in info_tambahan.items():
            print(f"  {k:12} : {v}")


pesan_makanan("Afdhali", "nasi goreng", "es teh", "sate",
              alamat="Jakarta Selatan", catatan="pedas sedang")
# Output:
# Pemesan     : Afdhali
# Pesanan     : nasi goreng, es teh, sate
# Info tambahan:
#   alamat       : Jakarta Selatan
#   catatan      : pedas sedang

#  ================= Unpacking ==========================================


def tambah(a, b, c):
    return a + b + c


# -------------------------------
# Tanpa unpacking
print(tambah(10, 20, 30))          # 60

# Dengan unpacking (*)
angka = [10, 20, 30]
# 60   ← * mengeluarkan isi list jadi argumen terpisah
print(tambah(*angka))

# -------------------------------
angka2 = (5, 15, 25)
print(tambah(*angka2))             # 45

# -------------------------------
# Bisa juga sebagian saja


def cetak_nama_depan_belakang(depan, tengah, belakang):
    print(depan, tengah, belakang)


orang = ["Budi", "Santoso", "Pratama"]
cetak_nama_depan_belakang(*orang)          # Budi Santoso Pratama


def gambar_lingkaran(x, y, radius, warna="merah", tebal=2):
    print(f"Lingkaran di ({x},{y}), r={radius}, warna={warna}, tebal={tebal}")


setting = {
    "warna": "biru",
    "tebal": 5
}

# Default + override beberapa saja
gambar_lingkaran(100, 200, 50, **setting)
# → Lingkaran di (100,200), r=50, warna=biru, tebal=5


def pesan(nama, *makanan, **info):
    print(f"Pemesan: {nama}")
    print("Makanan :", ", ".join(makanan))
    if info:
        print("Info   :", info)


daftar_makanan = ["nasi goreng", "es teh", "sate"]
info_tambahan = {"meja": 7, "catatan": "pedas sedang"}

pesan("Afdhali", *daftar_makanan, **info_tambahan)
# Output:
# Pemesan: Afdhali
# Makanan : nasi goreng, es teh, sate
# Info   : {'meja': 7, 'catatan': 'pedas sedang'}
