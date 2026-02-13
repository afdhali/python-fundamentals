# dictionary = a collection of {key:value} pairs
#       ordered and changeable. No Duplicates
# Ciri                 Set {}                                           Dictionary {key: value}
# Bentuk penulisan     "{""apel"", ""pisang""}"                         "{""nama"": ""Budi"", ""umur"": 17}"
# Isi                  Hanya value (tanpa key)                          Pasangan key dan value
# Boleh duplikat?      Tidak (otomatis hilang)                          "Key tidak boleh duplikat, value boleh"
# Ada urutan?          Tidak (unordered)                                Ya (ordered sejak Python 3.7+)
# Bisa diakses index?  Tidak                                            "Tidak (pakai key, bukan index)"
# Bisa diubah?         Bisa tambah/hapus elemen                         "Bisa ubah value, tambah/hapus key-value"
# Kegunaan utama       "Menyimpan data unik, cek keberadaan cepat"      Menyimpan data berpasangan (label + nilai)
# Contoh nyata         "Daftar ID unik, tag unik"                       "Data profil, setting, JSON"


print("=== DICTIONARY ===")

# Contoh sederhana
siswa = {
    "nama": "Budi",
    "umur": 17,
    "kelas": "XII IPA 1",
    "nilai": [85, 90, 78],
    "lulus": True
}

# Cara akses
print(siswa["nama"])          # Budi
print(siswa["nilai"])         # [85, 90, 78]
print(siswa["nilai"][1])      # 90

# Ubah value
siswa["umur"] = 18
siswa["alamat"] = "Jakarta"   # tambah key baru

# Hapus key
del siswa["lulus"]

print(siswa)
# Output contoh:
# {'nama': 'Budi', 'umur': 18, 'kelas': 'XII IPA 1', 'nilai': [85, 90, 78], 'alamat': 'Jakarta'}


# looping
for key, value in siswa.items():
    print(f"{key:8} : {value}")
