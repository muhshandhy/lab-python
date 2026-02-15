"""
==========================================================
 TUGAS 1 - Klasifikasi Dataset Wine
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def muat_dataset():
    """Muat dataset Wine dan tampilkan informasi dasar."""
    wine = load_wine()
    X, y = wine.data, wine.target

    print("=== INFO DATASET WINE ===")
    print(f"Jumlah sampel : {X.shape[0]}")
    print(f"Jumlah fitur  : {X.shape[1]}")
    print(f"Nama fitur    : {wine.feature_names}")
    print(f"Nama kelas    : {list(wine.target_names)}")
    print(f"Distribusi kelas:")
    for i, name in enumerate(wine.target_names):
        print(f"  {name}: {np.sum(y == i)} sampel")

    return X, y, wine


def preprocessing(X, y):
    """Train/test split dan standardisasi."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def latih_knn(X_train, X_test, y_train, y_test):
    """Latih KNN dengan beberapa nilai k, pilih terbaik."""
    best_k, best_acc = 3, 0
    print("\n--- KNN: Mencari K terbaik ---")
    for k in [3, 5, 7]:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        print(f"  k={k}: Accuracy = {acc:.4f}")
        if acc > best_acc:
            best_acc = acc
            best_k = k

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_train, y_train)
    print(f"  -> K terbaik: {best_k}")
    return model, best_k


def latih_decision_tree(X_train, y_train):
    """Latih Decision Tree."""
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    return model


def latih_random_forest(X_train, y_train):
    """Latih Random Forest."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluasi_model(model, X_test, y_test, nama_model):
    """Evaluasi model dan tampilkan metrik."""
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    cm = confusion_matrix(y_test, y_pred)

    print(f"\n{'=' * 50}")
    print(f" {nama_model}")
    print(f"{'=' * 50}")
    print(f"Accuracy: {acc:.4f}")
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Confusion Matrix:\n{cm}")

    return {
        "nama": nama_model,
        "accuracy": acc,
        "precision": report["weighted avg"]["precision"],
        "recall": report["weighted avg"]["recall"],
        "f1": report["weighted avg"]["f1-score"],
    }


def perbandingan_model(hasil_list):
    """Buat tabel perbandingan model."""
    print(f"\n{'=' * 65}")
    print(" PERBANDINGAN MODEL KLASIFIKASI")
    print(f"{'=' * 65}")
    print(f"{'Model':<20} | {'Accuracy':>8} | {'Precision':>9} | {'Recall':>6} | {'F1-Score':>8}")
    print("-" * 65)
    for h in hasil_list:
        print(f"{h['nama']:<20} | {h['accuracy']:>8.4f} | {h['precision']:>9.4f} | {h['recall']:>6.4f} | {h['f1']:>8.4f}")
    print("=" * 65)

    best = max(hasil_list, key=lambda x: x["accuracy"])
    print(f"Model Terbaik: {best['nama']} (Accuracy: {best['accuracy']*100:.1f}%)")
    return best


if __name__ == "__main__":
    X, y, wine = muat_dataset()
    X_train, X_test, y_train, y_test, scaler = preprocessing(X, y)

    knn_model, best_k = latih_knn(X_train, X_test, y_train, y_test)
    dt_model = latih_decision_tree(X_train, y_train)
    rf_model = latih_random_forest(X_train, y_train)

    hasil_knn = evaluasi_model(knn_model, X_test, y_test, f"KNN (k={best_k})")
    hasil_dt = evaluasi_model(dt_model, X_test, y_test, "Decision Tree")
    hasil_rf = evaluasi_model(rf_model, X_test, y_test, "Random Forest")

    best = perbandingan_model([hasil_knn, hasil_dt, hasil_rf])

    # Prediksi data baru
    print("\n=== PREDIKSI DATA BARU ===")
    models = {"KNN": knn_model, "Decision Tree": dt_model, "Random Forest": rf_model}
    best_model = rf_model
    data_baru = np.array([
        [13.0, 2.0, 2.3, 20.0, 100.0, 2.5, 2.5, 0.3, 1.5, 5.0, 1.0, 3.0, 1000],
        [12.0, 1.5, 2.0, 18.0, 80.0, 2.0, 2.0, 0.4, 1.2, 4.0, 0.8, 2.5, 700],
        [14.0, 3.0, 2.5, 22.0, 120.0, 3.0, 3.0, 0.2, 2.0, 6.0, 1.2, 3.5, 1200],
    ])
    data_baru_scaled = scaler.transform(data_baru)
    prediksi = best_model.predict(data_baru_scaled)
    for i, pred in enumerate(prediksi, 1):
        print(f"  Data {i}: Kelas {pred} ({wine.target_names[pred]})")

    # Analisis
    # Random Forest umumnya memberikan performa terbaik karena menggunakan
    # ensemble dari banyak decision tree, sehingga mengurangi overfitting
    # dan memiliki kemampuan generalisasi yang lebih baik.
