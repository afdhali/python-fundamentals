from calculator.ui import tampilkan_menu, ambil_input
from calculator.operations import OPERATIONS


def main():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Ketik 'q' atau 'keluar' untuk berhenti\n")

    while True:
        tampilkan_menu()
        result = ambil_input()
        if result is None:
            print("\nTerima kasih telah menggunakan kalkulator!")
            break

        a, op, b = result

        try:
            hasil = OPERATIONS[op](a, b)
            print(f"Hasil: {a} {op} {b} = {hasil}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    main()
