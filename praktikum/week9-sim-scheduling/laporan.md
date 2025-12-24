
# Laporan Praktikum Minggu [9]
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah 
- **NIM**   : 250202942  
- **Kelas** : 1IKRB

---

## Tujuan
Praktikum ini dirancang untuk membuat mahasiswa dapat menerapkan dan mensimulasikan algoritma penjadwalan CPU melalui perangkat lunak, terutama pada algoritma First Come First Served (FCFS) dan Shortest Job First (SJF) yang bersifat non-preemptive, serta melakukan analisis terhadap hasil simulasi yang meliputi waktu tunggu dan waktu penyelesaian.

---

## Dasar Teori
* CPU Scheduling merupakan cara yang digunakan oleh sistem operasi untuk menentukan urutan pelaksanaan proses di CPU.

* FCFS (First Come First Served) menjalankan proses berdasarkan urutan kedatangan pertama.

* SJF (Shortest Job First) menjalankan proses yang memiliki waktu burst terpendek terlebih dahulu.
Waiting Time adalah lamanya proses menunggu di antrian siap sebelum mulai dieksekusi.

* Turnaround Time adalah total waktu dari ketika proses tiba sampai selesai dieksekusi.

---

## Langkah Praktikum
1. Menyiapkan dataset proses dalam bentuk list di program Python.

2. Mengimplementasikan algoritma FCFS dan SJF non-preemptive.

3. Menghitung waiting time dan turnaround time setiap proses.

4. Menampilkan hasil simulasi dalam bentuk tabel pada terminal.

5. Membandingkan hasil simulasi dengan perhitungan manual.

6. Melakukan commit dan push hasil praktikum ke repositori GitHub.
   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```
---

## Kode / Perintah
Berikut adalah potongan logika utama algoritma FCFS yang saya buat:
```python
# Simulasi Algoritma Penjadwalan CPU
# FCFS 

processes = [
    {"id": "P1", "arrival": 0, "burst": 6},
    {"id": "P2", "arrival": 1, "burst": 8},
    {"id": "P3", "arrival": 2, "burst": 7},
    {"id": "P4", "arrival": 3, "burst": 3},
]

def fcfs(processes):
    time = 0
    result = []
    for p in sorted(processes, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]
        waiting = time - p["arrival"]
        turnaround = waiting + p["burst"]
        time += p["burst"]
        result.append((p["id"], waiting, turnaround))
    return result
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-12-24%20082904.png)

---

## Analisis


---

## Kesimpulan
1. Simulasi mempermudah analisis algoritma penjadwalan CPU dibandingkan perhitungan manual.

2. Algoritma SJF non-preemptive menghasilkan rata-rata waiting time yang lebih kecil dibandingkan FCFS.

3. Implementasi program membantu memahami alur kerja scheduling secara praktis.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 
    
   Simulasi memberikan sarana untuk mengevaluasi algoritma dengan cepat dan tepat pada sejumlah besar proses tanpa perlu melakukan perhitungan secara manual.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   
   Secara teori, hasil yang diperoleh tidak berbeda, tetapi simulasi menawarkan efisiensi yang lebih tinggi, mengurangi kemungkinan kesalahan, dan dapat mengelola volume data yang besar.

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   
   FCFS lebih sederhana untuk diterapkan karena hanya memerlukan pengurutan berdasarkan urutan waktu kedatangan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
