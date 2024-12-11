# view/mahasiswa.py

class ViewMahasiswa:
    def tampilkan_daftar(self, data_mahasiswa):
        print("\nDaftar Data Mahasiswa:")
        print("==================================================================================")
        print("| No | Nama                      | Tugas | UTS   | UAS   | Akhir                 |")
        print("==================================================================================")

        if data_mahasiswa:
            for i, mahasiswa in enumerate(data_mahasiswa.values(), start=1):
                print(f"| {i:>2} | {mahasiswa.nama:<25} | {mahasiswa.nilai_tugas:<5} | {mahasiswa.nilai_uts:<5} | {mahasiswa.nilai_uas:<5} | {mahasiswa.nilai_akhir:<21.2f} |")
                print("==================================================================================")
        else:
            print("|                             Belum ada data mahasiswa                           |")
            print("==================================================================================")

    def tampilkan_detail(self, nomor, mahasiswa):
        print(f"{nomor}. Nama: {mahasiswa.nama}")
        print(f"   Nilai Tugas: {mahasiswa.nilai_tugas}")
        print(f"   Nilai UTS: {mahasiswa.nilai_uts}")
        print(f"   Nilai UAS: {mahasiswa.nilai_uas}")
        print(f"   Nilai Akhir: {mahasiswa.nilai_akhir:.2f}")
        print("-------------------------------------------------------------------")
