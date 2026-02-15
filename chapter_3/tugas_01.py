"""
==========================================================
 TUGAS 1 - Sistem Penilaian Akademik
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""


def hitung_grade(nilai):
    """Menentukan grade berdasarkan nilai angka (0-100).

    Args:
        nilai (int): Nilai angka mahasiswa (0-100).

    Returns:
        tuple: (grade, keterangan)
    """
    if nilai >= 90:
        return ("A", "Sangat Baik")
    elif nilai >= 80:
        return ("B", "Baik")
    elif nilai >= 70:
        return ("C", "Cukup")
    elif nilai >= 60:
        return ("D", "Kurang")
    else:
        return ("E", "Sangat Kurang")


def status_kelulusan(grade):
    """Menentukan status kelulusan berdasarkan grade.

    Args:
        grade (str): Grade mahasiswa (A/B/C/D/E).

    Returns:
        str: "LULUS" jika A/B/C, "TIDAK LULUS" jika D/E.
    """
    return "LULUS" if grade in ("A", "B", "C") else "TIDAK LULUS"


# -- Data Mahasiswa ------------------------------------------------------------
data_mahasiswa = [
    ("Ahmad Fauzi", 85),
    ("Siti Rahma", 92),
    ("Budi Santoso", 55),
    ("Dewi Lestari", 78),
    ("Rizky Pratama", 60),
    ("Andi Wijaya", 90),
    ("Nur Aisyah", 73),
    ("Fajar Hidayat", 45),
    ("Mega Putri", 88),
    ("Hasan Basri", 67),
]


# -- Proses & Tampilkan -------------------------------------------------------
print("=" * 75)
print(" HASIL PENILAIAN AKADEMIK")
print("=" * 75)
print(f"{'No':>2} | {'Nama':<18} | {'Nilai':>5} | {'Grade':>5} | {'Keterangan':<14} | {'Status'}")
print("-" * 75)

jumlah_lulus = 0

for i, (nama, nilai) in enumerate(data_mahasiswa, 1):
    grade, keterangan = hitung_grade(nilai)
    status = status_kelulusan(grade)
    if status == "LULUS":
        jumlah_lulus += 1
    print(f"{i:>2} | {nama:<18} | {nilai:>5} | {grade:>5} | {keterangan:<14} | {status}")

print("=" * 75)

# -- Statistik -----------------------------------------------------------------
jumlah_tidak_lulus = len(data_mahasiswa) - jumlah_lulus
persen_lulus = jumlah_lulus / len(data_mahasiswa) * 100
persen_tidak_lulus = jumlah_tidak_lulus / len(data_mahasiswa) * 100

print(f"Lulus: {jumlah_lulus} ({persen_lulus:.1f}%) | Tidak Lulus: {jumlah_tidak_lulus} ({persen_tidak_lulus:.1f}%)")
