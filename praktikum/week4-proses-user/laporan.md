
# Laporan Praktikum Minggu [4]
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah  
- **NIM**   : 250202942 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  
---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **konsep proses dan manajemen user dalam sistem operasi Linux.**  
Mahasiswa akan memahami bagaimana sistem operasi:
- Membuat dan mengatur proses (process management).  
- Mengelola user, group, serta hak akses pengguna.  
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.  
- Menghubungkan konsep user management dengan keamanan sistem operasi.

Eksperimen dilakukan melalui penggunaan perintah dasar seperti `ps`, `top`, `kill`, `adduser`, `passwd`, `id`, dan `groups`.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-10-29%20123715.png)

## Eksperimen 1 – Identitas User 
1. Login dan Pemeriksaan User Aktif
  ```bash

  ilham@ilhamdzfx:~$ ``whoami``
  ilham
```
 - Perintah: `whoami`

- Fungsi: Menampilkan nama user yang sedang aktif/login saat ini.

- Output: `ilham` → berarti user yang sedang digunakan bernama ilham.

2. Melihat Informasi User dan Grup
   ```bash

   ilham@ilhamdzfx:~$ ``id``
   uid=1000(ilham) gid=1000(ilham) ``groups``=1000(ilham),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
- Perintah: `id`

- Fungsi: Menampilkan informasi identitas user dan grup-grup yang diikutinya.

- Penjelasan output:

     - `uid=1000(ilham)` → user ID 1000, username: ilham

     - `gid=1000(ilham)` → group ID utama adalah ilham

     - `groups=...` → daftar grup lain yang diikuti user ini (misalnya: sudo, audio, video, dll).

     - Kesimpulan: user ilham punya hak sudo (admin).
  
3. Melihat Daftar Grup User
   ```bash

   ilham@ilhamdzfx:~$ groups
   ilham adm dialout cdrom floppy sudo audio dip video plugdev netdev

- Perintah: `groups`

- Fungsi: Menampilkan daftar nama grup tempat user ilham terdaftar.

- Outputnya konsisten dengan hasil `id`
 sebelumnya.

4. Membuat User Baru
   ```bash
   ilham@ilhamdzfx:~$ sudo adduser praktikan
   ```
- Perintah: `sudo adduser praktikan`

- Fungsi: Membuat akun user baru bernama praktikan (dengan hak admin `sudo`).

- Proses yang terjadi (dan terlihat di output):
  
  ```vbnet

  Adding user `praktikan' ...
  Adding new group `praktikan' (1001) ...
  Adding new user `praktikan' (1001) with group `praktikan' ...
  Creating home directory `/home/praktikan' ...
  Copying files from `/etc/skel' ...
  ```
- Sistem membuat user dan grup baru bernama praktikan

- Membuat home directory: `/home/praktikan`

- Menyalin file konfigurasi default dari `/etc/skel`
  
5. Menentukan Password User Baru

```bash

New password:
Retype new password:
passwd: password updated successfully
```
- Fungsi: Menetapkan kata sandi baru untuk user `praktikan`.

- Setelah dikonfirmasi, sistem menampilkan:

   `password updated successfully`
   → Password berhasil disimpan.

6. Menambahkan Informasi Tambahan User
```bash

Changing the user information for praktikan
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] Y
```
- Fungsi: Mengisi data tambahan user (opsional).
Pengguna menekan Enter untuk melewati semuanya dan mengetik Y untuk konfirmasi.
7. Mengganti User ke Akun Baru
```bash

ilham@ilhamdzfx:~$ su – praktikum
```
- Perintah: `su - praktikum`

- Fungsi: Berpindah user (switch user) ke praktikum dengan login shell penuh (`-`).

8. Terjadi Error
   ```bash

   su: user praktikum does not exist or the user entry does not contain all the required fields
- Masalah: User praktikum tidak ditemukan.

- Penyebab:

   - Kamu membuat user bernama praktikan, bukan praktikum.

   - Jadi perintah seharusnya:
  ```bash
    su - praktikan
  ```
  - Kesalahan satu huruf menyebabkan sistem tidak menemukan user.

## Eksperimen 2 – Monitoring Proses 
![Screenshot hasil](./screenshots/Screenshot%202025-10-29%20123911.png)
![Screenshot hasil](./screenshots/Screenshot%202025-10-29%20123959.png)

```bash
top -n 1
```
Perintah ini digunakan untuk memantau proses yang sedang berjalan di sistem Linux secara real-time, termasuk penggunaan CPU dan memori.

| **Kolom**   | **Kepanjangan / Arti**    | **Fungsi / Keterangan**                                                                                                                     | **Contoh dari gambar**                                          |
| ----------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **PID**     | *Process ID*              | Nomor unik yang diberikan sistem ke setiap proses yang berjalan. Berguna untuk mengenali dan mengelola proses (misalnya dengan `kill PID`). | `534` untuk proses `top`                                        |
| **USER**    | *User name*               | Menunjukkan siapa pemilik proses tersebut (user yang menjalankannya).                                                                       | `ilham`, `root`, `systemd+`, `message+`                         |
| **%CPU**    | *CPU Usage Percentage*    | Persentase penggunaan CPU oleh proses tersebut. Semakin tinggi nilainya, semakin besar sumber daya CPU yang digunakan.                      | `6.7` untuk proses `top` (karena `top` sedang aktif menghitung) |
| **%MEM**    | *Memory Usage Percentage* | Persentase penggunaan memori fisik (RAM) oleh proses. Berguna untuk mendeteksi proses yang boros memori.                                    | `0.1` pada `top`, `0.5` pada `rsyslogd`                         |
| **COMMAND** | *Command Name*            | Nama atau perintah yang digunakan untuk menjalankan proses tersebut.                                                                        | `top`, `systemd`, `bash`, `wget`                                |

## Eksperimen 3 – Kontrol Proses

![Screenshot hasil](./screenshots/Screenshot%202025-10-29%20124247.png)

- Perintah sleep 1000 berarti sistem akan menunda (tidak melakukan apa-apa) selama 1000 detik.

- Tanda & di akhir perintah membuat proses ini berjalan di latar belakang (background).

- Shell tidak akan menunggu proses ini selesai; kamu bisa tetap mengetik perintah lain.

- Setelah dijalankan, shell menampilkan:
  ```csharp
  [1] 538
  ```
     - [1] → nomor job (urutan proses background dalam shell)

     - 538 → PID (Process ID) dari proses sleep yang baru dibuat
- ps aux menampilkan semua proses yang berjalan di sistem (dari semua user).

- grep sleep menyaring hasil agar hanya menampilkan proses yang mengandung kata sleep.

 Hasilnya menampilkan baris:
 ```yaml


 ilham   538  0.0  0.0  3212 1792 pts/0  S  12:40  0:00 sleep 1000
 ```
 - `kill` digunakan untuk mengirim sinyal ke proses berdasarkan PID-nya.

- Secara default, `kill` mengirim sinyal SIGTERM (15) yang menghentikan proses dengan cara “sopan”.

- Setelah dijalankan, proses `sleep` berhenti.

PID proses `sleep` adalah 538

Kesimpulannya Program latar belakang (background process) seperti `sleep 1000 &` memungkinkan pengguna:

- Menjalankan proses tanpa menunggu hasilnya (non-blocking).

- Tetap bisa mengetik perintah lain di terminal.

- Mengelola proses tersebut menggunakan `jobs`, `ps`, dan `kill`.
  
## Eksperimen 4 – Analisis Hierarki Proses 

![Screenshot hasil](./screenshots/Screenshot%202025-10-29%20124554.png)

1. Proses Induk Utama
   ```scss
   systemd(1)
   ```
- PID 1 menunjukkan `systemd` adalah proses induk utama (parent process) di sistem.

- `systemd` berfungsi sebagai init system modern pada Linux — menggantikan `init` tradisional.

- Semua proses lain di sistem adalah turunan (child process) dari `systemd`.
  
2. Contoh Child Proses dari `systemd(1)`
   Dari pohon proses yang terlihat :

   ```scss
   systemd(1)
   ├─ agetty(228)
   ├─ cron(192)
   ├─ dbus-daemon(194)
   ├─ rsyslogd(200)
   ├─ systemd-journal(67)
   ├─ systemd-logind(207)
   ├─ systemd-resolve(110)
   ├─ systemd-timesyn(111)
   ├─ systemd-udevd(96)
   └─ unattended-upgr(246)
    ```
 Layanan sistem yang dijalankan oleh `systemd` masing-masing memilki tugas tertentu:

- `agetty` → menangani terminal login

- `cron` → penjadwalan tugas otomatis

- `dbus-daemon` → komunikasi antarproses

- `rsyslogd` → logging sistem

- `systemd-logind` → manajemen sesi pengguna

3. Proses Shell dan Turunannya
```scss
   systemd(1)
 └─ init-systemd(Ub2)
      └─ SessionLeader(313)
           └─ bash(317)
                ├─ head(563)
                └─ pstree(562)
```
Penjelasan:

- `bash(317)` adalah shell login milik user (dalam hal ini: ilham).

- Dari `bash(317)` kemudian dijalankan perintah `pstree(562)` dan `head(563)` sebagai proses anak (child process).
  
kesimpulannya:

 - Proses induk utama: `systemd` dengan PID = 1

 - Peran: Menjadi root dari seluruh hierarki proses di sistem Linux.

 - Contoh turunan langsung: `agetty`, `cron`, `dbus-daemon`, `rsyslogd`, `systemd-logind`, dan lain-lain.

- Proses shell aktif pengguna: `bash(317)` yang menjalankan `pstree` dan `head`.

---

## Analisis
1. Identitas User dan Proses:
Hasil dari eksperimen 2 (menggunakan perintah `ps` dan `top`) menunjukkan bahwa setiap proses yang berjalan di dalam sistem memiliki pemilik atau `USER` tertentu. Pemilikan ini menjadi jembatan antara proses yang dijalankan dengan hak akses pengguna, sehingga sistem mampu menentukan siapa yang berwenang untuk menjalankan, memodifikasi, atau mengakhiri proses tersebut.

2. Siklus Hidup Proses:
Dalam eksperimen 3, diperlihatkan semua tahapan kehidupan sebuah proses. Proses tersebut dibuat dengan menggunakan perintah `sleep 1000 &`, dipantau melalui `ps aux`, dan akhirnya dihentikan dengan menggunakan `kill` . Urutan ini menggambarkan bahwa sistem operasi memberikan mekanisme lengkap bagi pengguna untuk mengendalikan proses-proses mereka, mulai dari penciptaan hingga pengakhiran, sesuai dengan hak akses yang mereka miliki.

3. Hierarki Proses:
Eksperimen 4 dengan perintah `pstree` menunjukkan hubungan antarproses secara hirarkis. Dari hasil tersebut terlihat bahwa semua proses dalam sistem berasal dari satu induk utama, yaitu `systemd` (atau `init` pada sistem yang lebih tua). Proses ini bertanggung jawab untuk memulai dan mengatur semua layanan yang berjalan selama sistem aktif.

Keterkaitan dengan Keamanan:
Pengelolaan pengguna dan keamanan sistem memiliki keterkaitan yang sangat erat. Karena setiap proses dikuasai oleh pengguna tertentu, sistem operasi dapat menerapkan pembatasan keamanan berdasarkan kepemilikan itu. Pengguna biasa, misalnya, tidak memiliki hak untuk menghentikan proses milik pengguna lain atau proses milik `root`. Dengan cara ini, sistem mencegah gangguan atau kerusakan yang dapat membahayakan stabilitas dan keselamatan keseluruhan.

---

## Kesimpulan
Manajemen proses dan user di Linux berfungsi untuk mengatur jalannya proses serta hak akses pengguna agar sistem berjalan stabil, efisien, dan aman. Proses seperti `systemd` mengelola layanan sistem, sedangkan pengaturan user (terutama `root`) menjaga kontrol penuh terhadap konfigurasi dan keamanan sistem.

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux? 
   
   systemd (atau init) adalah tulang punggung sistem Linux yang bertanggung jawab memulai, mengatur, dan menghentikan seluruh proses serta layanan di dalam sistem.
   Tanpa proses ini, sistem operasi tidak akan bisa berjalan dengan normal karena tidak ada layanan dasar yang diinisialisasi.
2. Apa perbedaan antara kill dan killall?
   - kill digunakan untuk menghentikan proses berdasarkan nomor PID.
   - killall digunakan untuk menghentikan semua proses berdasarkan nama program.
3. Mengapa user root memiliki hak istimewa di sistem Linux?
   
   User root memiliki hak istimewa karena berperan sebagai pengelola utama sistem (superuser) yang bertanggung jawab atas seluruh konfigurasi, keamanan, dan pengoperasian sistem Linux.

   Hak istimewa ini penting agar sistem tetap terkendali dan terlindungi dari kesalahan atau akses tidak sah dari user lain.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  Selalu menantang
- Bagaimana cara Anda mengatasinya?  
belajar bersama teman dan melihat tutorial

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
