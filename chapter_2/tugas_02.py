"""
==========================================================
 TUGAS 2 - Sistem Data Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Instruksi:
 1. Buat dictionary berisi data 5 mahasiswa, setiap mahasiswa
    memiliki: nama, nim, jurusan, dan nilai (dict mata kuliah)
 2. Tampilkan seluruh data mahasiswa dalam format tabel rapi
 3. Hitung rata-rata nilai setiap mahasiswa
 4. Cari mahasiswa dengan rata-rata tertinggi
 5. Tambahkan 1 mahasiswa baru ke dictionary
 6. Gunakan dict comprehension untuk {nama: rata_rata_nilai}
==========================================================
"""

# -- Data Mahasiswa ------------------------------------------------------------
mahasiswa = {
    "MHS001": {
        "nama": "Ahmad Fauzi",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
    },
    "MHS002": {
        "nama": "Siti Nurhaliza",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 92, "Basis Data": 88, "Jaringan": 95}
    },
    "MHS003": {
        "nama": "Budi Santoso",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 70, "Basis Data": 75, "Jaringan": 68}
    },
    "MHS004": {
        "nama": "Dewi Lestari",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 88, "Basis Data": 82, "Jaringan": 90}
    },
    "MHS005": {
        "nama": "Rizky Pratama",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 76, "Basis Data": 80, "Jaringan": 72}
    },
}


# -- Tampilkan Data dalam Format Tabel -----------------------------------------
print("===== SISTEM DATA MAHASISWA =====")
print(f"{'NIM':<8} | {'Nama':<18} | {'Jurusan':<18} | {'Algoritma':>9} | {'Basis Data':>10} | {'Jaringan':>8}")
print("-" * 85)

for nim, data in mahasiswa.items():
    n = data["nilai"]
    print(f"{nim:<8} | {data['nama']:<18} | {data['jurusan']:<18} | {n['Algoritma']:>9} | {n['Basis Data']:>10} | {n['Jaringan']:>8}")

print("-" * 85)


# -- Hitung Rata-rata Nilai Setiap Mahasiswa -----------------------------------
print("\n===== RATA-RATA NILAI =====")
for nim, data in mahasiswa.items():
    rata = sum(data["nilai"].values()) / len(data["nilai"])
    print(f"{data['nama']:<18} : {rata:.2f}")


# -- Cari Mahasiswa dengan Rata-rata Tertinggi ---------------------------------
print("\n===== MAHASISWA TERBAIK =====")
nim_terbaik = None
rata_tertinggi = 0

for nim, data in mahasiswa.items():
    rata = sum(data["nilai"].values()) / len(data["nilai"])
    if rata > rata_tertinggi:
        rata_tertinggi = rata
        nim_terbaik = nim

data_terbaik = mahasiswa[nim_terbaik]
print(f"Nama    : {data_terbaik['nama']}")
print(f"NIM     : {nim_terbaik}")
print(f"Jurusan : {data_terbaik['jurusan']}")
print(f"Rata-rata: {rata_tertinggi:.2f}")


# -- Tambahkan Mahasiswa Baru -------------------------------------------------
mahasiswa["MHS006"] = {
    "nama": "Andi Wijaya",
    "jurusan": "Informatika",
    "nilai": {"Algoritma": 80, "Basis Data": 85, "Jaringan": 82}
}
print(f"\n===== MAHASISWA BARU DITAMBAHKAN =====")
print(f"NIM     : MHS006")
print(f"Nama    : {mahasiswa['MHS006']['nama']}")
print(f"Jurusan : {mahasiswa['MHS006']['jurusan']}")
print(f"Nilai   : {mahasiswa['MHS006']['nilai']}")


# -- Dictionary Comprehension -------------------------------------------------
print("\n===== RINGKASAN (Dict Comprehension) =====")
ringkasan = {
    data["nama"]: round(sum(data["nilai"].values()) / len(data["nilai"]), 2)
    for nim, data in mahasiswa.items()
}

for nama, rata in ringkasan.items():
    print(f"{nama:<18} : {rata}")
