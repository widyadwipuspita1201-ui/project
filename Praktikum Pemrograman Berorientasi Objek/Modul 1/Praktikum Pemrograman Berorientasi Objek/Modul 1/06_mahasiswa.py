class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        return f"Halo, nama saya {self.nama}, NIM {self.nim}, jurusan {self.jurusan}, IPK {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}"

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum Memenuhi Syarat"


# Instansiasi 3 object mahasiswa
mhs1 = Mahasiswa("Andi", "220001", "Informatika", 3.8)
mhs2 = Mahasiswa("Budi", "220002", "Sistem Informasi", 3.2)
mhs3 = Mahasiswa("Citra", "220003", "Teknik Komputer", 2.7)

# Demonstrasi method perkenalan_diri()
print(mhs1.perkenalan_diri())
print(mhs2.perkenalan_diri())
print(mhs3.perkenalan_diri())

print()

# Demonstrasi method update_ipk()
print(mhs3.update_ipk(3.1))

print()

# Demonstrasi method predikat_kelulusan()
print(f"{mhs1.nama}: {mhs1.predikat_kelulusan()}")
print(f"{mhs2.nama}: {mhs2.predikat_kelulusan()}")
print(f"{mhs3.nama}: {mhs3.predikat_kelulusan()}")

print()

# Demonstrasi class attribute
print("Universitas:", Mahasiswa.universitas)
