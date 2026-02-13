# Versi dengan nested loop + batas percobaan keseluruhan

for sesi in range(1, 4):  # outer loop: maksimal 3 kali kesempatan input lengkap
    print(f"\n--- Sesi {sesi} dari 3 ---")

    # Inner loop untuk nama
    nama_valid = False
    for percobaan_nama in range(1, 6):  # maksimal 5 kali coba nama
        name = input("Masukkan nama kamu: ").strip()

        if name:
            nama_valid = True
            break
        else:
            print(f"[{percobaan_nama}/5] Nama tidak boleh kosong! Coba lagi.")

    if not nama_valid:
        print("Nama tetap kosong setelah 5 kali percobaan. Sesi dibatalkan.")
        continue  # lanjut ke sesi berikutnya (jika ada)

    # Inner loop untuk umur
    umur_valid = False
    for percobaan_umur in range(1, 6):  # maksimal 5 kali coba umur
        try:
            age_str = input("Masukkan umur kamu: ").strip()
            age = int(age_str)

            if age > 0:
                umur_valid = True
                break
            else:
                print(f"[{percobaan_umur}/5] Umur harus lebih dari 0. Coba lagi.")

        except ValueError:
            print(f"[{percobaan_umur}/5] Harus angka yang valid ya (contoh: 18).")

    if not umur_valid:
        print("Umur tetap tidak valid setelah 5 kali percobaan. Sesi dibatalkan.")
        continue

    # Kalau sampai sini → input lengkap dan valid
    print(f"\nHalo {name}! Kamu berumur {age} tahun. Selamat datang! 🎉")
    break  # keluar dari outer loop karena sudah berhasil

else:
    # outer loop selesai tanpa break → gagal semua sesi
    print("\nKamu sudah mencoba 3 kali sesi, tetap gagal input yang benar.")
    print("Program selesai. Sampai jumpa lagi!")
