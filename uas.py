class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def status(self):
        return "Lulus" if self.nilai >= 75 else "Tidak Lulus"


class MahasiswaProcess:
    def validasi_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 sampai 100")

    def buat_mahasiswa(self, nama, nilai):
        self.validasi_nilai(nilai)
        return Mahasiswa(nama, nilai)


class MahasiswaView:
    def input_data(self):
        nama = input("Masukkan nama mahasiswa: ")
        nilai = float(input("Masukkan nilai: "))
        return nama, nilai

    def tampilkan_tabel(self, mahasiswa):
        print("\n=== DATA MAHASISWA ===")
        print("-" * 40)
        print(f"{'Nama':15} | {'Nilai':5} | Status")
        print("-" * 40)
        print(f"{mahasiswa.nama:15} | {mahasiswa.nilai:5} | {mahasiswa.status()}")
        print("-" * 40)


def main():
    view = MahasiswaView()
    process = MahasiswaProcess()

    try:
        nama, nilai = view.input_data()
        mahasiswa = process.buat_mahasiswa(nama, nilai)
        view.tampilkan_tabel(mahasiswa)

    except ValueError as e:
        print("Error:", e)
    except Exception:
        print("Terjadi kesalahan input!")


if __name__ == "__main__":
    main()
