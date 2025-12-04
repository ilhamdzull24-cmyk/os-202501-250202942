
# Laporan Praktikum Minggu [7]
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas Kelompok
- **Nama Kelompok**  :
1. Miftakhul Lisna Esa Baehaqi (250202951) - (Ketua) - Bagian Implementasi
2. Ilham dzufikar barokah (250202942) - Bagian Dokumentasi
3. Ikhsan mu'arif (250202921) - Bagian analisis
4. Hanif arundaya usman (250202942) - Bagian analisis
   
- Kelas : 1IKRB
  

 


---

## Tujuan

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---


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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
  
- Pengecualian Bersama (persaingan untuk mendapatkan barang):

Ada sumber daya yang hanya bisa digunakan oleh satu orang atau proses saja. Jadi jika satu orang sudah menggunakannya, yang lainnya harus menunggu.

- Menahan dan Menunggu (sudah memiliki barang, masih meminta lebih):

Sebuah proses sudah memiliki satu sumber daya, tetapi masih meminta sumber daya lain. Sementara sumber daya lainnya sedang digunakan oleh proses yang berbeda.

- Tidak Ada Perampasan (barang tidak bisa diambil paksa):

Sumber daya yang sudah digunakan oleh suatu proses tidak boleh diambil secara paksa. Harus menunggu hingga proses tersebut selesai dan mengembalikannya secara sukarela.

- Antrian Melingkar (saling menunggu dalam siklus):

Terjadi keadaan "saling menunggu":
Proses A menunggu sumber daya yang dipegang oleh B, B menunggu C, C menunggu D, dan akhirnya D menunggu A. Hal ini menciptakan lingkaran menunggu.

2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
   
* Menghindari Kekacauan Data (Race Condition)

Ketika dua proses mencoba untuk mengakses dan mengubah data yang sama secara bersamaan, hasilnya bisa menjadi tidak teratur. Sinkronisasi menjamin bahwa hanya satu proses yang dapat mengakses data penting pada satu waktu.

* Memastikan Keberlangsungan Data

Tanpa sinkronisasi, nilai data dapat berubah tanpa sesuai dengan logika program. Contoh: kedua proses dapat menambah saldo, namun hasil akhirnya keliru karena keduanya mengambil nilai yang lama.

* Mengelola Akses ke Sumber Daya Bersama

Beberapa sumber daya seperti file, memori, printer, dan buffer tidak dapat digunakan secara bersamaan. Sinkronisasi membuat proses harus menunggu gilirannya.

* Menghindari Deadlock dan Situasi Macet Lain

Dengan menggunakan mekanisme sinkronisasi yang tepat seperti mutex, semaphore, dan monitor, sistem bisa mencegah kondisi di mana proses saling menunggu dan menyebabkan sistem terhenti.

* Memfasilitasi Eksekusi Paralel yang Aman

Tujuan utama dari multiprogramming dan multicore adalah untuk melaksanakan banyak tugas secara bersamaan. Sinkronisasi memastikan bahwa semua tugas tersebut berjalan dengan aman, teratur, dan tidak merusak data.
     
3. Jelaskan perbedaan antara semaphore dan monitor.  

Semaphore (seperti cara mengantre)

Semaphore adalah seperti mengantre menggunakan nomor.

* Ada angka yang menunjukkan berapa banyak orang yang bisa masuk.

* Jika nomornya masih ada → kamu bisa masuk.

* Jika sudah habis → kamu harus menunggu.

* Kamu sendiri yang harus ingat untuk “mengambil nomor” dan “mengembalikan nomor”.

Kesimpulannya:
Semaphore adalah sistem antrean yang perlu kamu atur sendiri.

Monitor (seperti ruangan dengan pintu otomatis)

Monitor itu seperti ruangan dengan pintu yang mengunci sendiri.

* Hanya satu orang yang dapat masuk.

* Saat kamu masuk, pintunya langsung terkunci otomatis.

* Ketika kamu keluar, pintunya otomatis terbuka.

* Kamu tidak perlu mengurus kuncinya sendiri.

Kesimpulannya:
Monitor adalah sistem yang mengurus kuncinya sendiri, sehingga lebih aman dan mudah.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
