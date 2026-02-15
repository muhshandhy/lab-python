"""
==========================================================
 TUGAS 1 - Sistem Perpustakaan
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""


class Buku:
    """Representasi sebuah buku di perpustakaan."""

    def __init__(self, judul, penulis, tahun, isbn):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.isbn = isbn
        self.tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} ({self.tahun}) [{status}]"

    def __repr__(self):
        return f"Buku('{self.judul}', '{self.penulis}', {self.tahun}, '{self.isbn}')"


class Perpustakaan:
    """Sistem manajemen perpustakaan sederhana."""

    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        for b in self.daftar_buku:
            if b.isbn == buku.isbn:
                print(f"Buku dengan ISBN {buku.isbn} sudah ada!")
                return
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan.")

    def cari_buku(self, kata_kunci):
        return [
            b for b in self.daftar_buku
            if kata_kunci.lower() in b.judul.lower()
            or kata_kunci.lower() in b.penulis.lower()
        ]

    def pinjam_buku(self, isbn):
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                if buku.tersedia:
                    buku.tersedia = False
                    return f"Buku '{buku.judul}' berhasil dipinjam."
                else:
                    return f"Buku '{buku.judul}' sedang dipinjam."
        return f"Buku dengan ISBN {isbn} tidak ditemukan."

    def kembalikan_buku(self, isbn):
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                if not buku.tersedia:
                    buku.tersedia = True
                    return f"Buku '{buku.judul}' berhasil dikembalikan."
                else:
                    return f"Buku '{buku.judul}' tidak sedang dipinjam."
        return f"Buku dengan ISBN {isbn} tidak ditemukan."

    def tampilkan_semua(self):
        print(f"\n{'=' * 70}")
        print(f" {self.nama}")
        print(f"{'=' * 70}")
        print(f"{'No':>2} | {'Judul':<25} | {'Penulis':<18} | {'Tahun':>5} | {'Status'}")
        print("-" * 70)
        for i, b in enumerate(self.daftar_buku, 1):
            status = "Tersedia" if b.tersedia else "Dipinjam"
            print(f"{i:>2} | {b.judul:<25} | {b.penulis:<18} | {b.tahun:>5} | {status}")
        print("=" * 70)
        tersedia = sum(1 for b in self.daftar_buku if b.tersedia)
        dipinjam = len(self.daftar_buku) - tersedia
        print(f"Total: {len(self.daftar_buku)} buku | Tersedia: {tersedia} | Dipinjam: {dipinjam}")


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    buku1 = Buku("Python Dasar", "Guido van Rossum", 2023, "978-001")
    buku2 = Buku("Data Science", "Jake VanderPlas", 2022, "978-002")
    buku3 = Buku("Machine Learning", "Andrew Ng", 2021, "978-003")
    buku4 = Buku("Algoritma Pemrograman", "Thomas Cormen", 2020, "978-004")
    buku5 = Buku("Artificial Intelligence", "Stuart Russell", 2019, "978-005")

    perpus = Perpustakaan("Perpustakaan Unismuh Makassar")

    for buku in [buku1, buku2, buku3, buku4, buku5]:
        perpus.tambah_buku(buku)

    print("\n=== DAFTAR BUKU ===")
    perpus.tampilkan_semua()

    print("\n=== CARI BUKU: 'python' ===")
    hasil = perpus.cari_buku("python")
    for buku in hasil:
        print(f"  - {buku}")

    print("\n=== PINJAM BUKU ===")
    print(perpus.pinjam_buku("978-001"))
    print(perpus.pinjam_buku("978-003"))
    print(perpus.pinjam_buku("978-001"))

    print("\n=== DAFTAR BUKU (setelah peminjaman) ===")
    perpus.tampilkan_semua()

    print("\n=== KEMBALIKAN BUKU ===")
    print(perpus.kembalikan_buku("978-001"))

    print("\n=== REPR ===")
    print(repr(buku1))
