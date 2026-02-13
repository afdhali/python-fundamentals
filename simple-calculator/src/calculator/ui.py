from calculator.operations import OPERATIONS


def tampilkan_menu():
    print("\n" + "="*40)
    print("  KALKULATOR SEDERHANA  ")
    print("="*40)
    print("Operasi yang tersedia:")
    for op in OPERATIONS:
        print(f"  {op:<4} ", end="")
    print("\n" + "-"*40)
    print("Ketik 'q' atau 'keluar' untuk berhenti")


def ambil_input():
    while True:
        expr = input("\nMasukkan ekspresi (contoh: 5 + 3) → ").strip()
        if expr.lower() in ('q', 'keluar', 'exit'):
            return None

        parts = expr.split()
        if len(parts) != 3:
            print("Format salah. Gunakan: angka operator angka")
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
        except ValueError:
            print("Angka tidak valid")
            continue

        if op not in OPERATIONS:
            print(f"Operator '{op}' tidak dikenal")
            continue

        return a, op, b
