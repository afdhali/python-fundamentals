import random

# =============================================
# KONFIGURASI (pakai tuple & dictionary)
# =============================================

PILIHAN = ("batu", "gunting", "kertas")           # Tuple → tidak bisa diubah

# Dictionary untuk menentukan siapa yang menang
# Key = (pemain, komputer) → Value = "pemain menang", "komputer menang", atau "seri"
HASIL = {
    ("batu", "gunting"): "pemain",
    ("gunting", "kertas"): "pemain",
    ("kertas", "batu"): "pemain",

    ("gunting", "batu"): "komputer",
    ("kertas", "gunting"): "komputer",
    ("batu", "kertas"): "komputer",

    # seri ditangani terpisah
}

SKOR = {"pemain": 0, "komputer": 0}   # Dictionary untuk simpan skor

# =============================================
# Fungsi bantu
# =============================================


def tampilkan_pilihan():
    print("\nPilihan:")
    for i, item in enumerate(PILIHAN, 1):
        print(f"{i}. {item.capitalize()}")


def dapatkan_pilihan_pemain():
    while True:
        tampilkan_pilihan()
        try:
            nomor = int(input("\nMasukkan nomor pilihanmu (1-3): "))
            if 1 <= nomor <= 3:
                return PILIHAN[nomor-1]
            else:
                print("Nomor harus antara 1 sampai 3!")
        except ValueError:
            print("Masukkan angka 1, 2, atau 3 saja!")

# =============================================
# PROGRAM UTAMA - pakai for loop untuk batas ronde
# =============================================


print("=====================================")
print("   BATU - GUNTING - KERTAS   v2.0   ")
print("=====================================\n")

nama = input("Masukkan namamu: ").strip()
if not nama:
    nama = "Pemain"

jumlah_ronde = 0
while True:
    try:
        jumlah_ronde = int(
            input(f"{nama}, mau main berapa ronde? (minimal 1, max 10): "))
        if 1 <= jumlah_ronde <= 10:
            break
        print("Masukkan angka antara 1 sampai 10!")
    except ValueError:
        print("Harus angka ya!")

print(f"\nOke {nama}! Kita main {jumlah_ronde} ronde. Siap-siap ya!\n")

# Main game dengan for loop
for ronde in range(1, jumlah_ronde + 1):
    print(f"\n=== Ronde {ronde} dari {jumlah_ronde} ===")

    # Pemain memilih
    pemain = dapatkan_pilihan_pemain()

    # Komputer memilih secara acak
    komputer = random.choice(PILIHAN)

    print(f"\nKamu pilih     : {pemain.upper()}")
    print(f"Komputer pilih : {komputer.upper()}")

    # Tentukan pemenang
    if pemain == komputer:
        print("→ SERI!")
    elif (pemain, komputer) in HASIL:
        pemenang = HASIL[(pemain, komputer)]
        if pemenang == "pemain":
            print("→ KAMU MENANG RONDE INI!")
            SKOR["pemain"] += 1
        else:
            print("→ KOMPUTER MENANG RONDE INI!")
            SKOR["komputer"] += 1
    else:
        # Seharusnya tidak masuk sini kalau logika benar
        print("Error logika?!")

    # Tampilkan skor sementara
    print(
        f"Skor saat ini → {nama}: {SKOR['pemain']}  |  Komputer: {SKOR['komputer']}")

# Hasil akhir
print("\n" + "="*40)
print("          HASIL AKHIR")
print("="*40)
print(f"{nama:<12}: {SKOR['pemain']} poin")
print(f"Komputer   : {SKOR['komputer']} poin")

if SKOR["pemain"] > SKOR["komputer"]:
    print(f"\nSELAMAT {nama.upper()}! KAMU JUARA!")
elif SKOR["pemain"] < SKOR["komputer"]:
    print("\nKomputer menang. Coba lagi ya!")
else:
    print("\nSeri! Kalian seimbang banget!")
