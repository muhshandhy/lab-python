"""
==========================================================
 TUGAS 2 - Pola & Deret
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""


def pola_segitiga(n):
    """Mencetak pola segitiga bintang dengan tinggi n."""
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def pola_segitiga_terbalik(n):
    """Mencetak pola segitiga terbalik dengan tinggi n."""
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)


def pola_diamond(n):
    """Mencetak pola diamond/berlian."""
    # Bagian atas
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Bagian bawah
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def deret_fibonacci(n):
    """Mengembalikan list berisi n bilangan Fibonacci pertama."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def is_prima(n):
    """Memeriksa apakah n adalah bilangan prima."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Pola Segitiga (n=5) ===")
    pola_segitiga(5)

    print("\n=== Pola Segitiga Terbalik (n=5) ===")
    pola_segitiga_terbalik(5)

    print("\n=== Pola Diamond (n=5) ===")
    pola_diamond(5)

    print(f"\nFibonacci (15): {deret_fibonacci(15)}")

    bilangan_prima = list(filter(is_prima, range(1, 101)))
    print(f"\nBilangan prima (1-100): {bilangan_prima}")
    print(f"Jumlah: {len(bilangan_prima)}")
