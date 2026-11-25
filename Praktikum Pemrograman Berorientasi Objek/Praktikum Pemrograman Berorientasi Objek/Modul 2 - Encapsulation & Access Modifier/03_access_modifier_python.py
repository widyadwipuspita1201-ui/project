class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim          # public
        self.nama = nama        # public
        self._semester = semester   # protected
        self.__ipk = ipk        # private

    # Getter semester
    def get_semester(self):
        return self._semester

    # Setter semester
    def set_semester(self, semester_baru):
        if semester_baru < 1:
            raise ValueError("Semester harus lebih dari 0")
        self._semester = semester_baru

    # Getter IPK
    def get_ipk(self):
        return self.__ipk

    # Setter IPK
    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0")
        self.__ipk = ipk_baru


# b. Membuat 2 objek Mahasiswa

mhs1 = Mahasiswa("23001", "Budi", 3, 3.50)
mhs2 = Mahasiswa("23002", "Siti", 5, 3.80)

# Menampilkan data awal

print("=== Data Awal Mahasiswa ===")

print("\nMahasiswa 1")
print("NIM      :", mhs1.nim)
print("Nama     :", mhs1.nama)
print("Semester :", mhs1.get_semester())
print("IPK      :", mhs1.get_ipk())

print("\nMahasiswa 2")
print("NIM      :", mhs2.nim)
print("Nama     :", mhs2.nama)
print("Semester :", mhs2.get_semester())
print("IPK      :", mhs2.get_ipk())

# c. Mengubah semester dan IPK

mhs1.set_semester(4)
mhs1.set_ipk(3.75)

mhs2.set_semester(6)
mhs2.set_ipk(3.90)

# Menampilkan data setelah perubahan

print("\n=== Setelah Perubahan ===")

print("\nMahasiswa 1")
print("NIM      :", mhs1.nim)
print("Nama     :", mhs1.nama)
print("Semester :", mhs1.get_semester())
print("IPK      :", mhs1.get_ipk())

print("\nMahasiswa 2")
print("NIM      :", mhs2.nim)
print("Nama     :", mhs2.nama)
print("Semester :", mhs2.get_semester())
print("IPK      :", mhs2.get_ipk())
