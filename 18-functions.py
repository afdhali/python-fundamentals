def happy_birthday(name="Someone", age="??"):
    print("Happy Birthday to you!")
    # pakai {age} langsung, aman meski string
    print(f"You are {age} old!")
    print("Happy Birthday to you")
    # tanpa f-string biar rapi kalau nama panjang
    print(name)


# Contoh pemanggilan
happy_birthday()                        # pakai default
happy_birthday("Afdhali")               # hanya nama
happy_birthday(age=20)                  # hanya umur (keyword argument)
happy_birthday("Budi", 17)              # normal
# urutan boleh dibalik kalau pakai nama parameter
happy_birthday(age=15, name="Caca")
