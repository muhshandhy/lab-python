"""
==========================================================
 TUGAS 4 - Permainan Tebak Angka
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
 Nama: MUH NUR SANDI
 NIM : 105841106721
==========================================================

 Catatan: Tugas ini interaktif (menggunakan input()).
          Sertakan screenshot saat menjalankan program.
==========================================================
"""

import random


def generate_angka(batas_bawah=1, batas_atas=100):
    """Generate angka acak dalam rentang tertentu."""
    return random.randint(batas_bawah, batas_atas)


def main_tebak_angka():
    """Permainan tebak angka dengan while loop."""
    target = generate_angka()
    maks_percobaan = 10

    print("=== PERMAINAN TEBAK ANGKA ===")
    print(f"Tebak angka antara 1 sampai 100 (maksimal {maks_percobaan} percobaan)")

    for percobaan in range(1, maks_percobaan + 1):
        try:
            tebakan = int(input(f"Percobaan {percobaan}: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if tebakan == target:
            print(f"BENAR! Angkanya adalah {target}")
            print(f"Anda berhasil dalam {percobaan} percobaan!")
            break
        elif tebakan > target:
            print("Terlalu besar!")
        else:
            print("Terlalu kecil!")
    else:
        print(f"\nGame Over! Angka yang benar adalah {target}")


def tebak_rekursif(target, percobaan=1, maks=10):
    """Versi rekursif dari permainan tebak angka."""
    if percobaan > maks:
        print(f"\nGame Over! Angka yang benar adalah {target}")
        return

    try:
        tebakan = int(input(f"Percobaan {percobaan}: "))
    except ValueError:
        print("Masukkan angka yang valid!")
        tebak_rekursif(target, percobaan, maks)
        return

    if tebakan == target:
        print(f"BENAR! Angkanya adalah {target}")
        print(f"Anda berhasil dalam {percobaan} percobaan!")
    elif tebakan > target:
        print("Terlalu besar!")
        tebak_rekursif(target, percobaan + 1, maks)
    else:
        print("Terlalu kecil!")
        tebak_rekursif(target, percobaan + 1, maks)


# -- Main Program -------------------------------------------------------------
if __name__ == "__main__":
    print("=== VERSI ITERATIF (while loop) ===")
    main_tebak_angka()

    print("\n=== VERSI REKURSIF ===")
    target = generate_angka()
    print(f"Tebak angka antara 1 sampai 100 (maksimal 10 percobaan)")
    tebak_rekursif(target)
