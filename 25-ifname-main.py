# if __name__ == "__main__":
#     # kode yang hanya dijalankan jika file ini di-RUN langsung
#     main()
#     # atau print("Hello"), atau unittest.main(), dll


def tambah(a, b):
    return a + b


def kali(a, b):
    return a * b


print("Ini muncul setiap kali file diimport atau di-run!")

if __name__ == "__main__":
    print("Hanya muncul jika di-run langsung")
    print("Hasil tambah(5, 3) =", tambah(5, 3))
    print("Hasil kali(4, 6)   =", kali(4, 6))
