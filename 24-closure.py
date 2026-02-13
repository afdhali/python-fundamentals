def buat_counter(nama):
    count = 0           # variabel ini "tertutup" di closure

    def tambah():
        nonlocal count
        count += 1
        print(f"{nama}: {count}")
        return count

    def reset():
        nonlocal count
        count = 0
        print(f"{nama} di-reset → {count}")

    def lihat():
        print(f"Nilai saat ini {nama}: {count}")

    # Mengembalikan dictionary berisi fungsi-fungsi
    return {
        'tambah': tambah,
        'reset': reset,
        'lihat': lihat,
        'nilai': lambda: count   # cara baca tanpa print
    }


# Penggunaan
hitung_A = buat_counter("A")
hitung_B = buat_counter("B")

hitung_A['tambah']()      # A: 1
hitung_A['tambah']()      # A: 2
hitung_B['tambah']()      # B: 1
hitung_A['tambah']()      # A: 3
hitung_B['lihat']()       # Nilai saat ini B: 1

hitung_A['reset']()       # A di-reset → 0
hitung_A['tambah']()      # A: 1

# Buktikan counter terpisah
print(hitung_A['nilai']())   # 1
print(hitung_B['nilai']())   # 1
