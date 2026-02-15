"""
==========================================================
 TUGAS 4 - Proyek Mini: End-to-End ML Pipeline
 Opsi A: Klasifikasi Kelayakan Beasiswa
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def buat_dataset_beasiswa(seed=42, n=200):
    """Buat dataset simulasi kelayakan beasiswa."""
    np.random.seed(seed)

    ipk = np.random.uniform(2.0, 4.0, n)
    penghasilan_ortu = np.random.uniform(1_000_000, 15_000_000, n)
    semester = np.random.randint(2, 9, n)
    tanggungan = np.random.randint(1, 7, n)
    prestasi = np.random.uniform(0, 100, n)

    # Target: layak jika skor tinggi
    skor = (
        ipk * 15
        - penghasilan_ortu / 1_000_000
        + tanggungan * 3
        + prestasi * 0.3
        + np.random.normal(0, 5, n)
    )
    layak = (skor > np.median(skor)).astype(int)

    X = np.column_stack([ipk, penghasilan_ortu, semester, tanggungan, prestasi])
    feature_names = ["IPK", "Penghasilan_Ortu", "Semester", "Tanggungan", "Prestasi"]

    return X, layak, feature_names


def preprocessing(X, y):
    """Split dan scaling data."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def evaluasi(model, X_test, y_test, nama):
    """Evaluasi model klasifikasi."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    print(f"\n--- {nama} ---")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred, target_names=["Tidak Layak", "Layak"]))
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

    return {
        "nama": nama,
        "accuracy": acc,
        "precision": report["weighted avg"]["precision"],
        "recall": report["weighted avg"]["recall"],
        "f1": report["weighted avg"]["f1-score"],
    }


if __name__ == "__main__":
    print("=" * 60)
    print(" PROYEK MINI: KLASIFIKASI KELAYAKAN BEASISWA")
    print("=" * 60)

    X, y, feature_names = buat_dataset_beasiswa()
    print(f"Jumlah data   : {len(y)}")
    print(f"Fitur         : {feature_names}")
    print(f"Layak         : {np.sum(y == 1)}")
    print(f"Tidak Layak   : {np.sum(y == 0)}")

    X_train, X_test, y_train, y_test, scaler = preprocessing(X, y)

    # Model 1: Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    hasil_rf = evaluasi(rf, X_test, y_test, "Random Forest")

    # Model 2: Gradient Boosting
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb.fit(X_train, y_train)
    hasil_gb = evaluasi(gb, X_test, y_test, "Gradient Boosting")

    # Model 3: Logistic Regression
    lr = LogisticRegression(random_state=42, max_iter=1000)
    lr.fit(X_train, y_train)
    hasil_lr = evaluasi(lr, X_test, y_test, "Logistic Regression")

    # Perbandingan
    print(f"\n{'=' * 65}")
    print(" PERBANDINGAN MODEL")
    print(f"{'=' * 65}")
    print(f"{'Model':<22} | {'Accuracy':>8} | {'Precision':>9} | {'Recall':>6} | {'F1':>6}")
    print("-" * 60)
    for h in [hasil_rf, hasil_gb, hasil_lr]:
        print(f"{h['nama']:<22} | {h['accuracy']:>8.4f} | {h['precision']:>9.4f} | {h['recall']:>6.4f} | {h['f1']:>6.4f}")

    best = max([hasil_rf, hasil_gb, hasil_lr], key=lambda x: x["accuracy"])
    print(f"\nModel Terbaik: {best['nama']} (Accuracy: {best['accuracy']*100:.1f}%)")

    # Feature Importance (Random Forest)
    print(f"\n--- Feature Importance (Random Forest) ---")
    importances = rf.feature_importances_
    for name, imp in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
        print(f"  {name:<20}: {imp:.4f}")

    # Prediksi data baru
    print(f"\n--- Prediksi Mahasiswa Baru ---")
    data_baru = np.array([
        [3.8, 2_000_000, 5, 4, 85],
        [2.5, 10_000_000, 3, 2, 30],
        [3.5, 3_500_000, 6, 5, 70],
        [3.0, 8_000_000, 4, 1, 50],
        [3.9, 1_500_000, 7, 6, 90],
    ])
    data_baru_scaled = scaler.transform(data_baru)
    prediksi = rf.predict(data_baru_scaled)
    label = ["Tidak Layak", "Layak"]

    print(f"{'No':>2} | {'IPK':>4} | {'Penghasilan':>12} | {'Smt':>3} | {'Tgg':>3} | {'Prestasi':>8} | {'Prediksi'}")
    print("-" * 65)
    for i, (d, p) in enumerate(zip(data_baru, prediksi), 1):
        print(f"{i:>2} | {d[0]:>4.1f} | Rp{d[1]:>10,.0f} | {d[2]:>3.0f} | {d[3]:>3.0f} | {d[4]:>8.0f} | {label[p]}")

    # Kesimpulan:
    # Model Random Forest/Gradient Boosting memberikan performa terbaik.
    # Fitur yang paling berpengaruh adalah IPK dan Penghasilan Orang Tua.
    # Mahasiswa dengan IPK tinggi dan penghasilan ortu rendah cenderung layak beasiswa.
