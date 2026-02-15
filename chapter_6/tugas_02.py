"""
==========================================================
 TUGAS 2 - Regresi: Prediksi Nilai Mahasiswa
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def buat_dataset(seed=42, n=200):
    """Buat dataset simulasi nilai mahasiswa."""
    np.random.seed(seed)
    jam_belajar = np.random.uniform(0, 20, n)
    kehadiran = np.random.uniform(50, 100, n)
    tugas_selesai = np.random.randint(0, 11, n)
    nilai_uts = np.random.uniform(0, 100, n)

    # Target: kombinasi linear dari fitur + noise
    nilai_akhir = (
        2.0 * jam_belajar
        + 0.3 * kehadiran
        + 3.5 * tugas_selesai
        + 0.4 * nilai_uts
        - 10
        + np.random.normal(0, 5, n)
    )
    nilai_akhir = np.clip(nilai_akhir, 0, 100)

    X = np.column_stack([jam_belajar, kehadiran, tugas_selesai, nilai_uts])
    feature_names = ["jam_belajar", "kehadiran", "tugas_selesai", "nilai_uts"]

    return X, nilai_akhir, feature_names


def evaluasi_regresi(y_true, y_pred):
    """Hitung metrik evaluasi regresi."""
    return {
        "MSE": mean_squared_error(y_true, y_pred),
        "RMSE": mean_squared_error(y_true, y_pred) ** 0.5,
        "MAE": mean_absolute_error(y_true, y_pred),
        "R2": r2_score(y_true, y_pred),
    }


if __name__ == "__main__":
    X, y, feature_names = buat_dataset()

    print("=" * 60)
    print(" REGRESI: PREDIKSI NILAI MAHASISWA")
    print("=" * 60)
    print(f"Jumlah data: {len(y)}")
    print(f"Fitur: {feature_names}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    eval_lr = evaluasi_regresi(y_test, y_pred_lr)

    print("\n--- Linear Regression ---")
    print("Koefisien:")
    for name, coef in zip(feature_names, lr_model.coef_):
        print(f"  {name:<15}: {coef:+.4f}")
    print(f"  {'intercept':<15}: {lr_model.intercept_:+.4f}")
    print(f"\nMSE  : {eval_lr['MSE']:.4f}")
    print(f"RMSE : {eval_lr['RMSE']:.4f}")
    print(f"MAE  : {eval_lr['MAE']:.4f}")
    print(f"R²   : {eval_lr['R2']:.4f}")

    # Polynomial Regression (degree=2)
    poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    poly_model.fit(X_train, y_train)
    y_pred_poly = poly_model.predict(X_test)
    eval_poly = evaluasi_regresi(y_test, y_pred_poly)

    print("\n--- Polynomial Regression (degree=2) ---")
    print(f"MSE  : {eval_poly['MSE']:.4f}")
    print(f"RMSE : {eval_poly['RMSE']:.4f}")
    print(f"MAE  : {eval_poly['MAE']:.4f}")
    print(f"R²   : {eval_poly['R2']:.4f}")

    # Perbandingan
    print(f"\n{'=' * 55}")
    print(" PERBANDINGAN LINEAR vs POLYNOMIAL")
    print(f"{'=' * 55}")
    print(f"{'Metrik':<8} | {'Linear':>10} | {'Polynomial':>10}")
    print("-" * 35)
    for m in ["MSE", "RMSE", "MAE", "R2"]:
        print(f"{m:<8} | {eval_lr[m]:>10.4f} | {eval_poly[m]:>10.4f}")

    # Prediksi data baru
    print(f"\n{'=' * 65}")
    print(" PREDIKSI NILAI AKHIR MAHASISWA BARU")
    print(f"{'=' * 65}")
    data_baru = np.array([
        [15, 95, 9, 85],
        [3, 60, 4, 50],
        [10, 80, 7, 70],
        [18, 98, 10, 90],
        [5, 55, 3, 40],
    ])
    prediksi = lr_model.predict(data_baru)
    print(f"{'No':>2} | {'Jam Belajar':>11} | {'Kehadiran':>9} | {'Tugas':>5} | {'UTS':>4} | {'Prediksi':>8}")
    print("-" * 55)
    for i, (d, p) in enumerate(zip(data_baru, prediksi), 1):
        print(f"{i:>2} | {d[0]:>11.0f} | {d[1]:>8.0f}% | {d[2]:>5.0f} | {d[3]:>4.0f} | {p:>8.1f}")

    # Interpretasi Koefisien
    # jam_belajar (~+2.0) : setiap +1 jam belajar, nilai naik ~2 poin
    # kehadiran (~+0.3)   : setiap +1% kehadiran, nilai naik ~0.3 poin
    # tugas_selesai (~+3.5): setiap +1 tugas, nilai naik ~3.5 poin -> PALING BERPENGARUH
    # nilai_uts (~+0.4)   : setiap +1 poin UTS, nilai akhir naik ~0.4 poin
