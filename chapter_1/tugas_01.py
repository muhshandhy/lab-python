"""
==========================================================
 TUGAS 1 - Biodata Mahasiswa
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Instruksi:
 1. Buat variabel yang menyimpan: nama lengkap, NIM, jurusan,
    semester (int), IPK (float), dan status aktif (bool)
 2. Tampilkan semua data menggunakan f-string dengan format rapi
 3. Tampilkan tipe data dari setiap variabel menggunakan type()
 4. Gunakan isinstance() untuk memeriksa apakah NIM bertipe str
    dan semester bertipe int
==========================================================
"""

# -- Deklarasi Variabel -------------------------------------------------------
nama_lengkap = "MUH NUR SANDI"
nim = "105841106721"
jurusan = "Informatika"
semester = 4
ipk = 3.75
status_aktif = True


# -- Tampilkan Biodata --------------------------------------------------------
print("===== BIODATA MAHASISWA =====")
print(f"Nama    : {nama_lengkap}")
print(f"NIM     : {nim}")
print(f"Jurusan : {jurusan}")
print(f"Semester: {semester}")
print(f"IPK     : {ipk}")
print(f"Aktif   : {status_aktif}")
print("=============================")


# -- Tampilkan Tipe Data ------------------------------------------------------
print(f"Tipe 'nama'    : {type(nama_lengkap)}")
print(f"Tipe 'nim'     : {type(nim)}")
print(f"Tipe 'jurusan' : {type(jurusan)}")
print(f"Tipe 'semester': {type(semester)}")
print(f"Tipe 'ipk'     : {type(ipk)}")
print(f"Tipe 'aktif'   : {type(status_aktif)}")


# -- Pemeriksaan isinstance() -------------------------------------------------
print(f"\nNIM adalah str?      {isinstance(nim, str)}")
print(f"Semester adalah int? {isinstance(semester, int)}")
