# Kebutuhan                         def (fungsi biasa)                          lambda
# Bisa lebih dari 1 baris?          Ya                                          Tidak (hanya 1 expression)
# Punya nama?                       Ya                                          Tidak (anonymous)
# Bisa punya docstring?             Ya                                          Tidak
# Bisa dipakai rekursif?            Ya                                          Sangat sulit / tidak praktis
# Cocok untuk fungsi sekali pakai?  Kurang efisien                              Sangat cocok
# Contoh penggunaan umum            "Fungsi utama, logika kompleks"             "key di sorted, map, filter, dll"

def hitung(a, b, c): return a * b + c


print(hitung(2, 3, 10))   # 16   →  2×3 + 10

angka = [10, 3, 7, 12, 5, 8, 9]

ganjil = list(filter(lambda x: x % 2 == 1, angka))
print(ganjil)             # [3, 7, 5, 9]


# 1. Ambil elemen tertentu dari tuple/list
data = [("Budi", 17), ("Ani", 20), ("Citra", 15)]
urut_umur = sorted(data, key=lambda x: x[1])          # urut berdasarkan umur
# → [('Citra', 15), ('Budi', 17), ('Ani', 20)]

# 2. Sort descending
urut_umur_desc = sorted(data, key=lambda x: x[1], reverse=True)

# 3. Kondisi sederhana (if else dalam lambda)


def status(umur): return "Dewasa" if umur >= 17 else "Anak-anak"


print(status(16))     # Anak-anak
