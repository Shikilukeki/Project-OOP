# main.py

from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

class Program:
    def __init__(self):
        self.data_mahasiswa = DataMahasiswa()
        self.input_form = InputForm()
        self.view_mahasiswa = ViewMahasiswa()

    def menu_utama(self):
        pilihan_menu = {
            '1': self.tambah_data,
            '2': self.ubah_data,
            '3': self.hapus_data,
            '4': self.lihat_data,
            '5': self.keluar
        }

        while True:
            print("\nProgram mendata mahasiswa")
            pilihan = input("[1] Tambah data\n[2] Ubah data\n[3] Hapus data\n[4] Lihat data\n[5] Keluar\nPilih menu: ")
            pilihan_menu.get(pilihan, self.invalid)()

    def tambah_data(self):
        nama, nilai_tugas, nilai_uts, nilai_uas = self.input_form.input_data()
        mahasiswa = Mahasiswa(nama, nilai_tugas, nilai_uts, nilai_uas)
        self.data_mahasiswa.tambah(mahasiswa)

    def ubah_data(self):
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        data = self.data_mahasiswa.cari(nama)
        if data:
            nama_baru, nilai_tugas, nilai_uts, nilai_uas = self.input_form.input_data()
            mahasiswa_baru = Mahasiswa(nama_baru, nilai_tugas, nilai_uts, nilai_uas)
            self.data_mahasiswa.ubah(nama, mahasiswa_baru)
        else:
            print("Data tidak ditemukan.")

    def hapus_data(self):
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        self.data_mahasiswa.hapus(nama)

    def lihat_data(self):
        self.view_mahasiswa.tampilkan_daftar(self.data_mahasiswa.data_mahasiswa)

    def keluar(self):
        print("Keluar dari program. Terima kasih!")
        exit()

    def invalid(self):
        print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    program = Program()
    program.menu_utama()
