class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori:
            self.inventori[nama_barang] += jumlah
        else:
            self.inventori[nama_barang] = jumlah
        return f"{jumlah} {nama_barang} berhasil ditambahkan."

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori and self.inventori[nama_barang] >= jumlah:
            self.inventori[nama_barang] -= jumlah
            return f"{jumlah} {nama_barang} berhasil dikurangi."
        return "Stok tidak mencukupi atau barang tidak ditemukan."

    def lihat_inventori(self):
        return self.inventori


inventori = ManajerInventori()

print(inventori.tambah_barang("Laptop", 10))
print(inventori.tambah_barang("Mouse", 20))
print(inventori.hapus_barang("Laptop", 3))

print("Inventori saat ini:")
print(inventori.lihat_inventori())
