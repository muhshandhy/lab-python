"""
==========================================================
 TUGAS 2 - Sistem Akademik dengan Inheritance
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""


class Orang:
    """Class dasar untuk merepresentasikan seseorang."""

    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}"

    def __str__(self):
        return self.nama


class Mahasiswa(Orang):
    """Representasi mahasiswa, turunan dari Orang."""

    BOBOT_NILAI = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}

    def __init__(self, nama, umur, alamat, nim, jurusan, semester):
        super().__init__(nama, umur, alamat)
        self.nim = nim
        self.jurusan = jurusan
        self.semester = semester
        self.daftar_mk = []

    def tambah_mk(self, nama_mk, sks, nilai):
        self.daftar_mk.append({"nama": nama_mk, "sks": sks, "nilai": nilai})

    def hitung_ipk(self):
        if not self.daftar_mk:
            return 0.0
        total_bobot = sum(
            self.BOBOT_NILAI.get(mk["nilai"], 0) * mk["sks"]
            for mk in self.daftar_mk
        )
        total_sks = sum(mk["sks"] for mk in self.daftar_mk)
        return total_bobot / total_sks if total_sks > 0 else 0.0

    def info(self):
        base = super().info()
        return f"{base}\n  NIM: {self.nim}, Jurusan: {self.jurusan}, Semester: {self.semester}, IPK: {self.hitung_ipk():.2f}"


class Dosen(Orang):
    """Representasi dosen, turunan dari Orang."""

    def __init__(self, nama, umur, alamat, nidn, bidang_keahlian):
        super().__init__(nama, umur, alamat)
        self.nidn = nidn
        self.bidang_keahlian = bidang_keahlian
        self.daftar_mk_diampu = []

    def tambah_mk_diampu(self, nama_mk):
        self.daftar_mk_diampu.append(nama_mk)

    def info(self):
        base = super().info()
        mk = ", ".join(self.daftar_mk_diampu) if self.daftar_mk_diampu else "-"
        return f"{base}\n  NIDN: {self.nidn}, Bidang: {self.bidang_keahlian}\n  MK Diampu: {mk}"


class Asisten(Mahasiswa):
    """Representasi asisten laboratorium, turunan dari Mahasiswa."""

    def __init__(self, nama, umur, alamat, nim, jurusan, semester, lab, dosen_pembimbing):
        super().__init__(nama, umur, alamat, nim, jurusan, semester)
        self.lab = lab
        self.dosen_pembimbing = dosen_pembimbing

    def info(self):
        base = super().info()
        return f"{base}\n  Lab: {self.lab}, Dosen Pembimbing: {self.dosen_pembimbing}"


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    dosen1 = Dosen("Dr. Ahmad", 45, "Makassar", "001122", "Machine Learning")
    dosen1.tambah_mk_diampu("Kecerdasan Buatan")
    dosen1.tambah_mk_diampu("Data Mining")

    mhs1 = Mahasiswa("Siti Aisyah", 20, "Makassar", "105841100123", "Informatika", 5)
    mhs1.tambah_mk("Kalkulus", 3, "A")
    mhs1.tambah_mk("Pemrograman Dasar", 4, "A")
    mhs1.tambah_mk("Basis Data", 3, "B")

    mhs2 = Mahasiswa("Budi Santoso", 21, "Gowa", "105841100456", "Informatika", 5)
    mhs2.tambah_mk("Kalkulus", 3, "B")
    mhs2.tambah_mk("Pemrograman Dasar", 4, "A")
    mhs2.tambah_mk("Basis Data", 3, "C")

    asisten1 = Asisten("Dewi Lestari", 22, "Makassar", "105841100789",
                       "Informatika", 7, "Lab AI", "Dr. Ahmad")
    asisten1.tambah_mk("Kecerdasan Buatan", 3, "A")
    asisten1.tambah_mk("Machine Learning", 3, "A")

    # Polymorphism
    print("=== POLYMORPHISM ===")
    semua_orang = [dosen1, mhs1, mhs2, asisten1]
    for orang in semua_orang:
        print(f"\n[{type(orang).__name__}]")
        print(orang.info())
        print("-" * 50)

    # isinstance()
    print("\n=== ISINSTANCE ===")
    for orang in semua_orang:
        print(f"{orang.nama}:")
        print(f"  isinstance(Orang)     = {isinstance(orang, Orang)}")
        print(f"  isinstance(Mahasiswa) = {isinstance(orang, Mahasiswa)}")
        print(f"  isinstance(Dosen)     = {isinstance(orang, Dosen)}")
        print(f"  isinstance(Asisten)   = {isinstance(orang, Asisten)}")

    # issubclass()
    print("\n=== ISSUBCLASS ===")
    print(f"Mahasiswa subclass Orang?  {issubclass(Mahasiswa, Orang)}")
    print(f"Dosen subclass Orang?      {issubclass(Dosen, Orang)}")
    print(f"Asisten subclass Mahasiswa? {issubclass(Asisten, Mahasiswa)}")
    print(f"Asisten subclass Orang?    {issubclass(Asisten, Orang)}")
    print(f"Dosen subclass Mahasiswa?  {issubclass(Dosen, Mahasiswa)}")

    # MRO
    print("\n=== MRO ===")
    print(f"Asisten MRO: {[c.__name__ for c in Asisten.__mro__]}")
