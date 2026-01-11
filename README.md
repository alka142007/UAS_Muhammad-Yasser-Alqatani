# UAS_Muhammad-Yasser-Alqatani

Class Data (Model) class Mahasiswa: def init(self, nama, nilai): self.nama = nama self.nilai = nilai

def status(self): return "Lulus" if self.nilai >= 75 else "Tidak Lulus" Fungsi Class Ini Class Mahasiswa berfungsi menyimpan data.

Penjelasan: init → constructor Dipanggil saat objek dibuat mahasiswa = Mahasiswa("Andi", 80) self.nama → menyimpan nama mahasiswa self.nilai → menyimpan nilai status() → menentukan lulus / tidak lulus Lulus jika nilai ≥ 75

Class ini TIDAK mengurus input atau output, hanya data.

Class Process (Controller) class MahasiswaProcess: def validasi_nilai(self, nilai): if nilai < 0 or nilai > 100: raise ValueError("Nilai harus antara 0 sampai 100")

def buat_mahasiswa(self, nama, nilai): self.validasi_nilai(nilai) return Mahasiswa(nama, nilai)

Fungsi Class Ini Mengatur logika & aturan bisnis.

Penjelasan: validasi_nilai() Mengecek apakah nilai: Tidak kurang dari 0 Tidak lebih dari 100 Jika salah → raise ValueError → Program langsung masuk ke except buat_mahasiswa() Memanggil validasi terlebih dahulu Jika valid → membuat objek Mahasiswa

Class Process adalah penghubung antara View dan Data.

Class View class MahasiswaView: def input_data(self): nama = input("Masukkan nama mahasiswa: ") nilai = float(input("Masukkan nilai: ")) return nama, nilai
Fungsi View Mengurus interaksi dengan pengguna.

Penjelasan: Meminta input: Nama (string) Nilai (diubah ke float) Mengembalikan nilai ke program utama

Tampilan Tabel def tampilkan_tabel(self, mahasiswa): Menampilkan data dalam format tabel Mengambil data dari objek mahasiswa Memanggil method status() Output contoh: Nama | Nilai | Status
Andi | 80 | Lulus

Program Utama (main) def main(): view = MahasiswaView() process = MahasiswaProcess()
Inisialisasi Membuat objek View Membuat objek Process

Try–Except (Validasi) try: nama, nilai = view.input_data() mahasiswa = process.buat_mahasiswa(nama, nilai) view.tampilkan_tabel(mahasiswa) Alurnya: Input user Validasi nilai Buat objek mahasiswa Tampilkan tabel

Penanganan Error except ValueError as e: print("Error:", e) Contoh error: Nilai = 120 Output: Error: Nilai harus antara 0 sampai 100

Program tidak crash, tapi menampilkan pesan error.

Alur Program Secara Keseluruhan Mulai ↓ User input nama & nilai ↓ Validasi nilai ↓ Buat objek Mahasiswa ↓ Hitung status lulus ↓ Tampilkan tabel ↓ Selesai
