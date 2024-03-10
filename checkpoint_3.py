import os
import datetime
from prettytable import PrettyTable


class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, kode_buku, jumlaah):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.kode_buku = kode_buku
        self.jumlah = jumlah
        self.daftar_peminjam = []

    def __str__(self):
        return f"Judul : {self.judul}\nPenulis : {self.penulis}\nPenerbit : {self.penerbit}\nTahun Terbit : {self.tahun_terbit}\nKode Buku : {self.kode_buku}\nJumlah : {self.jumlah}"


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class daftar_buku:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, kode_buku, data):
        current = self.head
        while current:
            if current.data.kode_buku == kode_buku:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                break
            current = current.next

    def add_before(self, kode_buku, data):
        current = self.head
        while current:
            if current.data.kode_buku == kode_buku:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                break
            current = current.next

    def update_data(self, kode_buku, data):
        current = self.head
        while current:
            if current.data.kode_buku == kode_buku:
                current.data = data
                break
            current = current.next

    def delete_first(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.tail = None

    def delete_last(self):
        if self.tail:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = self.tail = None

    def delete_data(self, kode_buku):
        current = self.head
        while current:
            if current.data.kode_buku == kode_buku:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.delete_first()
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.delete_last()
                break
            current = current.next

    def tampilan(self):
        if self.is_empty():
            print("\nData Buku Belum Terdaftar")
            return
        table = PrettyTable()
        table.field_names = ["Kode", "Judul", "Penulis", "Penerbit", "Tahun Terbit", "Jumlah"]
        current = self.head
        while current:
            buku = current.data
            table.add_row([buku.kode_buku, buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.jumlah])
            current = current.next
        print(table)
        
    def tampilan_peminjaman(self):
        if self.head is None:
            print("\nTidak ada peminjaman buku.")
            return
        table = PrettyTable()
        table.field_names = ["Nama Peminjam", "Judul Buku", "Tanggal Pinjam", "Tanggal Kembali"]
        current = self.head
        while current:
            buku = current.data
            for peminjam in buku.daftar_peminjam:
                table.add_row([peminjam.nama, buku.judul, peminjam.tanggal_pinjam.strftime('%Y-%m-%d'), peminjam.tanggal_kembali.strftime('%Y-%m-%d')])
            current = current.next
        print(table)

    def quicksort(self, arr, key, ascending=True):
        if len(arr) <= 1:
            return arr
        else:
            pivot = getattr(arr[0], key)
            greater = []
            lesser = []
            for item in arr[1:]:
                if (getattr(item, key) <= pivot) if ascending else (getattr(item, key) >= pivot):
                    lesser.append(item)
                else:
                    greater.append(item)
            return self.quicksort(lesser, key, ascending) + [arr[0]] + self.quicksort(greater, key, ascending)

    def sort_by_judul(self, ascending=True):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        arr = self.quicksort(arr, 'judul', ascending)
        self.head = Node(arr[0])
        current = self.head
        for item in arr[1:]:
            current.next = Node(item)
            current.next.prev = current
            current = current.next
        self.tail = current

    def sort_by_penulis(self, ascending=True):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        arr = self.quicksort(arr, 'penulis', ascending)
        self.head = Node(arr[0])
        current = self.head
        for item in arr[1:]:
            current.next = Node(item)
            current.next.prev = current
            current = current.next
        self.tail = current


class Peminjam:
    def __init__(self, nama, buku):
        self.nama = nama
        self.buku = buku
        self.tanggal_pinjam = datetime.datetime.now()
        self.tanggal_kembali = self.tanggal_pinjam + datetime.timedelta(days=7)

    def __str__(self):
        return f"Nama Peminjam : {self.nama}\nBuku yang Dipinjam : {self.buku}\nTanggal Pinjam : {self.tanggal_pinjam.strftime('%Y-%m-%d')}\nTanggal Kembali : {self.tanggal_kembali.strftime('%Y-%m-%d')}"


if __name__ == "__main__":
    buku1 = Buku("Atomic Habits", "James Clear", "Penguin Random House", 2018, 1, 5)
    buku2 = Buku("Kita Pergi Hari Ini", "Ziggy Zezsyazeoviennazabrizkie", "Gramedia Pustaka Utama", 2018, 2, 10)
    buku3 = Buku("Laut Bercerita", "Leila S. Chudori", "Gramedia Pustaka Utama", 2021, 3, 8)
    buku4 = Buku("Pride and Prejudice", "Jane Austen", "T. Egerton", 1813, 4, 5)
    buku5 = Buku("The Book of Forbidden Feelings", "Lala Bohang", "Gramedia Pustaka Utama", 2016, 5, 3)

    daftar_buku = daftar_buku()
    daftar_buku.add_last(buku1)
    daftar_buku.add_last(buku2)
    daftar_buku.add_last(buku3)
    daftar_buku.add_last(buku4)
    daftar_buku.add_last(buku5)
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
            print("          |3.| Lihat Daftar Peminjam         |")
            print("          |4.| Ubah Data Buku                |")
            print("          |5.| Hapus Buku                    |")
            print("          |6.| Urutkan Buku                  |")
            print("          |7.| Keluar                        |")
            print("          |----------------------------------|\n")

            pilihan = input("Pilih menu (1-7): ")
            if pilihan == "1":
                os.system("cls")
                print("\nDaftar Buku:")
                
                daftar_buku.tampilan()
                input("\nTekan Enter untuk kembali...")
                os.system("cls")

            elif pilihan == "2":
                while True:
                    os.system("cls")
                    daftar_buku.tampilan()

                    buku_dipinjam = input("Masukkan Kode Buku (atau tekan Enter untuk kembali): ")

                    if not buku_dipinjam:
                        break

                    found = False
                    current = daftar_buku.head
                    while current:
                        if str(current.data.kode_buku) == buku_dipinjam:
                            found = True
                            if current.data.jumlah > 0:
                                nama = input("Masukkan Nama Peminjam: ")
                                tanggal = datetime.date.today()
                                peminjaman_baru = Peminjam(nama, current.data.judul)
                                current.data.daftar_peminjam.append(peminjaman_baru)
                                daftar_peminjam.append(peminjaman_baru)
                                current.data.jumlah -= 1
                                os.system("cls")
                                print("\nData Peminjaman berhasil ditambahkan:")
                                print(peminjaman_baru)
                            else:
                                print("Maaf, stok buku sudah habis.")
                            break
                        current = current.next
                    else:
                        print("Kode buku tidak valid. Silakan masukkan kode yang benar.")

                    lagi = input("\nApakah ingin meminjam buku lagi? (y/t): ")
                    if lagi.lower() != 'y':
                        break

                input("\nTekan Enter untuk kembali ke menu utama...")
                os.system("cls")

            elif pilihan == "3":
                print("\nDaftar Peminjaman Buku:")
                if not daftar_peminjam:
                    print("Tidak ada data peminjaman buku.")
                else:
                    table_peminjaman = PrettyTable()
                    table_peminjaman.field_names = ["Nama Peminjam", "Judul Buku"]
                    for peminjam in daftar_peminjam:
                        table_peminjaman.add_row([peminjam.nama, peminjam.buku])
                    print(table_peminjaman)

                input("\nTekan Enter untuk kembali...")
                os.system("cls")

            elif pilihan == "4":
                os.system("cls")
                print("\nDaftar Buku Tersedia:")
                daftar_buku.tampilan()

                while True:
                    judul = input("Masukkan Judul Buku yang ingin diubah: ")
                    buku_ditemukan = False
                    current = daftar_buku.head
                    while current:
                        if current.data.judul == judul:
                            buku_ditemukan = True
                            break
                        current = current.next

                    if buku_ditemukan:
                        print("")
                        penulis_baru = input("Masukkan Nama Penulis Baru (tekan Enter jika tidak ingin mengubah): ")
                        penerbit_baru = input("Masukkan Penerbit Baru (tekan Enter jika tidak ingin mengubah): ")
                        tahun_terbit_baru = input("Masukkan Tahun Terbit Baru (tekan Enter jika tidak ingin mengubah): ")
                        jumlah_baru = input("Masukkan Jumlah Buku Baru (tekan Enter jika tidak ingin mengubah): ")
                        os.system("cls")

                        # Memperbarui data buku
                        if penulis_baru:
                            current.data.penulis = penulis_baru
                        if penerbit_baru:
                            current.data.penerbit = penerbit_baru
                        if tahun_terbit_baru:
                            current.data.tahun_terbit = int(tahun_terbit_baru)
                        if jumlah_baru:
                            current.data.jumlah = int(jumlah_baru)

                        print("\nData buku berhasil diubah!")

                        # Menampilkan data buku yang sudah diubah
                        print("\nData Buku Terbaru:")
                        print(current.data)
                        break
                    else:
                        print("\nBuku dengan judul", judul, "tidak ditemukan!")

                input("\nTekan Enter untuk kembali...")
                os.system("cls")

            elif pilihan == "5":
                os.system("cls")
                print("\nDaftar Buku Tersedia:")
                daftar_buku.tampilan()
                kode_buku = input("Masukkan Kode Buku yang ingin dihapus: ")
                buku_ditemukan = False
                current = daftar_buku.head
                while current:
                    if current.data.kode_buku == int(kode_buku):
                        buku_ditemukan = True
                        if current.prev:
                            current.prev.next = current.next
                        else:
                            daftar_buku.head = current.next
                        if current.next:
                            current.next.prev = current.prev
                        else:
                            daftar_buku.tail = current.prev
                        print("\nBuku dengan kode", kode_buku, "berhasil dihapus!")
                        break
                    current = current.next

                if not buku_ditemukan:
                    print("Buku dengan kode tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")
                os.system("cls")                
                pass

            elif pilihan == "6":
                while True:
                    os.system("cls")
                    print("\nUrutkan Berdasarkan:")
                    print("1. Judul Buku (Ascending)")
                    print("2. Judul Buku (Descending)")
                    print("3. Penulis (Ascending)")
                    print("4. Penulis (Descending)")

                    sub_pilihan = input("\nPilih opsi yang Anda inginkan (1-4), atau 't' untuk kembali: ")

                    if sub_pilihan == "t":
                        break

                    if sub_pilihan not in {"1", "2", "3", "4"}:
                        print("Opsi tidak valid. Silakan masukkan angka antara 1-4 atau tekan 't' untuk kembali.")
                        continue

                    os.system("cls")
                    if sub_pilihan == "1":
                        print("\nDaftar Buku (Urut Judul Ascending):")
                        daftar_buku.sort_by_judul()
                    elif sub_pilihan == "2":
                        print("\nDaftar Buku (Urut Judul Descending):")
                        daftar_buku.sort_by_judul(ascending=False)
                    elif sub_pilihan == "3":
                        print("\nDaftar Buku (Urut Penulis Ascending):")
                        daftar_buku.sort_by_penulis()
                    elif sub_pilihan == "4":
                        print("\nDaftar Buku (Urut Penulis Descending):")
                        daftar_buku.sort_by_penulis(ascending=False)
                    
                    daftar_buku.tampilan()

                    while True:
                        lagi = input("\nApakah Anda ingin mengurutkan dengan opsi lain? (y/t): ")
                        if lagi.lower() not in {"y", "t"}:
                            print("Pilihan tidak valid. Silakan masukkan 'y' atau 't'.")
                        else:
                            break

                    if lagi.lower() != 'y':
                        break

                input("\nTekan Enter untuk kembali ke menu utama...")
                os.system("cls")

            elif pilihan == "7":
                os.system("cls")
                print(f'''
        +-------------------------------------------------+
        |       Thank You For Using This Program :D       |
        +-------------------------------------------------+''')
                break
            else:
                print("Pilihan tidak valid!")

    menu_buku()
