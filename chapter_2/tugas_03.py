"""
==========================================================
 TUGAS 3 - Analisis Teks dengan Set
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Instruksi:
 1. Definisikan 2 string kalimat (minimal 10 kata per kalimat)
 2. Konversi setiap kalimat menjadi set kata unik (lowercase)
 3. Tampilkan intersection (kata di kedua kalimat)
 4. Tampilkan difference (kata hanya di kalimat 1 / kalimat 2)
 5. Tampilkan union (semua kata unik)
 6. Tampilkan symmetric difference (kata di salah satu saja)
 7. Hitung jumlah kata unik total
==========================================================
"""

# -- Data Kalimat --------------------------------------------------------------
kalimat_1 = "python adalah bahasa pemrograman yang populer dan mudah untuk dipelajari"
kalimat_2 = "bahasa python sangat cocok untuk pemula yang ingin belajar pemrograman dengan mudah"

print("===== ANALISIS TEKS DENGAN SET =====")
print(f"Kalimat 1: {kalimat_1}")
print(f"Kalimat 2: {kalimat_2}")


# -- Konversi ke Set -----------------------------------------------------------
kata_set_1 = set(kalimat_1.lower().split())
kata_set_2 = set(kalimat_2.lower().split())

print(f"\nSet Kalimat 1 ({len(kata_set_1)} kata): {kata_set_1}")
print(f"Set Kalimat 2 ({len(kata_set_2)} kata): {kata_set_2}")


# -- Intersection (kata yang muncul di KEDUA kalimat) --------------------------
kata_sama = kata_set_1 & kata_set_2
print(f"\nIntersection (di kedua kalimat)   : {kata_sama}")


# -- Difference (kata HANYA di kalimat 1) --------------------------------------
hanya_kalimat_1 = kata_set_1 - kata_set_2
print(f"Difference (hanya kalimat 1)      : {hanya_kalimat_1}")


# -- Difference (kata HANYA di kalimat 2) --------------------------------------
hanya_kalimat_2 = kata_set_2 - kata_set_1
print(f"Difference (hanya kalimat 2)      : {hanya_kalimat_2}")


# -- Union (SEMUA kata unik dari kedua kalimat) --------------------------------
semua_kata = kata_set_1 | kata_set_2
print(f"Union (semua kata unik)           : {semua_kata}")


# -- Symmetric Difference (kata di SALAH SATU saja) ----------------------------
kata_unik_masing = kata_set_1 ^ kata_set_2
print(f"Symmetric Difference (salah satu) : {kata_unik_masing}")


# -- Jumlah Kata Unik Total ---------------------------------------------------
print(f"\nJumlah kata unik total: {len(semua_kata)}")
