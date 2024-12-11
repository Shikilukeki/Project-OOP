# Project-OOP

Rifqi Maulana

312410529

TI.24.A.5

## FlowChart

![Image](https://github.com/Shikilukeki/Foto/blob/main/LabPy08.png?raw=true)

## Diagram class

![Image]()

## Penjelasan

### Direktori
![Image](https://github.com/Shikilukeki/Foto/blob/main/Direktori%20Program.png?raw=true)

### data/mahasiswa.py

```Class Mahasiswa```
```__init__(self, nama, nilai_tugas, nilai_uts, nilai_uas)``` Konstruktor untuk inisialisasi objek Mahasiswa dengan atribut nama, nilai tugas, nilai UTS, nilai UAS, dan menghitung nilai akhir.

hitung_nilai_akhir(self) Menghitung nilai akhir berdasarkan bobot nilai tugas, nilai UTS, dan nilai UAS.

```Class DataMahasiswa```
```__init__(self)``` Konstruktor untuk inisialisasi objek DataMahasiswa dengan dictionary kosong untuk menyimpan data mahasiswa.

```tambah(self, mahasiswa)``` Menambahkan objek Mahasiswa baru ke dictionary data_mahasiswa dengan nama sebagai kuncinya.

```ubah(self, nama, mahasiswa_baru)``` Mengubah data mahasiswa yang sudah ada berdasarkan nama, jika ditemukan dalam dictionary.

```hapus(self, nama)``` Menghapus data mahasiswa berdasarkan nama, jika ditemukan dalam dictionary.

```cari(self, nama)``` Mencari data mahasiswa berdasarkan nama dan mengembalikan objek Mahasiswa jika ditemukan, atau None jika tidak ditemukan.

### view/input_form.py

```Class InputForm```
```input_data(self)``` Mengambil input dari pengguna untuk nama, nilai tugas, nilai UTS, dan nilai UAS. Mengembalikan nilai-nilai ini sebagai tuple. Jika input tidak valid, akan meminta input ulang.

### view/mahasiswa.py

```Class ViewMahasiswa```
tampilkan_daftar(self, data_mahasiswa) Menampilkan daftar semua data mahasiswa dalam format tabel. Jika tidak ada data mahasiswa, menampilkan pesan bahwa data mahasiswa belum ada.

tampilkan_detail(self, nomor, mahasiswa) Menampilkan detail individu dari mahasiswa tertentu, termasuk nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.

### main.py
```Class Program```
```__init__(self)``` Konstruktor untuk inisialisasi objek Program dengan instance DataMahasiswa, InputForm, dan ViewMahasiswa.

```menu_utama(self)``` Menampilkan menu utama dan meminta pengguna untuk memilih opsi. Menjalankan fungsi yang sesuai berdasarkan pilihan pengguna.

```tambah_data(self)``` Mengambil input dari pengguna melalui InputForm, membuat objek Mahasiswa, dan menambahkannya ke DataMahasiswa.

```ubah_data(self)``` Mengambil input nama dari pengguna, mencari data mahasiswa berdasarkan nama, dan jika ditemukan, meminta input baru dan mengubah data mahasiswa tersebut.

```hapus_data(self)``` Mengambil input nama dari pengguna dan menghapus data mahasiswa berdasarkan nama, jika ditemukan.

```lihat_data(self)``` Menampilkan daftar semua data mahasiswa melalui ViewMahasiswa.

```keluar(self)``` Menampilkan pesan keluar dan mengakhiri program.

```invalid(self)``` Menangani pilihan menu yang tidak valid dan menampilkan pesan kesalahan.

## Hasil eksekusi program

### Tambah data

![Image](https://github.com/Shikilukeki/Foto/blob/main/Project%20OOP%20-%20Tambah%20data.png?raw=true)

### Ubah data

![Image](https://github.com/Shikilukeki/Foto/blob/main/Project%20OOP%20-%20Ubah%20data.png?raw=true)

### Hapus data

![Image](https://github.com/Shikilukeki/Foto/blob/main/Project%20OOP%20-%20Hapus%20data.png?raw=true)
