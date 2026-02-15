"""
==========================================================
 TUGAS 3 - Handling Missing Data
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import pandas as pd
import numpy as np


def buat_data_dengan_missing():
    """Membuat DataFrame dengan data yang memiliki missing values."""
    data = {
        "Nama": ["Ahmad", "Budi", "Citra", "Dewi", "Eko",
                  "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
                  "Kamal", "Lina"],
        "Usia": [20, 21, np.nan, 22, 20, np.nan, 23, 21, 20, np.nan, 22, 21],
        "IPK": [3.5, np.nan, 3.2, 3.8, np.nan, 3.1, 3.6, np.nan, 3.4, 3.7, np.nan, 3.3],
        "Jurusan": ["Informatika", "SI", np.nan, "Informatika", "Elektro",
                     "SI", np.nan, "Informatika", "Elektro", np.nan,
                     "SI", "Informatika"],
        "Skor_Survei": [85, 90, 78, np.nan, 88, 92, np.nan, 75, np.nan, 80, 95, np.nan],
    }
    return pd.DataFrame(data)


def deteksi_missing(df):
    """Mendeteksi dan menampilkan informasi missing values."""
    jumlah = df.isnull().sum()
    persen = (df.isnull().sum() / len(df)) * 100
    return jumlah, persen


def versi_dropna(df):
    """Versi 1: Menghapus baris yang mengandung NaN."""
    return df.dropna()


def versi_fillna_statistik(df):
    """Versi 2: Mengisi NaN -- numerik dengan mean, kategorikal dengan mode."""
    df_filled = df.copy()
    for col in df_filled.select_dtypes(include=["number"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
    for col in df_filled.select_dtypes(include=["object"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
    return df_filled


def versi_fillna_ffill(df):
    """Versi 3: Mengisi NaN dengan forward fill."""
    return df.ffill()


def bandingkan_hasil(df_asli, df_dropna, df_fillna_stat, df_fillna_ffill):
    """Membandingkan jumlah baris dan sisa NaN dari ketiga versi."""
    print(f"{'Metode':<25} | {'Baris':>5} | {'NaN Tersisa':>11}")
    print("-" * 48)
    print(f"{'Data Asli':<25} | {len(df_asli):>5} | {df_asli.isnull().sum().sum():>11}")
    print(f"{'dropna()':<25} | {len(df_dropna):>5} | {df_dropna.isnull().sum().sum():>11}")
    print(f"{'fillna (mean/mode)':<25} | {len(df_fillna_stat):>5} | {df_fillna_stat.isnull().sum().sum():>11}")
    print(f"{'fillna (ffill)':<25} | {len(df_fillna_ffill):>5} | {df_fillna_ffill.isnull().sum().sum():>11}")


# -- Kapan Menggunakan Metode Mana? -------------------------------------------
#
# dropna():
#   - Gunakan ketika: data yang hilang sangat sedikit dan baris bisa dibuang
#   - Risiko: kehilangan data penting, terutama jika banyak NaN tersebar
#   - Contoh kasus: dataset besar di mana kehilangan beberapa baris tidak signifikan
#
# fillna(mean/mode):
#   - Gunakan ketika: data hilang cukup banyak tapi distribusi data relatif normal
#   - Risiko: mengurangi variasi data, bisa bias jika data tidak terdistribusi normal
#   - Contoh kasus: data survei di mana beberapa responden melewatkan pertanyaan
#
# fillna(ffill):
#   - Gunakan ketika: data bersifat time-series atau berurutan (sequential)
#   - Risiko: tidak tepat untuk data yang tidak berurutan atau acak
#   - Contoh kasus: data sensor, data harga saham, data suhu harian


if __name__ == "__main__":
    df = buat_data_dengan_missing()

    print("=" * 55)
    print(" HANDLING MISSING DATA")
    print("=" * 55)

    print("\n-- Data Asli --")
    print(df)

    print("\n-- Deteksi Missing Values --")
    jumlah, persen = deteksi_missing(df)
    print(f"Jumlah NaN per kolom:\n{jumlah}")
    print(f"\nPersentase NaN per kolom:\n{persen.round(1)}")

    print("\n-- Versi 1: dropna() --")
    df_v1 = versi_dropna(df)
    print(df_v1)

    print("\n-- Versi 2: fillna (mean/mode) --")
    df_v2 = versi_fillna_statistik(df)
    print(df_v2)

    print("\n-- Versi 3: fillna (ffill) --")
    df_v3 = versi_fillna_ffill(df)
    print(df_v3)

    print("\n-- Perbandingan Hasil --")
    bandingkan_hasil(df, df_v1, df_v2, df_v3)
