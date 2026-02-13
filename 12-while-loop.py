name = ""

while not name.strip():  # biar ga bisa cuma enter doang / spasi
    name = input("Enter your name: ").strip()

print(f"Hello {name}!")

# Bagian umur - lebih aman pakai try-except
while True:
    try:
        age = int(input("Enter your age: "))

        if age <= 0:
            print("Umur harus lebih dari 0")
            continue

        # kalau sampai sini berarti umur valid
        break

    except ValueError:
        print("Masukkan angka yang benar ya (contoh: 17, 25, dll)")

print(f"Keren! {name} berumur {age} tahun")
