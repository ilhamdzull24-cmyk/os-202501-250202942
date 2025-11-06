
# Laporan Praktikum Minggu [5]
Topik: Penjadwalan CPU FCFS dan SJF

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah  
- **NIM**   : 250202942 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
Penjadwalan CPU merupakan suatu mekanisme dalam sistem operasi yang berfungsi untuk menentukan urutan proses yang akan dilaksanakan oleh CPU. Mengingat bahwa jumlah proses umumnya lebih banyak dibanding dengan jumlah CPU, sistem operasi harus memutuskan proses mana yang akan dijalankan lebih dahulu agar penggunaan CPU dapat dilakukan secara efisien dan mengurangi waktu tunggu bagi proses.

- FCFS berlandaskan pada teori antrian, di mana proses-proses akan disusun dalam urutan kedatangan. Proses yang tiba lebih awal akan mendapatkan giliran lebih dahulu untuk dilayani oleh CPU, mirip dengan cara kerja sistem pelayanan di kasir.

- SJF berasumsi bahwa total rata-rata waktu tunggu dapat diminimalkan jika proses dengan waktu eksekusi paling singkat dikerjakan terlebih dahulu. Secara matematis, SJF telah terbukti memberikan waktu tunggu rata-rata yang paling efisien dibandingkan dengan algoritma lain — hal ini dikenal sebagai "teorema penjadwalan optimal" dalam ranah teori antrian.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
 ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-11-05%20162016.png)

### Eksperimen 1 – FCFS (First Come First Served)

- Gantt Chart FCFS:
   ```
   | P1 | P2 | P3 | P4 |
   0    6    14   21   24
   ```
 - Tabel Perhitungan FCFS:
  ![Screenshot hasil](./screenshots/Screenshot%202025-11-05%20162127.png)

  ### Eksperimen 2 – SJF (Shortest Job First)

  - Gantt Chart SJF:
   ```
   | P1 | P4 | P3 | P2 |
   0    6    9    16   24
   ```
  - Tabel Perhitungan SJF:
  ![Screenshot hasil](./screenshots/Screenshot%202025-11-05%20162146.png)

  ### Eksperimen 3 - Perbandingan FCFS & SJF

   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
   | :--- | :--- | :--- | :--- | :--- |
   | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
   | SJF | 6,25 | 12,25	| Optimal untuk job pendek | Menyebabkan starvation pada job panjang |

---

### Analisis

| Algoritma | Rata-rata WT | Rata-rata TAT |
| --------- | ------------ | ------------- |
| **FCFS**  | 8,75         | 14,75         |
| **SJF**   | 6,25         | 12,25         |

SJF lebih efisien, karena menghasilkan waktu tunggu dan turnaround lebih kecil.

- SJF lebih unggul ketika:

  - Burst time tiap proses diketahui atau bisa diperkirakan.

  - Banyak proses pendek → mengurangi waktu tunggu rata-rata.

  - Tujuan utama adalah efisiensi CPU.

- FCFS lebih unggul ketika:

  - Burst time tidak diketahui.

  - Keadilan (fairness) lebih penting daripada efisiensi.

  - Ingin menghindari starvation (proses panjang tidak diabaikan).
---

## Kesimpulan
Perhitungan Waiting Time (WT) dan Turnaround Time (TAT) bisa dilakukan dengan cara sistematis untuk menilai kinerja setiap algoritma penjadwalan.

Algoritma FCFS (First Come First Served) merupakan yang paling mudah untuk diterapkan, tetapi sangat tidak efisien jika proses-proses pendek datang setelah proses panjang, karena mengakibatkan "convoy effect" dan waktu tunggu rata-rata yang tinggi.

Di sisi lain, algoritma SJF (Shortest Job First) terbukti paling optimal dalam situasi ini, menghasilkan waktu tunggu dan waktu putar balik rata-rata yang paling rendah dengan mengutamakan proses yang memiliki durasi eksekusi terpendek terlebih dahulu.

Pemilihan algoritma penjadwalan berpengaruh langsung terhadap kemampuan sistem dalam merespon, efisiensi, dan keadilan. SJF sangat unggul dalam hal efisiensi dan throughput sistem, terutama dalam beban kerja yang dapat diprediksi, sementara FCFS lebih menonjol dalam kesederhanaan, keadilan, dan stabilitas sistem karena tidak menyebabkan starvation dan mudah diterapkan pada berbagai jenis sistem operasi.

Oleh karena itu, pilihan algoritma harus disesuaikan dengan tujuan serta karakteristik sistem yang digunakan, baik lebih berfokus pada efisiensi waktu atau keadilan dalam memberikan pelayanan kepada proses.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   
   FCFS (First Come First Served) berarti bahwa proses yang tiba lebih awal akan ditangani terlebih dahulu, mirip dengan sistem antrean di kasir.
   - Keunggulan: mudah dipahami dan bersifat adil.
   - Kelemahan: proses yang lebih cepat bisa mengalami penundaan yang lama jika ada proses yang lebih panjang di depannya.

   SJF (Shortest Job First) berarti bahwa proses yang membutuhkan waktu paling sedikit akan dikerjakan lebih dahulu.
   - Keunggulan: lebih cepat dan efisien karena rata-rata waktu tunggu lebih rendah.
   - Kelemahan: dapat menyebabkan proses yang lebih lama terus-menerus menunggu.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum? 
   
   SJF menciptakan rata-rata waktu menunggu terendah karena proses yang memiliki waktu eksekusi tercepat dikerjakan terlebih dahulu, sehingga:

   - Proses-proses yang cepat tidak terhambat oleh proses yang lebih lama,

   - Proses-proses selanjutnya menunggu lebih sedikit waktu,

   - Jumlah waktu tunggu untuk semua proses menjadi lebih rendah.

   Jadi SJF mengurangi waktu tunggu rata-rata dengan meminimalisir waktu tunggu dari proses yang lebih singkat dan menyempurnakan urutan pelaksanaan berdasarkan waktu kerja yang paling singkat.
1. Apa kelemahan SJF jika diterapkan pada sistem interaktif?

   Kelemahan SJF pada sistem interaktif adalah:

   - Menentukan durasi eksekusi setiap proses dengan akurat sangatlah sulit padahal SJF memerlukan informasi tersebut guna menyusun urutan.

   - Proses yang lebih lama dapat terus mengalami keterlambatan (starvation) jika selalu ada proses yang lebih singkat datang.

   - Tidak cukup responsif terhadap proses yang baru, sebab proses yang lebih panjang bisa terjebak dan mengurangi pengalaman pengguna.

   - Kurang adaptif untuk sistem yang memerlukan respon cepat, seperti interaksi pengguna atau layanan waktu nyata.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  Selalu menantang karena saya belum cukup menguasai
- Bagaimana cara Anda mengatasinya?  
  belajar bersama teman dan melihat tutorial

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
