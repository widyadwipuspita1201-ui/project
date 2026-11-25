class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.mahasiswa = []

    def tambah_mahasiswa(self, mhs):
        self.mahasiswa.append(mhs)

    def daftar_mahasiswa(self):
        return [m.nama for m in self.mahasiswa]

    # a. Method baru
    def jumlah_mahasiswa(self):
        return len(self.mahasiswa)


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


# b. Buat 2 mata kuliah
mk1 = MataKuliah("TI101", "Pemrograman Dasar")
mk2 = MataKuliah("TI102", "Algoritma dan Struktur Data")

# b. Buat 3 mahasiswa
m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

# b. Daftarkan mahasiswa
mk1.tambah_mahasiswa(m1)
mk1.tambah_mahasiswa(m2)

mk2.tambah_mahasiswa(m2)
mk2.tambah_mahasiswa(m3)

# c. Tampilkan daftar mahasiswa dan jumlahnya

print("=== Mata Kuliah 1 ===")
print("Kode MK :", mk1.kode)
print("Nama MK :", mk1.nama)
print("Daftar Mahasiswa :", mk1.daftar_mahasiswa())
print("Jumlah Mahasiswa :", mk1.jumlah_mahasiswa())

print()

print("=== Mata Kuliah 2 ===")
print("Kode MK :", mk2.kode)
print("Nama MK :", mk2.nama)
print("Daftar Mahasiswa :", mk2.daftar_mahasiswa())
print("Jumlah Mahasiswa :", mk2.jumlah_mahasiswa())
