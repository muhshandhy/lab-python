"""
==========================================================
 TUGAS 1 - Analisis Statistik dengan NumPy
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import numpy as np


def buat_data_nilai(seed=42, jumlah=30, batas_bawah=40, batas_atas=100):
    """Membuat array nilai mahasiswa secara acak."""
    np.random.seed(seed)
    return np.random.randint(batas_bawah, batas_atas, jumlah)


def statistik_dasar(nilai):
    """Menghitung statistik dasar dari array nilai."""
    return {
        "mean": np.mean(nilai),
        "median": np.median(nilai),
        "std": np.std(nilai),
        "max": np.max(nilai),
        "min": np.min(nilai),
        "idx_max": np.argmax(nilai),
        "idx_min": np.argmin(nilai),
        "jumlah_lulus": int(np.sum(nilai >= 70)),
    }


def normalisasi_minmax(nilai):
    """Normalisasi Min-Max: (x - min) / (max - min)."""
    return (nilai - np.min(nilai)) / (np.max(nilai) - np.min(nilai))


def normalisasi_zscore(nilai):
    """Normalisasi Z-Score: (x - mean) / std."""
    return (nilai - np.mean(nilai)) / np.std(nilai)


def analisis_reshape(nilai, baris=6, kolom=5):
    """Reshape array dan hitung rata-rata per baris & kolom."""
    matriks = nilai.reshape(baris, kolom)
    rata_per_baris = np.mean(matriks, axis=1)
    rata_per_kolom = np.mean(matriks, axis=0)
    return matriks, rata_per_baris, rata_per_kolom


def tampilkan_hasil(nilai, stats, norm_mm, norm_zs, matriks, avg_baris, avg_kolom):
    """Menampilkan semua hasil analisis."""
    print("=" * 55)
    print(" ANALISIS STATISTIK NILAI MAHASISWA (NumPy)")
    print("=" * 55)

    print(f"\nData Nilai ({len(nilai)} mahasiswa):")
    print(nilai)

    print("\n-- Statistik Dasar --")
    print(f"  Mean   : {stats['mean']:.2f}")
    print(f"  Median : {stats['median']:.2f}")
    print(f"  Std Dev: {stats['std']:.2f}")
    print(f"  Max    : {stats['max']} (index {stats['idx_max']})")
    print(f"  Min    : {stats['min']} (index {stats['idx_min']})")
    print(f"  Lulus  : {stats['jumlah_lulus']}/{len(nilai)} ({stats['jumlah_lulus']/len(nilai)*100:.1f}%)")

    print("\n-- Normalisasi Min-Max (5 pertama) --")
    print(f"  Asli    : {nilai[:5]}")
    print(f"  Min-Max : {np.round(norm_mm[:5], 4)}")

    print("\n-- Normalisasi Z-Score (5 pertama) --")
    print(f"  Asli    : {nilai[:5]}")
    print(f"  Z-Score : {np.round(norm_zs[:5], 4)}")

    print(f"\n-- Reshape {matriks.shape[0]}x{matriks.shape[1]} --")
    print(matriks)
    print(f"\n  Rata-rata per baris (kelas) :")
    for i, avg in enumerate(avg_baris):
        print(f"    Kelas {i+1}: {avg:.2f}")
    print(f"  Rata-rata per kolom (ujian) : {np.round(avg_kolom, 2)}")


if __name__ == "__main__":
    nilai = buat_data_nilai()
    stats = statistik_dasar(nilai)
    norm_mm = normalisasi_minmax(nilai)
    norm_zs = normalisasi_zscore(nilai)
    matriks, avg_baris, avg_kolom = analisis_reshape(nilai)
    tampilkan_hasil(nilai, stats, norm_mm, norm_zs, matriks, avg_baris, avg_kolom)
