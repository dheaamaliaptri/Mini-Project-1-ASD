import os
from prettytable import PrettyTable


class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, kode_buku, jumlah):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.kode_buku = kode_buku
        self.jumlah = jumlah

    def __str__(self):
        return f"Judul : {self.judul}\nPenulis : {self.penulis}\nPenerbit : {self.penerbit}\nTahun Terbit : {self.tahun_terbit}\nKode Buku : {self.kode_buku}\nJumlah : {self.jumlah}"

class DaftarBuku:
    def __init__(self):
        self.daftar_buku = []

    def tampilan(self):
        if self.daftar_buku:
            table = PrettyTable()
            table.field_names = ["Kode", "Judul", "Penulis", "Penerbit", "Tahun Terbit", "Jumlah"]
            for buku in self.daftar_buku:
                table.add_row([buku.kode_buku, buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.jumlah])
            print(table)
        else:
            print("\nData Buku Belum Terdaftar")

class Peminjam:
    def __init__(self, nama, buku, tanggal_pinjam, tanggal_kembali):
        self.nama = nama
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

    def __str__(self):
        return f"Nama Peminjam : {self.nama}\nBuku yang Dipinjam : {self.buku}\nTanggal Pinjam : {self.tanggal_pinjam}\nTanggal Kembali : {self.tanggal_kembali}"

if __name__ == "__main__":
    buku1 = Buku("Atomic Habits", "James Clear", "Penguin Random House", 2018, 1, 5)
    buku2 = Buku("Kita Pergi Hari Ini", "Ziggy Zezsyazeoviennazabrizkie", "Gramedia Pustaka Utama", 2018, 2, 10)
    buku3 = Buku("Laut Bercerita", "Leila S. Chudori", "Gramedia Pustaka Utama", 2021, 3, 8)
    buku4 = Buku("Pride and Prejudice", "Jane Austen", "T. Egerton", 1813, 4, 5)
    buku5 = Buku("The Book of Forbidden Feelings", "Lala Bohang", "Gramedia Pustaka Utama", 2016, 5, 3)
    
    daftar_buku = DaftarBuku()
    daftar_buku.daftar_buku.extend([buku1, buku2, buku3, buku4, buku5])
    daftar_peminjam = []

def menu_buku():
    os.system("cls")
    print("""
+======================================================+
|            SELAMAT DATANG DI PERPUSTAKAAN            |
+======================================================+
""")

    while True:
        print("          |----------- Pilih Menu -----------|")
        print("          |----------------------------------|")
        print("          |1.| Lihat Daftar Buku             |")
        print("          |2.| Tambah Data Peminjaman Buku   |")
        print("          |3.| Ubah Data Buku                |")
        print("          |4.| Hapus Buku                    |")
        print("          |5.| Keluar                        |")
        print("          |----------------------------------|\n")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            os.system("cls")
            print("\nDaftar Buku:")
            daftar_buku.tampilan()
            input("\nTekan Enter untuk kembali...")
            os.system("cls")
        elif pilihan == "2":
            os.system("cls")
            print("\nDaftar Buku Tersedia:")
            daftar_buku.tampilan()
            while True:
                buku_dipinjam = input("Masukkan Kode Buku yang akan Dipinjam: ")
                buku_ditemukan = False
                for buku in daftar_buku.daftar_buku:
                    if buku.kode_buku == buku_dipinjam:
                        buku_ditemukan = True
                        if buku.jumlah > 0:
                            nama = input("Masukkan Nama Peminjam: ")
                            tanggal_pinjam = input("Masukkan Tanggal Peminjaman (YYYY-MM-DD): ")
                            tanggal_kembali = input("Masukkan Tanggal Pengembalian (YYYY-MM-DD): ")
                            peminjaman_baru = Peminjam(nama, buku.judul, tanggal_pinjam, tanggal_kembali)
                            daftar_peminjam.append(peminjaman_baru)
                            buku.jumlah -= 1
                            os.system("cls")
                            print("\nData Peminjaman berhasil ditambahkan:")
                            print(peminjaman_baru)
                            print("\nTekan Enter untuk kembali...")
                            break
                        else:
                            print("Maaf, stok buku sudah habis.")
                            break
                if buku_ditemukan:
                    break
                else:
                    print("Buku dengan kode tersebut tidak ditemukan.")
        elif pilihan == "3":
            os.system("cls")
            print("\nDaftar Buku Tersedia:")
            daftar_buku.tampilan()

            while True:
                judul = input("Masukkan Judul Buku yang ingin diubah: ")
                buku_ditemukan = False
                for buku in daftar_buku.daftar_buku:
                    if buku.judul == judul:
                        buku_ditemukan = True
                        break

                if buku_ditemukan:
                    print("")
                    penulis_baru = input("Masukkan Nama Penulis Baru (tekan Enter jika tidak ingin mengubah): ")
                    penerbit_baru = input("Masukkan Penerbit Baru (tekan Enter jika tidak ingin mengubah): ")
                    tahun_terbit_baru = input("Masukkan Tahun Terbit Baru (tekan Enter jika tidak ingin mengubah): ")
                    jumlah_baru = input("Masukkan Jumlah Buku Baru (tekan Enter jika tidak ingin mengubah): ")
                    os.system("cls")

                    # Perbarui data buku
                    if penulis_baru:
                        buku.penulis = penulis_baru
                    if penerbit_baru:
                        buku.penerbit = penerbit_baru
                    if tahun_terbit_baru:
                        buku.tahun_terbit = int(tahun_terbit_baru)
                    if jumlah_baru:
                        buku.jumlah = int(jumlah_baru)

                    print("\nData buku berhasil diubah!")

                    # Menampilkan data buku yang sudah diubah
                    print("\nData Buku Terbaru:")
                    print(buku)

                    # Menampilkan data peminjam
                    for peminjam in daftar_peminjam:
                        if peminjam.buku == judul:
                            print(peminjam)

                    break
                else:
                    print("\nBuku dengan judul", judul, "tidak ditemukan!")

            input("\nTekan Enter untuk kembali...")
            os.system("cls")
        elif pilihan == "4":
            os.system("cls")
            print("\nDaftar Buku Tersedia:")
            daftar_buku.tampilan()
            kode_buku = input("Masukkan Kode Buku yang ingin dihapus: ")
            buku_ditemukan = False
            for i, buku in enumerate(daftar_buku.daftar_buku):
                if buku.kode_buku == kode_buku:
                    buku_ditemukan = True
                    del daftar_buku.daftar_buku[i]
                    print("\nBuku dengan kode", kode_buku, "berhasil dihapus!")
                    break

            if not buku_ditemukan:
                print("Buku dengan kode tersebut tidak ditemukan.")
            input("\nTekan Enter untuk kembali...")
            pass
        elif pilihan == "5":
            print(f'''
    +-------------------------------------------------+
    |       Thank You For Using This Program :D       |
    +-------------------------------------------------+''')
            break
        else:
            print("Pilihan tidak valid!")

menu_buku()
