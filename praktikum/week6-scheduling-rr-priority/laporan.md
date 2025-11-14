
# Laporan Praktikum Minggu [6]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling  

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah  
- **NIM**   : 250202942 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.
---

## Dasar Teori
Round Robin merupakan algoritma penjadwalan yang sifatnya preemptive, mengandalkan konsep Time Quantum (irisan waktu) untuk secara seimbang mendistribusikan waktu CPU ke setiap proses dalam daftar siap.

Prinsip Utama

* Setiap proses menerima alokasi CPU dalam periode waktu yang sudah ditentukan (time quantum).

* Apabila proses belum rampung saat time quantum berakhir, proses tersebut akan dihentikan, dikembalikan ke antrian siap, dan CPU diserahkan kepada proses berikutnya.

* Seluruh proses diperlakukan dengan cara yang adil (pembagian yang seimbang).

Tujuan RR

* Mengurangi waktu tunggu respons.

* Efektif dalam sistem yang berbagi waktu di mana banyak pengguna membutuhkan tanggapan yang cepat.

Karakteristik

* Mudah dan adil.

* Kinerja sangat tergantung pada pemilihan time quantum:

   * Terlalu kecil → akan menyebabkan terlalu banyak pergantian konteks (beban yang tinggi).

  * Terlalu besar → mirip dengan FCFS (tanggapan yang lambat).

Priority Scheduling adalah metoda penjadwalan yang memberikan CPU kepada proses berdasar pada prioritasnya. Proses dengan prioritas yang lebih tinggi akan mendapat eksekusi terlebih dahulu.

Tipe Algoritma

* Non-preemptive: proses yang sedang berjalan akan dibiarkan sampai selesai tanpa gangguan.

* Preemptive: proses baru dengan prioritas lebih tinggi bisa menghentikan proses yang saat ini sedang berjalan.

Tujuan

* Memprioritaskan pelaksanaan proses yang penting atau mendesak.

* Memastikan respons lebih cepat untuk proses yang krusial.

Kelemahan – Starvation

Proses dengan prioritas rendah mungkin tidak pernah mendapatkan CPU jika selalu ada proses ber-prioritas tinggi yang aktif → starvation.
Solusi yang biasa digunakan: aging, yaitu dengan meningkatkan prioritas proses yang telah menunggu terlalu lama.

Karakteristik

* Fleksibel (dapat menggunakan parameter eksternal: tenggat waktu, I/O-bound vs CPU-bound).

* Tidak seadil RR karena lebih menekankan pada urutan prioritas.
---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```
 WT[i] = waktu mulai eksekusi - Arrival[i]
 TAT[i] = WT[i] + Burst[i]

```
---

## Hasil Eksekusi
* Tabel Round Robin (RR) & Priority Scheduling
  
![Screenshot hasil](./screenshots/Screenshot%202025-11-11%20182754.png)

### Eksperimen 1 Round Robin (RR)

* Tabel Round Robin(RR)
  
![Screenshot hasil](./screenshots/Screenshot%202025-11-11%20182810.png)

* Gant Chart FCFS:
```Bash
  | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P4 |
0    3    6   9   12   15    18   21  24 
```
### Eksperimen 2 Priorty Scheduling

* Tabel Priorty Scheduling
  
![Screenshot hasil](./screenshots/Screenshot%202025-11-11%20182824.png)

* Gant Chart FCFS:
```Bash
| P1 | P2 | P4 | P3 |
0    5    8   14   22
```
### Tabel Perbandingan

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| RR | 11,75 | 12,5 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
| Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |


---

## Analisis

Jadwal Prioritas memiliki durasi tunggu dan putaran yang lebih sedikit dibandingkan dengan Round Robin, sehingga efisiensi waktu lebih baik dalam situasi tersebut.

Dampak Time Quantum (pada Round Robin)

* Time Quantum ialah durasi maksimum yang diberikan CPU pada setiap proses sebelum berganti ke proses berikutnya.

* Apabila time quantum terlalu kecil, CPU sering mengalami pergantian konteks → biaya overhead tinggi → mengurangi efisiensi.

* Jika time quantum terlalu besar, RR akan bertindak seperti FCFS (First Come First Served) → proses yang lebih panjang menguasai CPU → waktu tunggu untuk proses kecil menjadi lebih lama.

Dampak Prioritas (pada Priority Scheduling)

* Algoritma ini menjalankan proses berdasarkan urutan prioritas (semakin tinggi prioritinya, semakin cepat diproses).
  * Akibatnya:
    - Proses yang penting atau mendesak  diselesaikan lebih cepat (Waktu Tunggu dan Waktu Penyelesaian rendah untuk proses dengan prioritas tinggi).
    - Akan tetapi, kemungkinan terjadinya kelaparan bisa muncul: proses dengan prioritas lebih rendah dapat tertunda cukup lama jika proses dengan prioritas tinggi terus muncul.
  

---

## Kesimpulan
Kesimpulannya:

• Round Robin sesuai untuk sistem berbagi waktu atau interaktif, karena memberikan keadilan bagi semua proses.

• Priority Scheduling tepat untuk sistem real-time atau batch, di mana krusial untuk menyelesaikan tugas yang penting lebih cepat.

• Pemilihan time quantum yang baik dan kebijakan prioritas yang adil sangat berpengaruh pada kinerja keseluruhan sistem.


---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
   
   Round Robin memberikan alokasi waktu CPU secara bergantian dengan batas waktu tertentu, sehingga setiap proses mendapatkan peluang yang seimbang.

   Priority Scheduling menjalankan proses berdasarkan urutan prioritas, memprioritaskan yang paling penting, sehingga tugas-tugas penting selesai lebih cepat, meskipun hal ini dapat menyebabkan tugas dengan prioritas lebih rendah terjebak dalam penantian yang lama.

2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?
   
   Jika time quantum terlalu kecil:

   - CPU sering beralih antar proses terlalu sering.

   - Beban kerja meningkat → sistem menjadi kurang efisien.

   - Namun, respons sistem menjadi cepat, ideal untuk sistem yang interaktif.

   Jika time quantum terlalu besar:

   - Setiap proses akan memegang CPU lebih lama, mengakibatkan proses lainnya harus menunggu.

   - RR akan berfungsi mirip dengan FCFS (First Come First Served).

   - Waktu respons menjadi lambat → kurang adil bagi proses yang lebih kecil.

3. Mengapa algoritma Priority dapat menyebabkan starvation?
   
   Algoritma Priority Scheduling berpotensi menyebabkan kelaparan proses karena tugas dengan prioritas rendah terus-menerus tertunda jika ada tugas dengan prioritas lebih tinggi yang terus masuk ke dalam antrian.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
