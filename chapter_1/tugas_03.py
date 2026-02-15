"""
==========================================================
 TUGAS 3 - Operator & Ekspresi
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Instruksi:
 1. Buat dua variabel bilangan bulat a dan b
 2. Tampilkan hasil semua operator aritmatika
    (+, -, *, /, //, %, **)
 3. Buat variabel boolean berdasarkan hasil perbandingan a dan b
 4. Demonstrasikan operator logika (and, or, not)
    dengan minimal 3 ekspresi berbeda
 5. Buat sebuah list dan demonstrasikan operator in dan not in
 6. Tunjukkan perbedaan == dan is menggunakan contoh list
==========================================================
"""

# -- Variabel ------------------------------------------------------------------
a = 15
b = 4


# -- Operator Aritmatika ------------------------------------------------------
print("=== Operator Aritmatika ===")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b}  = {a % b}")
print(f"{a} ** {b} = {a ** b}")


# -- Operator Perbandingan ----------------------------------------------------
print("\n=== Operator Perbandingan ===")
is_equal = a == b
is_not_equal = a != b
is_greater = a > b
is_less = a < b
is_greater_equal = a >= b
is_less_equal = a <= b

print(f"{a} == {b} ? {is_equal}")
print(f"{a} != {b} ? {is_not_equal}")
print(f"{a} > {b}  ? {is_greater}")
print(f"{a} < {b}  ? {is_less}")
print(f"{a} >= {b} ? {is_greater_equal}")
print(f"{a} <= {b} ? {is_less_equal}")


# -- Operator Logika ----------------------------------------------------------
print("\n=== Operator Logika ===")
print(f"(a > 0) and (b > 0)   = {(a > 0) and (b > 0)}")
print(f"(a > 100) or (b > 0)  = {(a > 100) or (b > 0)}")
print(f"not (a == b)           = {not (a == b)}")
print(f"(a > 10) and (b < 10) = {(a > 10) and (b < 10)}")


# -- Operator Keanggotaan (in, not in) ----------------------------------------
print("\n=== Operator Keanggotaan ===")
buah = ["apel", "mangga", "jeruk", "durian"]
print(f"buah = {buah}")
print(f"'apel' in buah?      {('apel' in buah)}")
print(f"'semangka' in buah?  {('semangka' in buah)}")
print(f"'durian' not in buah? {('durian' not in buah)}")
print(f"'anggur' not in buah? {('anggur' not in buah)}")


# -- Perbedaan == dan is ------------------------------------------------------
print("\n=== Perbedaan == dan is ===")
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a = {list_a}")
print(f"list_b = {list_b}")
print(f"list_c = list_a")
print(f"list_a == list_b ? {list_a == list_b}")   # True  - nilainya sama
print(f"list_a is list_b ? {list_a is list_b}")    # False - objek berbeda di memori
print(f"list_a is list_c ? {list_a is list_c}")    # True  - objek yang sama
