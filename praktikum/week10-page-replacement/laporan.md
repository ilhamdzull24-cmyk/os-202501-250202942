
# Laporan Praktikum Minggu [10]
Topik:  Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah 
- **NIM**   : 250202942 
- **Kelas** : 1IKRB

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dan LRU dalam program.

2. Menjalankan simulasi page replacement dengan reference string dan jumlah frame tertentu.

3. Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.

---

## Dasar Teori
* Memori Virtual: Ini adalah metode yang memungkinkan software untuk menggunakan ruang alamat yang lebih besar daripada yang tersedia dalam memori fisik. Proses ini dilakukan dengan membagi software menjadi unit-unit logis yang dikenal sebagai halaman dan mengintegrasikannya ke dalam unit fisik memori utama yang disebut frame.

* Page Fault: Kejadian ini berlangsung ketika sebuah halaman yang diakses oleh CPU tidak tersedia di memori utama. Bila frame memori telah penuh, sistem operasi harus memilih salah satu halaman dalam memori untuk digantikan.

* FIFO (First-In First-Out): Merupakan algoritma penggantian halaman yang paling dasar, yang memilih halaman yang telah ada di memori untuk waktu paling lama tanpa mempertimbangkan seberapa sering halaman tersebut diakses.

* LRU (Least Recently Used): Ini adalah algoritma yang memilih halaman yang paling lama tidak digunakan untuk diganti. Metode ini biasanya menghasilkan lebih sedikit page fault dibandingkan dengan FIFO.

---

## Langkah Praktikum
1. Menentukan reference string uji: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 dan jumlah frame memori: 3.

2. Mengimplementasikan fungsi simulasi `page_replacement_fifo()` dan `page_replacement_lru()` dalam Python (`page_replacement.py`).

3. Menjalankan program Python untuk kedua algoritma.

4. Mencatat hasil page fault dan page hit dari simulasi.

5. Menyajikan hasil perbandingan dalam tabel di bagian Analisis.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
python3 page_replacement.py

```python
# page_replacement.py
# Simulasi Page Replacement FIFO dan LRU

def page_replacement_fifo(reference_string, num_frames):
    """Simulasi algoritma FIFO."""
    frames = []
    page_faults = 0
    
    print(f"\n--- FIFO: Frames={num_frames} ---")
    print("Reference String:", ', '.join(map(str, reference_string)))

    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                # Frame belum penuh, tambahkan saja
                frames.append(page)
            else:
                # Frame penuh, ganti halaman yang paling lama (index 0)
                frames.pop(0)
                frames.append(page)
            
            status = "FAULT"
        else:
            status = "HIT"
            
        print(f"Akses: {page} | Frames: {frames} | Status: {status}")

    return page_faults
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-12-24%20102234.png)
![Screenshot hasil](./screenshots/Screenshot%202025-12-24%20102315.png)
---

## Analisis
Berdasarkan hasil eksekusi program simulasi dengan reference string:
`7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`

| Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | Halaman yang masuk pertama akan diganti pertama. |
   | LRU | 9 | Halaman yang paling lama tidak diakses akan diganti. |

---

1. Makna Hasil Percobaan: Jumlah kesalahan halaman yang ditunjukkan oleh LRU (9) ternyata lebih rendah dibandingkan dengan FIFO (10). Ini menunjukkan bahwa LRU memiliki keunggulan dalam penggunaan memori frame terhadap string referensi yang ada.

2. Hubungan dengan Teori (Fungsi Kernel): Algoritma penggantian halaman merupakan elemen penting dalam modul manajemen memori di kernel sistem operasi. Kernel memiliki tanggung jawab untuk menerapkan algoritma ini saat terjadi kesalahan halaman guna menentukan halaman mana yang harus dikeluarkan dari memori fisik, yang berdampak besar terhadap kinerja sistem keseluruhannya.

3. Perbedaan Hasil: Jumlah kesalahan halaman yang berbeda disebabkan oleh prinsip penggantian yang berbeda.

   * FIFO hanya memperhatikan urutan kedatangan halaman. Halaman 7 yang datang lebih awal akan diganti terlebih dahulu, meskipun mungkin baru saja diakses kembali (seperti yang terlihat pada frame ke-4, 2 menggantikan 7).

   * LRU mempertimbangkan waktu terakhir halaman diakses. Algoritma ini meningkatkan locality of reference (kecenderungan proses untuk mengakses halaman yang baru saja diakses).


---

## Kesimpulan
* LRU menghasilkan jumlah page fault yang lebih sedikit (9) dibandingkan FIFO (10) untuk reference string uji, membuktikan bahwa LRU lebih efisien dalam meminimalkan operasi I/O yang mahal.

* Kedua algoritma, meskipun memiliki kompleksitas implementasi yang berbeda, adalah mekanisme inti dalam Manajemen Memori Virtual kernel untuk mengatasi Page Fault dan mengoptimalkan penggunaan memori fisik.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?  
   
   FIFO itu mengganti halaman yang paling duluan masuk ke memori sesuai urutan kedatangannya. Sementara itu, LRU mengganti halaman yang paling lama tidak terpakai berdasarkan kapan terakhir kali halaman itu diakses.
  
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?  
   
   Belady's Anomaly itu keadaan aneh saat nambahin slot memori (misalnya dari 3 jadi 4) malah bikin lebih sering terjadi page fault. FIFO gampang kena ini sebab dia tidak melihat bagaimana halaman itu dipakai sebelumnya atau nanti, jadi nambah slot malah bisa mengganti halaman yang sebenarnya masih sering dipakai.  
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?  
   
   LRU itu dasarnya pakai prinsip kedekatan referensi, yang artinya halaman yang baru saja dipakai kemungkinan besar akan dipakai lagi sebentar lagi. Dengan mengganti halaman yang paling lama nganggur, LRU lebih jago menyimpan halaman yang sering dipakai tetap di memori, hasilnya page fault jadi berkurang.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
