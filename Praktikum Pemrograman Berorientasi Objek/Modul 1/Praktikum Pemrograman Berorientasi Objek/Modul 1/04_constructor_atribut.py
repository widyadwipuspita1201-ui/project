class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk}, warna {self.warna}, tahun {self.tahun}"


# Instansiasi object
kendaraan1 = Kendaraan("Toyota", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda", "Putih", 2023)

# Menampilkan instance attribute
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())

# Menampilkan class attribute
print(f"Bahan bakar kendaraan1: {kendaraan1.bahan_bakar}")
print(f"Bahan bakar kendaraan2: {kendaraan2.bahan_bakar}")

# Akses class attribute melalui class
print(f"Bahan bakar umum: {Kendaraan.bahan_bakar}")
