"""
==========================================================
 TUGAS 4 - Class Bangun Ruang
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================
"""

import math


class BangunRuang:
    """Class dasar (abstract) untuk bangun ruang."""

    def __init__(self, nama):
        self.nama = nama

    def volume(self):
        raise NotImplementedError("Subclass harus mengimplementasikan volume()")

    def luas_permukaan(self):
        raise NotImplementedError("Subclass harus mengimplementasikan luas_permukaan()")

    def info(self):
        raise NotImplementedError("Subclass harus mengimplementasikan info()")

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __eq__(self, other):
        return abs(self.volume() - other.volume()) < 0.01

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __str__(self):
        return f"{self.nama} (V={self.volume():.2f})"


class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__("Kubus")
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

    def luas_permukaan(self):
        return 6 * self.sisi ** 2

    def info(self):
        return (f"Kubus [sisi={self.sisi}]\n"
                f"  Volume         : {self.volume():.2f}\n"
                f"  Luas Permukaan : {self.luas_permukaan():.2f}")

    @classmethod
    def dari_volume(cls, vol):
        sisi = vol ** (1/3)
        return cls(sisi)

    @staticmethod
    def is_valid(sisi):
        return isinstance(sisi, (int, float)) and sisi > 0


class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

    def luas_permukaan(self):
        p, l, t = self.panjang, self.lebar, self.tinggi
        return 2 * (p*l + p*t + l*t)

    def info(self):
        return (f"Balok [p={self.panjang}, l={self.lebar}, t={self.tinggi}]\n"
                f"  Volume         : {self.volume():.2f}\n"
                f"  Luas Permukaan : {self.luas_permukaan():.2f}")

    @classmethod
    def dari_kubus(cls, sisi):
        return cls(sisi, sisi, sisi)

    @staticmethod
    def is_valid(panjang, lebar, tinggi):
        return all(isinstance(d, (int, float)) and d > 0 for d in [panjang, lebar, tinggi])


class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__("Tabung")
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

    def luas_permukaan(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def info(self):
        return (f"Tabung [r={self.jari_jari}, t={self.tinggi}]\n"
                f"  Volume         : {self.volume():.2f}\n"
                f"  Luas Permukaan : {self.luas_permukaan():.2f}")

    @classmethod
    def dari_volume(cls, vol, tinggi):
        r = math.sqrt(vol / (math.pi * tinggi))
        return cls(r, tinggi)

    @staticmethod
    def is_valid(jari_jari, tinggi):
        return all(isinstance(d, (int, float)) and d > 0 for d in [jari_jari, tinggi])


class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__("Bola")
        self.jari_jari = jari_jari

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

    def luas_permukaan(self):
        return 4 * math.pi * self.jari_jari ** 2

    def info(self):
        return (f"Bola [r={self.jari_jari}]\n"
                f"  Volume         : {self.volume():.2f}\n"
                f"  Luas Permukaan : {self.luas_permukaan():.2f}")

    @classmethod
    def dari_volume(cls, vol):
        r = ((3 * vol) / (4 * math.pi)) ** (1/3)
        return cls(r)

    @staticmethod
    def is_valid(jari_jari):
        return isinstance(jari_jari, (int, float)) and jari_jari > 0


# -- Demonstrasi ---------------------------------------------------------------
if __name__ == "__main__":
    kubus = Kubus(5)
    balok = Balok(8, 4, 3)
    tabung = Tabung(7, 10)
    bola = Bola(6)

    print("=== INFO BANGUN RUANG ===")
    bangun_list = [kubus, balok, tabung, bola]
    for bangun in bangun_list:
        print(bangun.info())
        print()

    print("=== ALTERNATIVE CONSTRUCTOR (@classmethod) ===")
    kubus2 = Kubus.dari_volume(125)
    print(f"Kubus dari volume 125: sisi = {kubus2.sisi:.2f}")
    print(kubus2.info())

    tabung2 = Tabung.dari_volume(1000, 10)
    print(f"\nTabung dari volume 1000 (t=10): r = {tabung2.jari_jari:.2f}")
    print(tabung2.info())

    print("\n=== VALIDASI (@staticmethod) ===")
    print(f"Kubus.is_valid(5)   = {Kubus.is_valid(5)}")
    print(f"Kubus.is_valid(-3)  = {Kubus.is_valid(-3)}")
    print(f"Kubus.is_valid('a') = {Kubus.is_valid('a')}")
    print(f"Tabung.is_valid(7, 10) = {Tabung.is_valid(7, 10)}")
    print(f"Tabung.is_valid(-1, 5) = {Tabung.is_valid(-1, 5)}")

    print("\n=== OPERATOR OVERLOADING ===")
    print(f"{kubus} > {balok}  ? {kubus > balok}")
    print(f"{tabung} > {bola}  ? {tabung > bola}")
    print(f"{kubus} == {kubus2} ? {kubus == kubus2}")
    print(f"{kubus} < {bola}   ? {kubus < bola}")

    print("\n=== URUTAN BERDASARKAN VOLUME ===")
    urut_volume = sorted(bangun_list, key=lambda b: b.volume())
    print("Kecil -> Besar:")
    for i, b in enumerate(urut_volume, 1):
        print(f"  {i}. {b.nama:<8} -> Volume: {b.volume():>10.2f}")

    print("\nBesar -> Kecil:")
    urut_desc = sorted(bangun_list, key=lambda b: b.volume(), reverse=True)
    for i, b in enumerate(urut_desc, 1):
        print(f"  {i}. {b.nama:<8} -> Volume: {b.volume():>10.2f}")

    print("\n=== TEST ABSTRACT (NotImplementedError) ===")
    try:
        br = BangunRuang("Test")
        br.volume()
    except NotImplementedError as e:
        print(f"Error: {e}")
