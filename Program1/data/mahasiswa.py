# data/mahasiswa.py

class Mahasiswa:
    def __init__(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_akhir = self.hitung_nilai_akhir()

    def hitung_nilai_akhir(self):
        return (0.3 * self.nilai_tugas) + (0.35 * self.nilai_uts) + (0.35 * self.nilai_uas)


class DataMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah(self, mahasiswa):
        self.data_mahasiswa[mahasiswa.nama.lower()] = mahasiswa
        print("Data berhasil ditambahkan.")

    def ubah(self, nama, mahasiswa_baru):
        nama_lower = nama.lower()
        if nama_lower in self.data_mahasiswa:
            self.data_mahasiswa[nama_lower] = mahasiswa_baru
            print("Data berhasil diubah.")
        else:
            print("Data tidak ditemukan.")

    def hapus(self, nama):
        nama_lower = nama.lower()
        if nama_lower in self.data_mahasiswa:
            del self.data_mahasiswa[nama_lower]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    def cari(self, nama):
        nama_lower = nama.lower()
        return self.data_mahasiswa.get(nama_lower, None)
