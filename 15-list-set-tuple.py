# collection = single "variable" used to store multiple values
#       List = [] ordered and changeable. Duplicates OK
#       Set =  {} unordered and immutable, but Add/Remove OK. No Duplicates
#       Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# 1. LIST = []
#    → bisa diubah, boleh ada data yang sama, urutannya penting

print("=== LIST ===")
buah = ["apel", "pisang", "jeruk", "apel"]   # boleh duplikat

print(buah)                  # ['apel', 'pisang', 'jeruk', 'apel']
print(buah[1])               # pisang
buah[1] = "mangga"           # bisa diubah
buah.append("anggur")        # tambah di akhir
print(buah)                  # ['apel', 'mangga', 'jeruk', 'apel', 'anggur']


# 2. TUPLE = ()
#    → tidak bisa diubah (immutable), boleh duplikat, cepat

print("\n=== TUPLE ===")
warna = ("merah", "biru", "hijau", "merah")

print(warna)                 # ('merah', 'biru', 'hijau', 'merah')
print(warna[2])              # hijau

# warna[2] = "kuning"        # ERROR! → tidak bisa diubah
# warna.append("hitam")      # ERROR! → tidak punya append


# 3. SET = {}
#    → tidak berurutan, tidak boleh duplikat, bisa tambah/hapus

print("\n=== SET ===")
hewan = {"kucing", "anjing", "burung", "kucing"}   # duplikat hilang otomatis

print(hewan)                 # {'kucing', 'anjing', 'burung'}  (urutan acak)
# print(hewan[0])            # ERROR! → tidak punya index

hewan.add("ikan")            # bisa tambah
hewan.remove("burung")       # bisa hapus
print(hewan)                 # contoh: {'kucing', 'anjing', 'ikan'}
