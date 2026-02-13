# Bagian nama - pakai for loop dengan batas percobaan
for attempt in range(1, 6):  # maksimal 5 kali coba
    name = input("Enter your name: ").strip()

    if name:  # kalau ada isi (bukan kosong/spasi doang)
        break

    print(f"[{attempt}/5] Nama tidak boleh kosong ya... coba lagi.")
else:
    # kalau sudah 5 kali masih kosong
    print("Sudah 5 kali coba, nama tetap kosong. Program berhenti.")
    exit()  # atau bisa diganti pass kalau ga mau keluar

print(f"Hello {name}!")

# Bagian umur - pakai for loop juga
for attempt in range(1, 6):  # maksimal 5 percobaan
    try:
        age_input = input("Enter your age: ").strip()
        age = int(age_input)

        if age > 0:
            break  # umur valid → keluar loop

        print(f"[{attempt}/5] Umur harus lebih dari 0. Coba lagi.")

    except ValueError:
        print(f"[{attempt}/5] Harus masukkan angka yang benar (contoh: 17, 25).")

else:
    # kalau sudah 5 kali gagal
    print("Sudah 5 kali salah input umur. Program berhenti.")
    exit()

print(f"Keren! {name} berumur {age} tahun 🎉")
