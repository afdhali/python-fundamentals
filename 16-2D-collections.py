# 2D LISTS

# Contoh sederhana: tabel nilai siswa (3 siswa × 3 mata pelajaran)

nilai = [
    [80, 85, 90],     # siswa 1: Matematika, IPA, Bahasa
    [75, 70, 95],     # siswa 2
    [60, 82, 78]      # siswa 3
]

print("=== 2D List ===")
print(nilai)                    # [[80,85,90], [75,70,95], [60,82,78]]

# Akses elemen: baris ke-0, kolom ke-1
print(nilai[0][1])              # 85 (nilai IPA siswa 1)

# Ubah nilai
nilai[2][0] = 88                # ubah nilai Matematika siswa 3 jadi 88
print(nilai[2])                 # [88, 82, 78]

# Tambah baris baru (siswa baru)
nilai.append([92, 88, 85])
print("Setelah tambah siswa baru:", nilai)

# Cetak rapi seperti tabel
print("\nTabel nilai:")
for baris in nilai:
    print(baris)

# Mengisi 2D list kosong
# Cara BENAR (jangan pakai yang salah!)
baris = 3
kolom = 4

# Cara 1 (paling aman & mudah dipahami)
matriks = [[0 for _ in range(kolom)] for _ in range(baris)]
# atau
matriks = []
for i in range(baris):
    baris_baru = [0] * kolom
    matriks.append(baris_baru)

print(matriks)          # [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# ======================================================================

# 2D Tuple
# Contoh: koordinat titik di peta (tidak boleh diubah)

koordinat = (
    (3, 5),     # titik A
    (1, 8),     # titik B
    (7, 2)      # titik C
)

print("=== 2D Tuple ===")
print(koordinat)            # ((3,5), (1,8), (7,2))
print(koordinat[1][0])      # 1  (x dari titik B)

# koordinat[1][0] = 10      # ERROR! Tuple tidak bisa diubah
