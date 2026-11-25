# ======================================
# CLASS BUKU
# ======================================

class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku

        self._stok = stok

        self.__lokasi_rak = lokasi_rak

    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi_baru):
        self.__lokasi_rak = lokasi_baru

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= self._stok:
            self._stok -= jumlah


# ======================================
# CLASS ANGGOTA
# ======================================

class Anggota:
    def __init__(self, id_anggota, nama,
                 maks_pinjam=3,
                 status_aktif=True):

        self.id_anggota = id_anggota
        self.nama = nama

        self._maks_pinjam = maks_pinjam

        self.__status_aktif = status_aktif

        self.daftar_peminjaman = []

    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    def pinjam_buku(self, peminjaman):
        self.daftar_peminjaman.append(peminjaman)

    def kembalikan_buku(self, kode_buku):
        for p in self.daftar_peminjaman:
            if p.kode_buku == kode_buku:
                p.status = "Dikembalikan"


# ======================================
# CLASS PEMINJAMAN
# ======================================

class Peminjaman:
    def __init__(self,
                 kode_buku,
                 tanggal_pinjam,
                 tanggal_kembali,
                 status):

        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return (
            f"Kode Buku: {self.kode_buku}, "
            f"Tanggal Pinjam: {self.tanggal_pinjam}, "
            f"Tanggal Kembali: {self.tanggal_kembali}, "
            f"Status: {self.status}"
        )


# ======================================
# CONTOH ASSOCIATION
# ======================================

buku1 = Buku(
    "Python Dasar",
    "Andi",
    "B001",
    10,
    "Rak A1"
)

pinjam1 = Peminjaman(
    buku1.kode_buku,
    "01-12-2026",
    "08-12-2026",
    "Dipinjam"
)

print("Kode Buku:", pinjam1.kode_buku)


# ======================================
# TAMBAHAN METHOD
# ======================================

def pinjam_buku(self, peminjaman):
    self.daftar_peminjaman.append(peminjaman)


# ======================================
# CLASS PERPUSTAKAAN
# ======================================

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)


# ======================================
# INSTANSIASI
# ======================================

buku1 = Buku(
    "Python Dasar",
    "Andi",
    "B001",
    10,
    "Rak A1"
)

buku2 = Buku(
    "Pemrograman Web",
    "Budi",
    "B002",
    8,
    "Rak A2"
)

buku3 = Buku(
    "Basis Data",
    "Citra",
    "B003",
    5,
    "Rak B1"
)

print("3 buku berhasil dibuat")

anggota1 = Anggota("A001", "Rina")
anggota2 = Anggota("A002", "Doni")

print("2 anggota berhasil dibuat")

pinjam1 = Peminjaman(
    "B001",
    "01-12-2026",
    "08-12-2026",
    "Dipinjam"
)

pinjam2 = Peminjaman(
    "B002",
    "01-12-2026",
    "08-12-2026",
    "Dipinjam"
)

anggota1.pinjam_buku(pinjam1)
anggota1.pinjam_buku(pinjam2)

print(
    "Jumlah pinjaman anggota 1:",
    len(anggota1.daftar_peminjaman)
)

pinjam3 = Peminjaman(
    "B003",
    "02-12-2026",
    "09-12-2026",
    "Dipinjam"
)

anggota2.pinjam_buku(pinjam3)

print(
    "Jumlah pinjaman anggota 2:",
    len(anggota2.daftar_peminjaman)
)

anggota1.kembalikan_buku("B001")

for p in anggota1.daftar_peminjaman:
    print(
        p.kode_buku,
        "-",
        p.status
    )


# ======================================
# DEMONSTRASI OUTPUT
# ======================================

print("\n=== INFORMASI BUKU ===")

daftar_buku = [buku1, buku2, buku3]

for buku in daftar_buku:
    print("Judul :", buku.judul)
    print("Penulis :", buku.penulis)
    print("Kode Buku :", buku.kode_buku)
    print("Stok :", buku._stok)
    print("-" * 20)

print("\n=== INFORMASI ANGGOTA ===")

daftar_anggota = [anggota1, anggota2]

for anggota in daftar_anggota:
    print("ID Anggota :", anggota.id_anggota)
    print("Nama :", anggota.nama)
    print("Maks Pinjam :", anggota._maks_pinjam)
    print("Status Aktif :", anggota.get_status())
    print("-" * 20)

print("\n=== DAFTAR PEMINJAMAN ===")

for anggota in [anggota1, anggota2]:
    print(f"\nAnggota : {anggota.nama}")

    for p in anggota.daftar_peminjaman:
        print(
            p.kode_buku,
            "|",
            p.tanggal_pinjam,
            "|",
            p.tanggal_kembali,
            "|",
            p.status
        )
