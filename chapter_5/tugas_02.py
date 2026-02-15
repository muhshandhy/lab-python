"""
==========================================================
 TUGAS 2 - Analisis Data Mahasiswa dengan Pandas
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import pandas as pd
import numpy as np


def buat_dataframe_mahasiswa(seed=42):
    """Membuat DataFrame berisi data 20 mahasiswa."""
    np.random.seed(seed)

    nama_list = [
        "Ahmad", "Budi", "Citra", "Dewi", "Eko",
        "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
        "Kamal", "Lina", "Mira", "Naufal", "Olivia",
        "Putra", "Qory", "Rizky", "Sari", "Taufik",
    ]

    jurusan_list = ["Informatika", "Sistem Informasi", "Teknik Elektro"]

    data = {
        "Nama": nama_list,
        "NIM": [f"10520{i:04d}" for i in range(1, 21)],
        "Jurusan": np.random.choice(jurusan_list, 20),
        "Semester": np.random.randint(2, 9, 20),
        "IPK": np.round(np.random.uniform(2.0, 4.0, 20), 2),
        "Jenis_Kelamin": np.random.choice(["L", "P"], 20),
    }

    return pd.DataFrame(data)


def info_dasar(df):
    """Menampilkan informasi dasar DataFrame."""
    print(f"Shape: {df.shape}")
    print(f"\nTipe Data:\n{df.dtypes}")
    print(f"\nStatistik Deskriptif:\n{df.describe()}")


def filter_ipk_tinggi(df, batas_ipk=3.5):
    """Filter mahasiswa dengan IPK >= batas_ipk."""
    return df[df["IPK"] >= batas_ipk]


def filter_jurusan_semester(df, jurusan="Informatika", min_semester=5):
    """Filter mahasiswa berdasarkan jurusan DAN minimum semester."""
    return df[(df["Jurusan"] == jurusan) & (df["Semester"] >= min_semester)]


def top_mahasiswa(df, n=5):
    """Mengurutkan berdasarkan IPK dan mengambil top n."""
    return df.sort_values("IPK", ascending=False).head(n)


def statistik_per_jurusan(df):
    """Menghitung statistik IPK per jurusan."""
    return df.groupby("Jurusan")["IPK"].agg(["mean", "min", "max", "count"])


def jumlah_per_gender_jurusan(df):
    """Menghitung jumlah mahasiswa per jenis_kelamin per jurusan."""
    return pd.crosstab(df["Jurusan"], df["Jenis_Kelamin"])


def tambah_predikat(df):
    """Menambah kolom Predikat berdasarkan IPK."""
    conditions = [
        df["IPK"] >= 3.5,
        df["IPK"] >= 3.0,
        df["IPK"] >= 2.5,
    ]
    choices = ["Cum Laude", "Sangat Memuaskan", "Memuaskan"]
    df["Predikat"] = np.select(conditions, choices, default="Cukup")
    return df


def distribusi_predikat(df):
    """Menampilkan distribusi predikat."""
    return df["Predikat"].value_counts()


if __name__ == "__main__":
    df = buat_dataframe_mahasiswa()

    print("=" * 60)
    print(" ANALISIS DATA MAHASISWA (Pandas)")
    print("=" * 60)

    print("\n-- Info Dasar --")
    info_dasar(df)

    print("\n-- Mahasiswa IPK >= 3.5 --")
    print(filter_ipk_tinggi(df))

    print("\n-- Informatika & Semester >= 5 --")
    print(filter_jurusan_semester(df))

    print("\n-- Top 5 Mahasiswa --")
    print(top_mahasiswa(df))

    print("\n-- Statistik IPK per Jurusan --")
    print(statistik_per_jurusan(df))

    print("\n-- Jumlah per Gender per Jurusan --")
    print(jumlah_per_gender_jurusan(df))

    df = tambah_predikat(df)
    print("\n-- DataFrame dengan Predikat --")
    print(df[["Nama", "IPK", "Predikat"]])

    print("\n-- Distribusi Predikat --")
    print(distribusi_predikat(df))
