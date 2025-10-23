
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah
- **NIM**   : 250202942    
- **Kelas** : 1IKRB

---

## Tujuan
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **pengelolaan file dan direktori menggunakan perintah dasar Linux**, serta konsep **permission dan ownership**.  
Praktikum berfokus pada:
- Navigasi sistem file dengan `ls`, `pwd`, `cd`, dan `cat`.
- Pengaturan hak akses file menggunakan `chmod`.
- Pengubahan kepemilikan file menggunakan `chown`.
- Dokumentasi hasil eksekusi dan pengelolaan repositori praktikum.

Tujuan utama dari praktikum ini adalah agar mahasiswa mampu **mengoperasikan perintah Linux dasar dengan benar**, memahami sistem izin (permission), dan mendokumentasikan hasilnya dalam format laporan Git.


---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   cat /etc/passwd | head -n 5
    echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-21%20194417.png)

**Eksperimen 1 – Navigasi Sistem File**
---
Perintah pwd,ls -1,cd /tmp, dan ls -a

- Menunjukkan posisi pengguna di dalam hierarki sistem file Linux (dalam hal ini di `/home/ilham`).

- Perintah `ls` digunakan untuk melihat isi direktori. Karena tidak ada hasil yang muncul, berarti direktori home kosong.
 

- `/tmp` adalah direktori sementara untuk menyimpan file yang bersifat sementara oleh sistem atau pengguna.

- `ls -a` menampilkan semua file termasuk yang tersembunyi (berawalan titik), misalnya `.X11-unix `atau direktori yang digunakan `systemd`.
  
**Eksperimen 2 – Membaca File**
---
- Isi File /etc/passwd

  File /etc/passwd adalah file sistem penting di Linux/Unix yang berisi informasi tentang semua akun pengguna yang ada di sistem.
  Meskipun namanya “passwd”, file ini tidak menyimpan password secara langsung (password disimpan terenkripsi di /etc/shadow).


| Kolom | Nama                      | Penjelasan                                                                                                                                              |
| :---: | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1   | **username**              | Nama login pengguna. Contoh: `root`, `daemon`, `ilham`.                                                                                                 |
|   2   | **UID (User ID)**         | Nomor unik untuk setiap pengguna. <br>• `0` = root (superuser) <br>• `1–999` = akun sistem <br>• `1000+` = akun pengguna biasa                          |
|   3   | **GID (Group ID)**        | Nomor grup utama dari user (lihat detail di `/etc/group`).                                                                                              |
|   4   | **home_directory**        | Lokasi direktori “rumah” pengguna, tempat file pribadinya disimpan. Contoh: `/home/ilham` untuk user biasa, `/root` untuk root.                         |
|   5  | **login_shell**           | Program shell yang dijalankan saat pengguna login. Contoh: `/bin/bash`, `/bin/sh`, atau `/usr/sbin/nologin` untuk akun sistem yang tidak boleh login.   |

**Eksperimen 3 – Permission & Ownership**
---

- Sebelum chmod 600, file percobaan.txt memiliki izin -rw-r--r-- (644) — artinya pemilik dapat membaca dan menulis, sedangkan pengguna lain hanya bisa membaca.

- Setelah chmod 600, izin berubah menjadi -rw------- — hanya pemilik yang bisa membaca dan menulis, sedangkan pengguna lain tidak memiliki akses sama sekali.

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  



## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari perintah chmod? 
   
   **Jawaban:**  
2. Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  
3.  Jelaskan perbedaan antara chown dan chmod.  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  
- Bagaimana cara Anda mengatasinya?  
  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
