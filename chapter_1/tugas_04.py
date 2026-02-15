"""
==========================================================
 TUGAS 4 - Menghitung Luas & Keliling Bangun Datar
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Instruksi:
 1. Buat variabel untuk dimensi: persegi, persegi panjang,
    lingkaran, dan segitiga
 2. Hitung luas dan keliling masing-masing bangun datar
 3. Gunakan konstanta PI = 3.14159 untuk lingkaran
 4. Tampilkan hasil dalam format tabel yang rapi
 5. Gunakan operator assignment (+=) untuk menghitung total luas
==========================================================
"""

# -- Konstanta -----------------------------------------------------------------
PI = 3.14159

# -- Dimensi Bangun Datar -----------------------------------------------------

# Persegi
sisi_persegi = 5

# Persegi Panjang
panjang = 10
lebar = 4

# Lingkaran
jari_jari = 5

# Segitiga (sisi a, b, c dan tinggi)
sisi_a = 6
sisi_b = 8
sisi_c = 10
tinggi_segitiga = 4.8
alas_segitiga = 10


# -- Perhitungan Luas ----------------------------------------------------------
luas_persegi = sisi_persegi * sisi_persegi
luas_persegi_panjang = panjang * lebar
luas_lingkaran = PI * jari_jari ** 2
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga


# -- Perhitungan Keliling ------------------------------------------------------
keliling_persegi = 4 * sisi_persegi
keliling_persegi_panjang = 2 * (panjang + lebar)
keliling_lingkaran = 2 * PI * jari_jari
keliling_segitiga = sisi_a + sisi_b + sisi_c


# -- Total Luas (gunakan operator +=) -----------------------------------------
total_luas = 0
total_luas += luas_persegi
total_luas += luas_persegi_panjang
total_luas += luas_lingkaran
total_luas += luas_segitiga


# -- Tampilkan Hasil dalam Format Tabel ----------------------------------------
print("============ LUAS & KELILING BANGUN DATAR ============")
print(f"{'Bangun':<18}| {'Luas':>9} | {'Keliling':>9}")
print("-" * 50)
print(f"{'Persegi':<18}| {luas_persegi:>9.2f} | {keliling_persegi:>9.2f}")
print(f"{'Persegi Panjang':<18}| {luas_persegi_panjang:>9.2f} | {keliling_persegi_panjang:>9.2f}")
print(f"{'Lingkaran':<18}| {luas_lingkaran:>9.2f} | {keliling_lingkaran:>9.2f}")
print(f"{'Segitiga':<18}| {luas_segitiga:>9.2f} | {keliling_segitiga:>9.2f}")
print("-" * 50)
print(f"{'Total Luas':<18}| {total_luas:>9.2f}")
print("=" * 50)
