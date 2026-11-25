# relasi aggregation dan composition

class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []  # agregasi

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # f. Method rata-rata
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []  # agregasi

    def tambah_matakuliah(self, mk):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# fungsi report_program
def report_program(prodi, daftar_mahasiswa):
    print(f"\nProgram Studi: {prodi.nama}")

    print("Mata Kuliah:")
    for mk in prodi.daftar_matakuliah:
        print(f"- {mk.kode} : {mk.nama}")

    print("Mahasiswa dan Nilai:")

    for m in daftar_mahasiswa:
        nilai_relevan = [
            n.skor
            for n in m.daftar_nilai
            if any(n.kode_mk == mk.kode
                   for mk in prodi.daftar_matakuliah)
        ]

        if nilai_relevan:
            rata2 = sum(nilai_relevan) / len(nilai_relevan)
            print(f"{m.nim} - {m.nama} : {round(rata2, 2)}")


# ==================================================
# a. Tambahkan 2 Program Studi baru
# ==================================================

uni = Universitas("Universitas A")

prodi_ti = uni.buat_program("Teknik Informatika")
prodi_si = uni.buat_program("Sistem Informasi")
prodi_mi = uni.buat_program("Manajemen Informatika")

# ==================================================
# b. Tambahkan minimal 2 Mata Kuliah
# ==================================================

# Teknik Informatika
prodi_ti.tambah_matakuliah(
    MataKuliah("TI101", "Pemrograman Dasar")
)

prodi_ti.tambah_matakuliah(
    MataKuliah("TI102", "Struktur Data")
)

# Sistem Informasi
prodi_si.tambah_matakuliah(
    MataKuliah("SI101", "Sistem Informasi Manajemen")
)

prodi_si.tambah_matakuliah(
    MataKuliah("SI102", "Basis Data")
)

# Manajemen Informatika
prodi_mi.tambah_matakuliah(
    MataKuliah("MI101", "Aplikasi Perkantoran")
)

prodi_mi.tambah_matakuliah(
    MataKuliah("MI102", "Jaringan Komputer")
)

# ==================================================
# c. Buat 3 Mahasiswa lalu tambahkan beberapa nilai
# ==================================================

m1 = Mahasiswa("23001", "Budi")
m2 = Mahasiswa("23002", "Siti")
m3 = Mahasiswa("23003", "Andi")

m1.tambah_nilai(Nilai("TI101", 85))
m1.tambah_nilai(Nilai("TI102", 78))

m2.tambah_nilai(Nilai("TI101", 90))
m2.tambah_nilai(Nilai("SI101", 88))

m3.tambah_nilai(Nilai("MI101", 80))
m3.tambah_nilai(Nilai("MI102", 92))

# ==================================================
# Menampilkan hasil poin a, b, c
# ==================================================

print("Universitas :", uni.nama)

for prodi in uni.programs:
    print(f"\nProgram Studi : {prodi.nama}")

    print("Daftar Mata Kuliah:")

    for mk in prodi.daftar_matakuliah:
        print(f"- {mk.kode} : {mk.nama}")

print("\n=== Data Mahasiswa dan Nilai ===")

for m in [m1, m2, m3]:
    print(f"\n{m.nim} - {m.nama}")

    for n in m.daftar_nilai:
        print(f"- {n.kode_mk} : {n.skor}")

# ==================================================
# d. Tampilkan daftar mata kuliah tiap Program Studi
# ==================================================

print("\n=== DAFTAR MATA KULIAH SETIAP PROGRAM STUDI ===")

for prodi in uni.programs:
    print(f"\nProgram Studi: {prodi.nama}")

    for mk in prodi.daftar_matakuliah:
        print(f"- {mk.kode} : {mk.nama}")

# ==================================================
# e. Tampilkan daftar nilai setiap mahasiswa
# ==================================================

print("\n=== DAFTAR NILAI SETIAP MAHASISWA ===")

for m in [m1, m2, m3]:
    print(f"\nNIM : {m.nim}")
    print(f"Nama: {m.nama}")

    for nilai in m.daftar_nilai:
        print(f"- {nilai.kode_mk} : {nilai.skor}")

# ==================================================
# f. Tampilkan rata-rata nilai setiap mahasiswa
# ==================================================

print("\n=== RATA-RATA NILAI MAHASISWA ===")

for m in [m1, m2, m3]:
    print(f"{m.nim} - {m.nama} : {round(m.rata_rata(), 2)}")

# ==================================================
# g. Panggil report_program()
# ==================================================

print("\n=== LAPORAN PROGRAM STUDI ===")

report_program(prodi_ti, [m1, m2, m3])
report_program(prodi_si, [m1, m2, m3])
report_program(prodi_mi, [m1, m2, m3])
