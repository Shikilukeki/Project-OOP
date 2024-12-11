# view/input_form.py

class InputForm:
    def input_data(self):
        try:
            nama = input("Masukkan nama: ")
            nilai_tugas = float(input("Masukkan nilai tugas: "))
            nilai_uts = float(input("Masukkan nilai UTS: "))
            nilai_uas = float(input("Masukkan nilai UAS: "))
            return nama, nilai_tugas, nilai_uts, nilai_uas
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")
            return self.input_data()
