
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock
---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah 
- **NIM**   : 250202942  
- **Kelas** : 1IKRB

---

## Tujuan
Praktikum ini dibuat dengan tujuan agar kita bisa lebih memahami bagaimana deadlock terdeteksi pada sistem operasi. Caranya adalah dengan menjalankan simulasi program sederhana. Selain itu, kita juga akan belajar menganalisis penyebab terjadinya deadlock secara logis, berdasarkan bagaimana sumber daya dialokasikan dan diminta.


---

## Dasar Teori
Deadlock merupakan situasi di mana dua atau lebih proses saling menantikan sumber daya sehingga tidak ada yang bisa melanjutkan pelaksanaan. Identifikasi deadlock dilakukan setelah kondisi ini terjadi, bertentangan dengan upaya pencegahan dan peminimalan. Prosedur untuk mendeteksi deadlock berfungsi dengan mengevaluasi adanya siklus ketergantungan antara proses dan sumber daya. Ketika tidak ada proses yang bisa diselesaikan, maka sistem berada dalam keadaan deadlock.

---

## Langkah Praktikum
1. Menyusun dataset proses, allocation, dan request resource.

2. Membuat program Python untuk mendeteksi deadlock.

3. Menjalankan simulasi menggunakan dataset uji.

4. Membandingkan hasil simulasi dengan analisis manual.

5. Menyusun laporan hasil praktikum dalam `laporan.md`.

6. Commit & Push

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah

Program dibuat pada file `code/deadlock_detection.py` 
dan dataset berada pada `code/dataset_deadlock.csv`.

Tuliskan potongan kode atau perintah utama:
```python
# deadlock_detection.py

processes = ["P1", "P2", "P3"]

allocation = {
    "P1": ["R1"],
    "P2": ["R2"],
    "P3": ["R3"]
}

request = {
    "P1": ["R2"],
    "P2": ["R3"],
    "P3": ["R1"]
}

available = []  # tidak ada resource bebas
finish = {p: False for p in processes}

changed = True
while changed:
    changed = False
    for p in processes:
        if not finish[p]:
            if all(r in available for r in request[p]):
                finish[p] = True
                available.extend(allocation[p])
                changed = True

deadlock_processes = [p for p in processes if not finish[p]]

if deadlock_processes:
    print("Deadlock terdeteksi pada proses:", deadlock_processes)
else:
    print("Tidak terjadi deadlock")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil Deteksi Deadlock](./screenshots/Screenshot%202025-12-26%20074811.png)

Hasil dari simulasi menunjukkan bahwa tidak ada satu pun proses yang dapat diselesaikan hingga akhir karena tiap proses menunggu sumber daya yang sedang dipegang oleh proses lainnya. Sebagai akibatnya, sistem teridentifikasi berada dalam situasi deadlock.

---

## Analisis

| Proses | Resource Dialokasikan | Resource Diminta | Status Proses |
| :----: | :-------------------: | :--------------: | :-----------: |
|   P1   |           R1          |        R2        |    Deadlock   |
|   P2   |           R2          |        R3        |    Deadlock   |
|   P3   |           R3          |        R1        |    Deadlock   |


Berdasarkan hasil simulasi deteksi deadlock, seluruh proses (P1, P2, dan P3) teridentifikasi berada dalam kondisi deadlock. Karena kondisi ini memenuhi keempat syarat yaitu :

* Mutual Exclusion → Resource hanya dapat digunakan satu proses.

* Hold and Wait → Proses menahan resource sambil menunggu resource lain.

* No Preemption → Resource tidak dapat diambil paksa.

* Circular Wait → Terjadi siklus P1 → P2 → P3 → P1.

Setiap proses memegang satu sumber daya dan secara bersamaan meminta sumber daya lainnya yang sedang digunakan oleh proses lain. Situasi ini menciptakan siklus ketergantungan, di mana P1 menunggu R2 yang dimiliki oleh P2, P2 menunggu R3 yang dikuasai oleh P3, dan P3 menunggu R1 yang dimiliki oleh P1. Karena tidak ada sumber daya yang dapat diakses, tidak ada proses yang bisa diselesaikan, sehingga algoritma deteksi mengindikasikan bahwa sistem terjebak dalam keadaan deadlock. Hasil ini sejalan dengan analisis manual dan sejalan dengan teori deadlock dalam sistem operasi.

---

## Kesimpulan
1. Deadlock dapat dideteksi dengan menganalisis hubungan alokasi dan permintaan resource.

2. Simulasi menunjukkan hasil yang konsisten dengan perhitungan manual.

3. Deteksi deadlock penting untuk sistem yang tidak menerapkan pencegahan deadlock.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection? 
    
   Prevention mencegah deadlock sejak awal, avoidance menghindari kondisi tidak aman, sedangkan detection mendeteksi deadlock setelah terjadi.

2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   
   karena  tidak setiap sistem dapat menerapkan metode untuk mencegah atau menghindari terjadinya deadlock.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
  
   Kelebihan sistem ini adalah adanya fleksibilitas dan efisiensi, sementara kekurangannya mencakup kebutuhan untuk mengelola overhead serta menangani pemulihan dari deadlock.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  
- Bagaimana cara Anda mengatasinya?  


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
