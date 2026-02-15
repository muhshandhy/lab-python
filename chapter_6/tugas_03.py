"""
==========================================================
 TUGAS 3 - Clustering: Segmentasi Mahasiswa
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def buat_dataset(seed=42, n=150):
    """Buat dataset simulasi mahasiswa dengan 3 cluster natural."""
    np.random.seed(seed)
    n1, n2, n3 = 50, 55, 45

    # Cluster 0: Mahasiswa Berprestasi
    c0 = np.column_stack([
        np.random.uniform(3.3, 4.0, n1),
        np.random.uniform(14, 25, n1),
        np.random.uniform(85, 100, n1),
        np.random.uniform(5, 10, n1),
    ])

    # Cluster 1: Mahasiswa Standar
    c1 = np.column_stack([
        np.random.uniform(2.5, 3.3, n2),
        np.random.uniform(7, 15, n2),
        np.random.uniform(65, 85, n2),
        np.random.uniform(2, 6, n2),
    ])

    # Cluster 2: Mahasiswa Berisiko
    c2 = np.column_stack([
        np.random.uniform(1.5, 2.5, n3),
        np.random.uniform(0, 8, n3),
        np.random.uniform(40, 65, n3),
        np.random.uniform(0, 3, n3),
    ])

    X = np.vstack([c0, c1, c2])
    feature_names = ["ipk", "jam_belajar", "kehadiran_persen", "aktivitas_organisasi"]
    return X, feature_names


def elbow_method(X_scaled):
    """Jalankan K-Means untuk K=2..10 dan tampilkan Inertia & Silhouette."""
    print("\n--- Elbow Method ---")
    print(f"{'K':>3} | {'Inertia':>12} | {'Silhouette':>10}")
    print("-" * 32)

    results = []
    for k in range(2, 11):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X_scaled)
        sil = silhouette_score(X_scaled, km.labels_)
        results.append({"k": k, "inertia": km.inertia_, "silhouette": sil})
        print(f"{k:>3} | {km.inertia_:>12.2f} | {sil:>10.4f}")

    return results


if __name__ == "__main__":
    X, feature_names = buat_dataset()

    print("=" * 60)
    print(" CLUSTERING: SEGMENTASI MAHASISWA")
    print("=" * 60)
    print(f"Jumlah data: {len(X)}")
    print(f"Fitur: {feature_names}")

    # Standardisasi
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Elbow Method
    results = elbow_method(X_scaled)

    # K Optimal = 3
    k_optimal = 3
    print(f"\nK Optimal: {k_optimal}")

    # K-Means
    kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    labels = kmeans.labels_
    sil_score = silhouette_score(X_scaled, labels)

    print(f"Silhouette Score: {sil_score:.4f}")

    # Profil Cluster
    nama_segment = {0: "Mahasiswa Berprestasi", 1: "Mahasiswa Standar", 2: "Mahasiswa Berisiko"}

    print(f"\n{'=' * 85}")
    print(" PROFIL CLUSTER")
    print(f"{'=' * 85}")
    print(f"{'Cluster':>7} | {'Segment':<22} | {'Jumlah':>6} | {'IPK':>5} | {'Jam Belajar':>11} | {'Kehadiran':>9} | {'Organisasi':>10}")
    print("-" * 85)

    cluster_profiles = {}
    for c in range(k_optimal):
        mask = labels == c
        data_cluster = X[mask]
        means = data_cluster.mean(axis=0)
        cluster_profiles[c] = means

    # Urutkan cluster berdasarkan IPK (tertinggi = berprestasi)
    sorted_clusters = sorted(cluster_profiles.items(), key=lambda x: x[1][0], reverse=True)
    label_map = {}
    segment_names = ["Mahasiswa Berprestasi", "Mahasiswa Standar", "Mahasiswa Berisiko"]
    for idx, (c, means) in enumerate(sorted_clusters):
        label_map[c] = segment_names[idx]

    for c, means in sorted_clusters:
        count = np.sum(labels == c)
        print(f"{c:>7} | {label_map[c]:<22} | {count:>6} | {means[0]:>5.2f} | {means[1]:>11.1f} | {means[2]:>8.1f}% | {means[3]:>10.1f}")

    # Rekomendasi
    print(f"\n--- Rekomendasi ---")
    rekomendasi = {
        "Mahasiswa Berprestasi": "Pertahankan prestasi, arahkan ke riset/lomba",
        "Mahasiswa Standar": "Tingkatkan jam belajar dan kehadiran",
        "Mahasiswa Berisiko": "Perlu bimbingan intensif dan monitoring kehadiran",
    }
    for c, means in sorted_clusters:
        print(f"  {label_map[c]:<22}: {rekomendasi[label_map[c]]}")

    # Prediksi mahasiswa baru
    print(f"\n--- Prediksi Mahasiswa Baru ---")
    data_baru = np.array([
        [3.8, 20, 95, 8],
        [2.9, 10, 75, 4],
        [2.0, 3, 50, 1],
        [3.5, 16, 90, 7],
        [2.2, 5, 55, 2],
    ])
    data_baru_scaled = scaler.transform(data_baru)
    prediksi = kmeans.predict(data_baru_scaled)
    for i, (d, p) in enumerate(zip(data_baru, prediksi), 1):
        print(f"  Mahasiswa {i} (IPK={d[0]}, Jam={d[1]:.0f}, Hadir={d[2]:.0f}%, Org={d[3]:.0f}) -> {label_map[p]}")

    # Analisis:
    # Cluster terbentuk dengan baik (Silhouette > 0.4), memisahkan mahasiswa
    # ke dalam 3 kelompok berdasarkan perilaku akademik. Mahasiswa berisiko
    # perlu perhatian khusus dengan IPK rendah dan kehadiran di bawah 65%.
