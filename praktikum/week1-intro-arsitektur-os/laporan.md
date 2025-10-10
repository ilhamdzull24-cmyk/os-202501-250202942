
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah
- **NIM**   : 250202942
- **Kelas** : 1IKRB

---

## Tujuan  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.


---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/screenshots.terminal%20wsl.png.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  

Evaluasi Performa Sistem

Melalui percobaan, kita bisa melihat seberapa baik sistem menangani tugas-tugas seperti penjadwalan proses, manajemen memori, I/O, dll.

Contoh: Menganalisis waktu tunggu (waiting time), waktu respons (response time), throughput, dll.

Pemahaman Mekanisme Internal

Percobaan membantu memahami bagaimana sistem operasi bekerja di balik layar.

Contoh: Melihat perbedaan kinerja antara algoritma penjadwalan FCFS, SJF, dan Round Robin.

Identifikasi Kelemahan atau Bottleneck

Melalui hasil percobaan, kita bisa mengidentifikasi bagian mana dari sistem yang menyebabkan kinerja menurun.

Contoh: Jika terjadi deadlock atau starvation, percobaan bisa menunjukkan kondisi penyebabnya.

Validasi Teori

Hasil percobaan dapat digunakan untuk membuktikan atau membantah teori yang dipelajari.

Contoh: Mencocokkan hasil simulasi dengan prediksi teoretis algoritma.

Pengambilan Keputusan untuk Implementasi Nyata

Dalam pengembangan software atau sistem, hasil percobaan sistem operasi dapat menjadi dasar pemilihan algoritma yang paling efisien.

Contoh: Memilih algoritma penjadwalan terbaik untuk aplikasi real-time.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
 
 Fungsi Kernel
•	Teori:
Kernel adalah inti dari sistem operasi yang bertugas mengatur seluruh aktivitas pada dasar computer, seperti manajemen proses, memori, file system, dan perangkat I/O.
Menjadi “penghubung langsung” antara perangkat keras (hardware) dan perangkat lunak (software).
•	Hubungan dengan hasil percobaan:
Jika dalam percobaan saat menjalankan program yang membuat proses, mengalokasikan memori, atau mengakses file, maka hasil output (misalnya PID, alokasi memori, waktu eksekusi, atau respon I/O) menunjukkan peran kernel dalam mengatur dan mengendalikan sumber daya tersebut.
Contoh: pada Linux, saat perintah fork() berhasil membuat proses baru, itu berarti kernel menjalankan fungsi manajemen proses dengan benar.
________________________________________
 System Call
•	Teori:
System call adalah jembatan antara program pengguna (user mode) dan kernel (kernel mode).
Melalui system call, aplikasi bisa meminta layanan dari OS seperti membuka file (open()), membuat proses (fork()), atau mengalokasikan memori (malloc() yang pada akhirnya memanggil brk()/mmap() di kernel).
•	Hubungan dengan hasil percobaan:
Ketika kamu melihat hasil berupa output program C yang memanggil system call, log aktivitas proses, atau penggunaan syscall tertentu, maka hasil itu membuktikan bagaimana system call menjadi mekanisme komunikasi utama antara user space dan kernel space.
Contoh: hasil percobaan menunjukkan proses baru dengan PID berbeda → berarti system call fork() berhasil dijalankan oleh kernel.
________________________________________
 Arsitektur Sistem Operasi
•	Teori:
Arsitektur OS menentukan bagaimana komponen OS berinteraksi, misalnya:
o	Monolitik (Linux, Unix): semua layanan inti dijalankan dalam kernel space.
o	Microkernel (Minix, macOS sebagian): fungsi kernel dipisah ke modul-modul kecil, sisanya dijalankan di user space.
o	Hybrid (Windows, Android): gabungan keduanya.
•	Hubungan dengan hasil percobaan:
Jika saat membandingkan hasil di Linux dan Windows, perbedaan output, waktu eksekusi, atau struktur proses mencerminkan perbedaan arsitektur OS-nya.
Contoh:
o	Linux bisa lebih cepat dalam akses sistem karena kernel monolitik → semua layanan berada di satu ruang kernel.
o	Windows mungkin lebih stabil karena arsitektur hybrid dengan pemisahan komponen yang lebih jelas.


- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

 Arsitektur dan Kernel
Aspek	Linux	Windows
Jenis kernel	Monolitik (semua layanan utama seperti manajemen memori, proses, dan sistem file berada di dalam kernel)	Hybrid (gabungan monolitik dan microkernel — beberapa layanan berjalan di user mode untuk keamanan & stabilitas)
Dampak pada hasil percobaan	Hasil percobaan sering menunjukkan akses sistem yang cepat, misalnya saat membuat proses atau membaca file.	Hasil bisa menunjukkan latensi sedikit lebih tinggi, tetapi sistem lebih stabil dan aman.
________________________________________
 System Call dan Mekanisme Eksekusi
Aspek	Linux	Windows
System call	Menggunakan POSIX standard (misal fork(), exec(), read(), write())	Menggunakan Win32 API (misal CreateProcess(), ReadFile(), WriteFile())
Dampak pada hasil percobaan	Output percobaan yang menggunakan fork() hanya berjalan di Linux — menghasilkan dua proses (parent dan child).	Di Windows, tidak ada fork(), jadi hasil berbeda — program harus memakai CreateProcess() dan hasilnya berbeda secara struktur.
________________________________________
 Manajemen Proses
Aspek	Linux	Windows
Identifikasi proses	Menggunakan PID yang ditangani kernel dengan sistem hirarki (parent–child).	Menggunakan process handle dan ID yang tidak selalu hierarkis.
Dampak pada hasil percobaan	Saat menjalankan percobaan fork() → muncul dua proses dengan PID berbeda.	Pada Windows, hasilnya menunjukkan satu proses utama; percabangan hanya terjadi jika dibuat manual dengan API lain.
________________________________________
 Manajemen File dan Direktori
Aspek	Linux	Windows
Sistem file utama	ext4, xfs, btrfs	NTFS, FAT32
Struktur path	Menggunakan / (misal /home/user/file.txt)	Menggunakan \ (misal C:\Users\User\file.txt)
Dampak pada hasil percobaan	Program berbasis UNIX path berjalan normal.	Jika tidak disesuaikan, program bisa gagal karena perbedaan format path.
________________________________________
 Lingkungan Eksekusi dan Perintah
Aspek	Linux	Windows
Shell/Terminal	Bash, zsh, sh	Command Prompt, PowerShell
Dampak pada hasil percobaan	Beberapa perintah (misal ls, ps, grep) hanya ada di Linux → hasil percobaan lengkap.	Perintah setara (dir, tasklist, findstr) menghasilkan format dan detail berbeda.



---

## Kesimpulan
Linux dan Windows, dapat disimpulkan bahwa perbedaan arsitektur kernel, sistem panggilan (system call), dan manajemen sumber daya menyebabkan perbedaan hasil eksekusi program.
Pada sistem Linux, yang menggunakan kernel monolitik dan standar POSIX, percobaan menunjukkan mekanisme kerja sistem operasi secara langsung, seperti proses pembuatan dan pengelolaan proses dengan fork(), pengaturan memori, dan akses file yang transparan.
Sedangkan pada Windows, dengan arsitektur kernel hybrid dan penggunaan Win32 API, hasil percobaan menunjukkan bahwa akses ke fungsi inti sistem lebih terkontrol dan terbatas, sehingga beberapa perintah atau system call dari Linux tidak dapat dijalankan secara langsung.
Secara umum, Linux lebih terbuka untuk eksplorasi konsep dasar sistem operasi, sementara Windows lebih berfokus pada stabilitas, keamanan, dan kompatibilitas aplikasi.
Perbedaan hasil ini menegaskan bahwa setiap sistem operasi memiliki pendekatan berbeda dalam mengelola proses, memori, dan sistem file, sesuai dengan desain arsitekturnya.



---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi. 
   
   Manajemen Sumber Daya (Resource Management)
Mengelola seluruh sumber daya perangkat keras komputer seperti CPU, memori, perangkat penyimpanan, dan perangkat input/output agar dapat digunakan secara efisien oleh berbagai macam program.
Manajemen File (File Management)
Mengatur penyimpanan, pengambilan, penamaan, dan pengorganisasian file di dalam sistem penyimpanan agar pengguna dan program dapat mengakses data dengan mudah dan aman.
Manajemen Proses (Process Management)
Mengelola eksekusi program (proses), meliputi penjadwalan, pembuatan, penghentian, dan sinkronisasi proses, serta memastikan proses berjalan secara terkoordinasi tanpa konflik.
 
2. Jelaskan perbedaan antara kernel mode dan user mode.

Perbedaan antara kernel mode dan user mode adalah salah satu konsep dasar dalam sistem operasi yang berkaitan dengan tingkat hak akses terhadap perangkat keras dan sumber daya sistem. Berikut penjelasan perbedaannya:
Hak Akses
Hak akses Kernel Mode memiliki akses penuh ke seluruh sumber daya system, termasuk perangkat keras, memori, dan instruksi system yang sensitive. 
Dapat menjalankan semua intruksi mesin, termasuk yang dapat mengubah konfigurasi system. Sedangkan
Hak akses User Mode memiliki akses terbatas. Program tidak diizinkan untuk mengakses langsung perangkat keras ataupun memori system inti.
Intruksi yang sensitive tidak boleh dijalankan, jika dicoba maka akan menyebabkan interupsi atau error.
Tujuan Utama
Kernel Mode, Digunakan oleh system operasi dan kode inti, seperti driver perangkat. Dan menjamin control dan keamanan terhadap system.
User Mode, Digunakan oleh aplikasi pengguna, misalnya browser, editor teks. Dan menjaga agar aplikasi tidak merusak system jika terjadi kesalahan.
Peralihan Mode
Peralihan dari user mode ke kernel mode terjadi saat aplikasi memanggil system call (permintaan layanan OS). Dan ada interupsi perangkat keras. Jika
Peralihan dari kernel mode ke user mode terjadi setelah system operasi selesai menangani permintaan dan mengembalikan control ke aplikasi.


3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
 
  Arsitektur Monolithic :
Linux (Ubuntu, Fedora, Debian)
Unix (versi tradisional seperti BSD)
MS-DOS

Arsitektur Microkernel :
Mnix,
QNX,
L4 Microkernel Family,
GNU Hurd


---

## Refleksi Diri
Tuliskan secara singkat:
-   Apa bagian yang paling menantang minggu ini?  
   Menjalankan wsl atau Linux
- Bagaimana cara Anda mengatasinya? 
  
  belajar kepada teman dan melihat tutorial di youtube dll  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
