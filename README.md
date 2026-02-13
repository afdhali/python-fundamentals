# Python Fundamentals

Repository ini berisi materi pembelajaran dasar Python dan contoh project sederhana untuk memahami struktur Python package.

## Struktur Proyek

```
your-repo-name/
├── 01-variables.py          # File pembelajaran dasar Python
├── 02-type-casting.py         # ... dan file pembelajaran lainnya
├── ...
├── venv/                    # Virtual environment (dibuat saat setup)
├── simple-calculator/       # Sub-project: Contoh struktur Python package
│   ├── src/
│   │   └── calculator/
│   │       ├── __init__.py
│   │       ├── __main__.py
│   │       ├── operations.py
│   │       └── ui.py
│   └── pyproject.toml
└── README.md               # File ini
```

## Persyaratan Sistem

- Python 3.9 atau lebih tinggi
- pip (Python package installer)

## Setup Awal

### 1. Membuat Virtual Environment

Virtual environment digunakan untuk mengisolasi dependencies proyek. **Semua perintah dijalankan dari folder root `your-repo-name/`**.

#### Untuk Bash/Linux/macOS:

```bash
# Pastikan Anda berada di folder your-repo-name/
# pwd harus menunjukkan: .../your-repo-name

# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate
```

#### Untuk PowerShell (Windows):

```powershell
# Pastikan Anda berada di folder your-repo-name/
# pwd harus menunjukkan: ...\your-repo-name

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
.\venv\Scripts\Activate.ps1
```

**Catatan untuk PowerShell:** Jika muncul error terkait execution policy, jalankan:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Untuk Command Prompt (Windows):

```cmd
# Pastikan Anda berada di folder your-repo-name/

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate.bat
```

### 2. Verifikasi Virtual Environment Aktif

Setelah aktivasi, Anda akan melihat `(venv)` di awal command prompt:

```bash
(venv) user@computer:~/your-repo-name$
```

## Menjalankan File Pembelajaran Python

Untuk menjalankan file-file pembelajaran dasar Python:

```bash
# Pastikan venv aktif dan Anda berada di folder your-repo-name/

# Jalankan file pembelajaran
python 01-variables.py
python 02-type-casting.py
# ... dan seterusnya
```

## Menjalankan Sub-Project: Simple Calculator

### 1. Install Package Calculator

Pastikan virtual environment sudah aktif dan Anda berada di folder root `your-repo-name/`:

```bash
# Install package calculator dalam mode editable
pip install -e simple-calculator/
```

Mode editable (`-e`) memungkinkan Anda mengubah source code tanpa perlu reinstall package.

### 2. Menjalankan Program Calculator

Ada beberapa cara untuk menjalankan kalkulator (semua dari folder root):

#### Cara 1: Menggunakan command yang sudah terdaftar

```bash
calc
```

#### Cara 2: Menjalankan sebagai module

```bash
python -m calculator
```

#### Cara 3: Menjalankan file **main**.py secara langsung

```bash
python simple-calculator/src/calculator/__main__.py
```

### 3. Cara Menggunakan Kalkulator

1. Setelah program berjalan, Anda akan melihat menu operasi yang tersedia
2. Pilih operasi dengan memasukkan nomor (1-4)
3. Masukkan angka pertama
4. Masukkan angka kedua
5. Program akan menampilkan hasil perhitungan
6. Ketik `q` atau `keluar` untuk keluar dari program

#### Contoh Penggunaan

```
Selamat datang di Kalkulator Sederhana!
Ketik 'q' atau 'keluar' untuk berhenti

=== Menu Kalkulator ===
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
=======================

Pilih operasi (1-4): 1
Masukkan angka pertama: 10
Masukkan angka kedua: 5
Hasil: 10 + 5 = 15
```

## Menonaktifkan Virtual Environment

Setelah selesai belajar atau menggunakan program, Anda bisa menonaktifkan virtual environment:

```bash
deactivate
```

Prompt akan kembali normal tanpa `(venv)` di awal.

## Workflow Pembelajaran

### Untuk Belajar Dasar Python

```bash
# 1. Aktifkan virtual environment
source venv/bin/activate          # Linux/macOS
# atau
.\venv\Scripts\Activate.ps1       # Windows PowerShell

# 2. Jalankan file pembelajaran
python 01-variables.py
python 02-type-casting.py

# 3. Selesai belajar? Nonaktifkan venv
deactivate
```

### Untuk Belajar Struktur Package (Simple Calculator)

```bash
# 1. Aktifkan virtual environment
source venv/bin/activate          # Linux/macOS

# 2. Install calculator package (hanya sekali)
pip install -e simple-calculator/

# 3. Jalankan program
calc

# 4. Edit source code di simple-calculator/src/calculator/
# Perubahan langsung terdeteksi karena mode editable

# 5. Selesai? Nonaktifkan venv
deactivate
```

## Troubleshooting

### 1. Perintah `python` tidak ditemukan

- **Linux/macOS**: Gunakan `python3` instead of `python`
- **Windows**: Pastikan Python sudah diinstall dan ada di PATH

### 2. Virtual environment tidak aktif

Pastikan Anda melihat `(venv)` di awal command prompt. Jika tidak:

- Ulangi langkah aktivasi venv
- Pastikan Anda berada di folder `your-repo-name/`

### 3. Error "Module 'calculator' not found"

Pastikan Anda sudah:

1. Aktifkan virtual environment
2. Jalankan `pip install -e simple-calculator/` dari folder root

### 4. Error pembagian dengan nol

Program sudah menangani ini dengan menampilkan pesan error. Ini adalah fitur keamanan.

### 5. PowerShell execution policy error

Jalankan PowerShell sebagai Administrator dan eksekusi:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Tips Pengembangan

### Menambah File Pembelajaran Baru

Cukup buat file `.py` baru di folder root:

```bash
# Buat file baru
touch 05-my-new-lesson.py

# Edit dengan text editor favorit
nano 05-my-new-lesson.py

# Jalankan
python 05-my-new-lesson.py
```

### Modifikasi Calculator

1. Edit file di `simple-calculator/src/calculator/`
2. Tidak perlu reinstall karena menggunakan mode editable
3. Langsung jalankan `calc` untuk testing

### Melihat Package yang Terinstall

```bash
pip list
```

## Kesimpulan

- **Folder root** (`your-repo-name/`) adalah tempat virtual environment dan file pembelajaran
- **Semua perintah CLI** dijalankan dari folder root
- **Sub-project** (`simple-calculator/`) adalah contoh struktur Python package profesional
- **Satu venv** untuk semua: file pembelajaran dan sub-project

## Lisensi

MIT License - Silakan gunakan dan modifikasi sesuai kebutuhan Anda.
