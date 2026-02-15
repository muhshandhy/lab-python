"""
==========================================================
 TUGAS 3 - Sistem Keuangan dengan Encapsulation
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

from datetime import datetime


class Rekening:
    """Rekening bank dengan encapsulation."""

    def __init__(self, nomor_rekening, pemilik, pin, saldo_awal=0, bank="Bank Unismuh"):
        # Public
        self.bank = bank
        # Protected
        self._nomor_rekening = nomor_rekening
        self._pemilik = pemilik
        # Private
        self.__saldo = saldo_awal
        self.__pin = pin
        self.__riwayat_transaksi = []
        self.__catat_transaksi("SALDO AWAL", saldo_awal)

    @property
    def saldo(self):
        """Getter untuk saldo (read-only)."""
        return self.__saldo

    @property
    def pemilik(self):
        """Getter untuk nama pemilik."""
        return self._pemilik

    @pemilik.setter
    def pemilik(self, nama_baru):
        """Setter untuk nama pemilik dengan validasi."""
        if not nama_baru or len(nama_baru) < 3:
            raise ValueError("Nama harus minimal 3 karakter")
        self._pemilik = nama_baru

    def __verifikasi_pin(self, pin):
        return pin == self.__pin

    def __catat_transaksi(self, jenis, jumlah, keterangan=""):
        self.__riwayat_transaksi.append({
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "jenis": jenis,
            "jumlah": jumlah,
            "keterangan": keterangan,
            "saldo_setelah": self.__saldo,
        })

    def setor(self, jumlah, pin):
        if not self.__verifikasi_pin(pin):
            return "PIN salah!"
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0!"
        self.__saldo += jumlah
        self.__catat_transaksi("SETOR", jumlah)
        return f"Setor Rp{jumlah:,.0f} berhasil! Saldo: Rp{self.__saldo:,.0f}"

    def tarik(self, jumlah, pin):
        if not self.__verifikasi_pin(pin):
            return "PIN salah!"
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0!"
        if jumlah > self.__saldo:
            return f"Saldo tidak cukup! Saldo: Rp{self.__saldo:,.0f}"
        self.__saldo -= jumlah
        self.__catat_transaksi("TARIK", jumlah)
        return f"Tarik Rp{jumlah:,.0f} berhasil! Saldo: Rp{self.__saldo:,.0f}"

    def transfer(self, tujuan, jumlah, pin):
        if not self.__verifikasi_pin(pin):
            return "PIN salah!"
        if jumlah <= 0:
            return "Jumlah harus lebih dari 0!"
        if jumlah > self.__saldo:
            return f"Saldo tidak cukup! Saldo: Rp{self.__saldo:,.0f}"
        self.__saldo -= jumlah
        tujuan._Rekening__saldo += jumlah
        self.__catat_transaksi("TRANSFER", jumlah, f"ke {tujuan._nomor_rekening}")
        tujuan._Rekening__riwayat_transaksi.append({
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "jenis": "TERIMA TRANSFER",
            "jumlah": jumlah,
            "keterangan": f"dari {self._nomor_rekening}",
            "saldo_setelah": tujuan._Rekening__saldo,
        })
        return f"Transfer Rp{jumlah:,.0f} ke {tujuan._nomor_rekening} berhasil!"

    def cek_riwayat(self, pin):
        if not self.__verifikasi_pin(pin):
            return "PIN salah!"
        print(f"\n--- Riwayat Transaksi {self._nomor_rekening} ---")
        for t in self.__riwayat_transaksi:
            ket = f" ({t['keterangan']})" if t['keterangan'] else ""
            print(f"  [{t['waktu']}] {t['jenis']:<15} Rp{t['jumlah']:>12,.0f}{ket} | Saldo: Rp{t['saldo_setelah']:,.0f}")
        return ""

    def ganti_pin(self, pin_lama, pin_baru):
        if not self.__verifikasi_pin(pin_lama):
            return "PIN lama salah!"
        if len(pin_baru) != 6 or not pin_baru.isdigit():
            return "PIN baru harus 6 digit angka!"
        self.__pin = pin_baru
        return "PIN berhasil diganti."

    def __str__(self):
        return f"[{self.bank}] {self._nomor_rekening} - {self._pemilik} (Saldo: Rp{self.__saldo:,.0f})"


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    rek1 = Rekening("REK-0001", "Ahmad Dahlan", "123456", 5_000_000)
    rek2 = Rekening("REK-0002", "Siti Rahmah", "654321", 3_000_000)

    print("=== INFO REKENING ===")
    print(rek1)
    print(rek2)

    print("\n=== SETOR ===")
    print(rek1.setor(2_000_000, "123456"))

    print("\n=== TARIK ===")
    print(rek1.tarik(500_000, "123456"))

    print("\n=== TRANSFER ===")
    print(rek1.transfer(rek2, 1_000_000, "123456"))

    print("\n=== CEK SALDO (property) ===")
    print(f"Saldo Ahmad: Rp{rek1.saldo:,.0f}")
    print(f"Saldo Siti : Rp{rek2.saldo:,.0f}")

    print("\n=== TEST AKSES PRIVATE ===")
    try:
        rek1.saldo = 999_999_999
    except AttributeError as e:
        print(f"Error saldo: {e}")

    try:
        print(rek1.__saldo)
    except AttributeError as e:
        print(f"Error __saldo: {e}")

    print(f"Name mangling: rek1._Rekening__saldo = {rek1._Rekening__saldo}")

    print("\n=== TEST PROPERTY SETTER ===")
    rek1.pemilik = "Ahmad Dahlan Syamsuddin"
    print(f"Pemilik baru: {rek1.pemilik}")
    try:
        rek1.pemilik = "AB"
    except ValueError as e:
        print(f"Error setter: {e}")

    print("\n=== RIWAYAT TRANSAKSI ===")
    rek1.cek_riwayat("123456")

    print("\n=== GANTI PIN ===")
    print(rek1.ganti_pin("123456", "111111"))
    print(rek1.ganti_pin("111111", "abc"))
