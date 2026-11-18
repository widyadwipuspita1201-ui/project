class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} dengan NIDN {self.nidn} mengajar mata kuliah {mata_kuliah}"

# Instansiasi 2 object dosen
dosen1 = Dosen("Andi Wijaya", "12345678")
dosen2 = Dosen("Rina Kusuma", "87654321")

# Memanggil method
print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Struktur Data"))
