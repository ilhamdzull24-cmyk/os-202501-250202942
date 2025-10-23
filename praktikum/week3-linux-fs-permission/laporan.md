
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
  
  Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

  Direktori aktif:
  
  `/home/ilham`

  Isi folder /tmp:

   `snap-private-tmp
systemd-private-83d9ac843f5c47ecbf8c49a4006281be-systemd-logind.service-hE48EB
systemd-private-83d9ac843f5c47ecbf8c49a4006281be-systemd-resolved.service-7T6yYO
systemd-private-83d9ac843f5c47ecbf8c49a4006281be-systemd-timesyncd.service-cCQejA`

File dan folder tersembunyi:

- `.`
- `..`
- `.X11-unix`

  
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
Analisis perbedaan sebelum dan sesudah chmod.
- Sebelum `chmod 600`, file percobaan.txt memiliki izin  -rw-r--r-- (644) — artinya pemilik dapat membaca dan menulis, sedangkan pengguna lain hanya bisa membaca.

- Setelah `chmod 600`, izin berubah menjadi -rw------- — hanya pemilik yang bisa membaca dan menulis, sedangkan pengguna lain tidak memiliki akses sama sekali.

Catat hasil :

`-rw------- 1 root ilham 24 Oct 21 19:41 percobaan.txt`

Artinya:

- `-rw-------` → hanya pemilik (root) yang dapat membaca dan menulis file.

- `root` → pemilik file sekarang adalah root.

- `ilham` → grup file masih milik user ilham.

- Ukuran: 18 byte

- Tanggal & waktu: 24 Oktober 2021, pukul 19:41

- Nama file: percobaan.txt
## Analisis
- Jelaskan makna hasil percobaan.  
  
  Percobaan linux-fs-permission menunjukkan cara Linux mengatur hak akses file.
Setiap file memiliki pemilik (owner), grup, dan lainnya (others) dengan izin read (r), write (w), dan execute (x).
Perintah chmod digunakan untuk mengubah izin akses, sedangkan chown untuk mengganti pemilik file.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
  
   - Fungsi Kernel
Kernel adalah inti sistem operasi yang mengatur akses terhadap sumber daya seperti file, memori, dan perangkat keras.
Saat pengguna menjalankan perintah seperti chmod atau chown, kernel memeriksa izin file melalui tabel permission di sistem file sebelum mengizinkan atau menolak akses.
Jadi, kernel berperan sebagai pengontrol keamanan antara pengguna dan sistem.

  - System Call
 Perintah chmod, chown, dan ls sebenarnya memanggil system call seperti:

    chmod() → mengubah mode (izin) file.

    chown() → mengubah pemilik file.

    stat() → membaca informasi metadata file.
 System call ini menjadi jembatan antara program pengguna (user space) dan kernel (kernel space).

   - Arsitektur Sistem Operasi
Dalam arsitektur OS, terdapat dua lapisan utama:

  User space: tempat user menjalankan perintah melalui shell.

  Kernel space: tempat kernel mengeksekusi system call dan mengatur akses ke file system.
  Saat user mengetik perintah di terminal, instruksi dikirim ke kernel melalui system call untuk dieksekusi dengan kontrol keamanan yang ketat.


- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
  
  Di Linux, kontrol akses dilakukan melalui sistem izin tradisional berbasis bit (rwx), sedangkan di Windows menggunakan ACL yang lebih rinci. Meskipun berbeda mekanisme, keduanya bertujuan sama: menjaga keamanan dan membatasi akses file sesuai hak pengguna.



## Kesimpulan


Praktikum Linux FS Permission menunjukkan bahwa Linux mengatur keamanan file melalui sistem izin read (r), write (w), dan execute (x) untuk owner, group, dan others. Perintah seperti chmod dan chown digunakan untuk mengatur akses, sementara kernel mengontrolnya melalui system call, memastikan hanya pengguna berhak yang dapat mengakses file.
---

## Quiz
1. Apa fungsi dari perintah chmod? 
   
   Perintah chmod berfungsi untuk mengubah hak akses (permission) pada file atau direktori di sistem operasi Linux/Unix.
    
2. Apa arti dari kode permission rwxr-xr--?
   
   kode rwxr-xr-- memberikan hak penuh (baca, tulis, eksekusi) kepada pemilik, hak baca dan eksekusi kepada grup, dan hanya hak baca kepada pengguna lain.
    
3.  Jelaskan perbedaan antara chown dan chmod.  
     chmod() → mengubah mode (izin) file.

    chown() → mengubah pemilik file.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  
  selalu menantang

- Bagaimana cara Anda mengatasinya?  
  
  belajar bersama teman dan melihat tutorial

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
