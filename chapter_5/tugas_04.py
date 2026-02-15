"""
==========================================================
 TUGAS 4 - Analisis Data Penjualan
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import pandas as pd
import numpy as np


PRODUK_INFO = {
    "Laptop": {"kategori": "Elektronik", "harga": 12_000_000},
    "Mouse": {"kategori": "Elektronik", "harga": 150_000},
    "Buku Tulis": {"kategori": "ATK", "harga": 15_000},
    "Pulpen": {"kategori": "ATK", "harga": 8_000},
    "Flash Drive": {"kategori": "Elektronik", "harga": 85_000},
}


def buat_data_penjualan(seed=42, jumlah_hari=30):
    """Membuat DataFrame data penjualan harian."""
    np.random.seed(seed)
    tanggal = pd.date_range(start="2025-01-01", periods=jumlah_hari, freq="D")
    produk_list = list(PRODUK_INFO.keys())
    produk = np.random.choice(produk_list, jumlah_hari)
    kategori = [PRODUK_INFO[p]["kategori"] for p in produk]
    harga = [PRODUK_INFO[p]["harga"] for p in produk]
    quantity = np.random.randint(1, 51, jumlah_hari)

    df = pd.DataFrame({
        "Tanggal": tanggal,
        "Produk": produk,
        "Kategori": kategori,
        "Quantity": quantity,
        "Harga_Satuan": harga,
    })
    df["Total"] = df["Quantity"] * df["Harga_Satuan"]
    return df


def analisis_keseluruhan(df):
    """Menghitung metrik analisis keseluruhan."""
    total = df["Total"].sum()
    penjualan_harian = df.groupby("Tanggal")["Total"].sum()
    rata_harian = penjualan_harian.mean()

    penjualan_produk = df.groupby("Produk")["Total"].sum()
    produk_terlaris = penjualan_produk.idxmax()

    penjualan_kategori = df.groupby("Kategori")["Total"].sum()
    kategori_terlaris = penjualan_kategori.idxmax()

    hari_terbaik = (penjualan_harian.idxmax(), penjualan_harian.max())
    hari_terburuk = (penjualan_harian.idxmin(), penjualan_harian.min())

    return {
        "total_penjualan": total,
        "rata_per_hari": rata_harian,
        "produk_terlaris": produk_terlaris,
        "kategori_terlaris": kategori_terlaris,
        "hari_terbaik": hari_terbaik,
        "hari_terburuk": hari_terburuk,
    }


def ringkasan_per_produk(df):
    """Membuat ringkasan penjualan per produk."""
    return df.groupby("Produk").agg(
        Total_Penjualan=("Total", "sum"),
        Rata_Rata=("Total", "mean"),
        Jumlah_Transaksi=("Total", "count"),
        Total_Quantity=("Quantity", "sum"),
    ).sort_values("Total_Penjualan", ascending=False)


def ringkasan_per_kategori(df):
    """Membuat ringkasan penjualan per kategori."""
    return df.groupby("Kategori").agg(
        Total_Penjualan=("Total", "sum"),
        Rata_Rata=("Total", "mean"),
        Jumlah_Transaksi=("Total", "count"),
    )


def format_rupiah(angka):
    """Format angka ke format Rupiah."""
    return f"Rp {angka:,.0f}".replace(",", ".")


def tampilkan_hasil(df, analisis, per_produk, per_kategori):
    """Menampilkan semua hasil analisis."""
    print("=" * 60)
    print(" ANALISIS DATA PENJUALAN")
    print("=" * 60)

    print(f"\n-- Data Penjualan (5 baris pertama) --")
    print(df.head())

    print(f"\n-- Ringkasan Keseluruhan --")
    print(f"  Total Penjualan   : {format_rupiah(analisis['total_penjualan'])}")
    print(f"  Rata-rata/Hari    : {format_rupiah(analisis['rata_per_hari'])}")
    print(f"  Produk Terlaris   : {analisis['produk_terlaris']}")
    print(f"  Kategori Terlaris : {analisis['kategori_terlaris']}")

    tgl_best, total_best = analisis["hari_terbaik"]
    tgl_worst, total_worst = analisis["hari_terburuk"]
    print(f"  Hari Terbaik      : {tgl_best.strftime('%d %b %Y')} ({format_rupiah(total_best)})")
    print(f"  Hari Terburuk     : {tgl_worst.strftime('%d %b %Y')} ({format_rupiah(total_worst)})")

    print(f"\n-- Ringkasan per Produk --")
    print(per_produk)

    print(f"\n-- Ringkasan per Kategori --")
    print(per_kategori)


if __name__ == "__main__":
    df = buat_data_penjualan()
    analisis = analisis_keseluruhan(df)
    per_produk = ringkasan_per_produk(df)
    per_kategori = ringkasan_per_kategori(df)
    tampilkan_hasil(df, analisis, per_produk, per_kategori)
