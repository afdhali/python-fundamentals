def tambah(a: float, b: float) -> float:
    return a + b


def kurang(a: float, b: float) -> float:
    return a - b


def kali(a: float, b: float) -> float:
    return a * b


def bagi(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol!")
    return a / b


OPERATIONS = {
    "+": tambah,
    "-": kurang,
    "*": kali,
    "/": bagi,
}
