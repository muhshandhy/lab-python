"""
==========================================================
 TUGAS 3 - Kalkulator Serbaguna
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""


def kalkulator(a, b, operasi="+"):
    """Kalkulator dasar dengan default parameter.

    Args:
        a (float): Bilangan pertama.
        b (float): Bilangan kedua.
        operasi (str): Operator (+, -, *, /, //, %, **). Default: "+".

    Returns:
        float: Hasil perhitungan, atau None jika operasi tidak valid.
    """
    if operasi == "+":
        return a + b
    elif operasi == "-":
        return a - b
    elif operasi == "*":
        return a * b
    elif operasi == "/":
        if b == 0:
            return "Error: Pembagian dengan nol!"
        return a / b
    elif operasi == "//":
        if b == 0:
            return "Error: Pembagian dengan nol!"
        return a // b
    elif operasi == "%":
        if b == 0:
            return "Error: Pembagian dengan nol!"
        return a % b
    elif operasi == "**":
        return a ** b
    else:
        return None


def statistik(*args):
    """Menghitung statistik dari sekumpulan angka.

    Args:
        *args: Bilangan-bilangan yang akan dihitung statistiknya.

    Returns:
        dict: {"min": ..., "max": ..., "sum": ..., "mean": ..., "count": ...}
    """
    if not args:
        return {}
    return {
        "min": min(args),
        "max": max(args),
        "sum": sum(args),
        "mean": sum(args) / len(args),
        "count": len(args),
    }


def format_output(**kwargs):
    """Mencetak data dalam format key: value yang rapi.

    Args:
        **kwargs: Pasangan key-value yang akan dicetak.
    """
    for key, value in kwargs.items():
        print(f"  {key:<15}: {value}")


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Kalkulator ===")
    operasi_list = ["+", "-", "*", "/", "//", "%", "**"]
    for op in operasi_list:
        print(f"10 {op} 3 = {kalkulator(10, 3, op)}")
    print(f"10 / 0 = {kalkulator(10, 0, '/')}")

    print("\n=== Statistik (*args) ===")
    hasil = statistik(85, 90, 78, 92, 65, 88, 73)
    for key, value in hasil.items():
        print(f"  {key:<6}: {value}")

    print("\n=== Format Output (**kwargs) ===")
    format_output(nama="MUH NUR SANDI", nim="105841106721", jurusan="Informatika")

    # Lambda + map() -> hitung kuadrat
    angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kuadrat = list(map(lambda x: x ** 2, angka))
    print(f"\nLambda + map (kuadrat): {kuadrat}")

    # Lambda + filter() -> bilangan genap
    genap = list(filter(lambda x: x % 2 == 0, angka))
    print(f"Lambda + filter (genap): {genap}")

    # Lambda + sorted() -> urutkan list of tuple
    mahasiswa = [("Ahmad", 85), ("Siti", 92), ("Budi", 78), ("Dewi", 90)]
    by_nilai = sorted(mahasiswa, key=lambda x: x[1], reverse=True)
    print(f"Lambda + sorted (by nilai desc): {by_nilai}")
