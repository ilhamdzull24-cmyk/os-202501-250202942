
# Laporan Praktikum Minggu [13]
Topik:  Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Ilham Dzufikar Barokah 
- **NIM**   : 250202942 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
1. Docker Container adalah teknologi virtualisasi berbasis OS-level yang memungkinkan aplikasi berjalan secara terisolasi dengan overhead lebih ringan dibandingkan virtual machine.  
2. Resource Limit pada Docker digunakan untuk membatasi pemakaian CPU dan memori agar satu container tidak menghabiskan seluruh sumber daya host.  
3. CPU Limit mengatur jatah waktu eksekusi CPU yang dapat digunakan container, misalnya dengan opsi `--cpus`.  
4. Memory Limit membatasi jumlah memori maksimum yang dapat digunakan container menggunakan opsi `--memory`.  
5. Docker memanfaatkan mekanisme control groups (cgroups) pada Linux untuk mengelola dan membatasi resource setiap container.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
Program Uji Resource (Python)
```python
import time
import sys
import psutil
import os

def print_system_info():
    """Menampilkan informasi sistem"""
    print("=" * 60)
    print("INFORMASI SISTEM")
    print("=" * 60)
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"Memory Total: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Memory Available: {psutil.virtual_memory().available / (1024**3):.2f} GB")
    print("=" * 60)
    print()

def cpu_intensive_task(duration=10):
    """Task yang menggunakan CPU secara intensif"""
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    iterations = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika untuk membebani CPU
        result = sum([i**2 for i in range(1000)])
        iterations += 1
        
        # Tampilkan progress setiap 2 detik
        elapsed = time.time() - start_time
        if int(elapsed) % 2 == 0 and elapsed - int(elapsed) < 0.1:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            print(f"  Progress: {elapsed:.1f}s | Iterasi: {iterations} | CPU: {cpu_percent}%")
    
    end_time = time.time()
    print(f"[CPU TEST] Selesai! Total iterasi: {iterations}")
    print(f"[CPU TEST] Waktu eksekusi: {end_time - start_time:.2f} detik")
    print()
    return iterations

def memory_intensive_task(target_mb=200, chunk_mb=50):
    """Task yang mengalokasikan memori secara bertahap"""
    print(f"[MEMORY TEST] Memulai alokasi memori hingga {target_mb} MB...")
    print(f"[MEMORY TEST] Chunk size: {chunk_mb} MB")
    
    data_arrays = []
    allocated = 0
    
    try:
        while allocated < target_mb:
            # Alokasi chunk memori (dalam MB)
            chunk_size = min(chunk_mb, target_mb - allocated)
            # Buat array berisi angka (sekitar 1MB = 125000 integer 64-bit)
            array_size = int(chunk_size * 125000)
            new_data = list(range(array_size))
            data_arrays.append(new_data)
            allocated += chunk_size
            
            # Informasi memori saat ini
            mem = psutil.virtual_memory()
            mem_used = (mem.total - mem.available) / (1024**2)
            mem_percent = mem.percent
            
            print(f"  Alokasi: {allocated} MB | Memory Used: {mem_used:.1f} MB | Usage: {mem_percent}%")
            time.sleep(0.5)
        
        print(f"[MEMORY TEST] Berhasil mengalokasikan {allocated} MB")
        print(f"[MEMORY TEST] Total arrays: {len(data_arrays)}")
        
    except MemoryError:
        print(f"[MEMORY TEST] ERROR: Kehabisan memori pada {allocated} MB!")
        print(f"[MEMORY TEST] Container memory limit tercapai!")
    except Exception as e:
        print(f"[MEMORY TEST] ERROR: {type(e).__name__}: {e}")
    
    print()
    return allocated

def main():
    print("\n" + "=" * 60)
    print("DOCKER RESOURCE LIMIT TEST")
    print("Praktikum Minggu 13 - Sistem Operasi")
    print("=" * 60)
    print()
    
    # Tampilkan informasi sistem
    print_system_info()
    
    # Test CPU
    print("[1] PENGUJIAN CPU")
    print("-" * 60)
    cpu_iterations = cpu_intensive_task(duration=10)
    
    # Test Memory
    print("[2] PENGUJIAN MEMORI")
    print("-" * 60)
    memory_allocated = memory_intensive_task(target_mb=200, chunk_mb=50)
    
    # Ringkasan
    print("=" * 60)
    print("RINGKASAN HASIL")
    print("=" * 60)
    print(f"CPU Test - Total Iterasi: {cpu_iterations}")
    print(f"Memory Test - Total Alokasi: {memory_allocated} MB")
    print("=" * 60)
    print("\n[INFO] Program selesai dijalankan.")

if __name__ == "__main__":
    main()
   ```

```bash
cd praktikum/week13-docker-resource-limit/code
docker build -t week13-resource-limit .
docker run --rm week13-resource-limit
docker run --rm --cpus="0.5" week13-resource-limit
docker run --rm --memory="256m" week13-resource-limit
docker run --rm --memory="128m" week13-resource-limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
# Terminal 1: Jalankan container tanpa --rm
docker run --name test-limit --cpus="0.5" --memory="256m" week13-resource-limit

# Terminal 2: Monitor
docker stats test-limit
```

---

## Hasil Eksekusi

Sertakan screenshot hasil percobaan atau diagram:
1. Build Docker Image
```bash
cd praktikum/week13-docker-resource-limit/code
docker build -t week13-resource-limit .
```
![Screenshot hasil](./screenshots/Build%20Docker%20Image.png)

2. Eksekusi Tanpa Limit Resource
```bash
docker run --rm week13-resource-limit
```
![Screenshot hasil](./screenshots/Eksekusi%20Tanpa%20Limit%20Resource%201.png)
![Screenshot hasil](./screenshots/Eksekusi%20Tanpa%20Limit%20Resource%202.png)

3. Eksekusi Dengan Limit CPU (--cpus="0.5")
```bash
docker run --rm --cpus="0.5" week13-resource-limit
```
![Screenshot hasil](./screenshots/Eksekusi%20Dengan%20Limit%20CPU%20(--cpus=0.5)%201.png)
![Screenshot hasil](./screenshots/Eksekusi%20Dengan%20Limit%20CPU%20(--cpus=0.5)%202.png)

4.  Eksekusi Dengan Limit Memory (--memory="256m")
```bash
docker run --rm --memory="256m" week13-resource-limit
```
![Screenshot hasil](./screenshots/Eksekusi%20Dengan%20Limit%20Memory%20(--memory=256m)%201.png)

5. Eksekusi Dengan Limit Memory Ketat (--memory="128m")
```bash
docker run --rm --memory="128m" week13-resource-limit
```
![Screenshot hasil](./screenshots/Eksekusi%20Dengan%20Limit%20Memory%20Ketat%20(--memory=128m).png)

6. Eksekusi Dengan Limit CPU dan Memory
```bash
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
![Screenshot hasil](./screenshots/Eksekusi%20Dengan%20Limit%20CPU%20dan%20Memory.png)

7. Monitoring dengan docker stats
```bash
# Terminal 1: Jalankan container tanpa --rm
docker run --name test-limit --cpus="0.5" --memory="256m" week13-resource-limit

# Terminal 2: Monitor
docker stats test-limit
```
![Screenshot hasil](./screenshots/Monitoring%20dengan%20docker%20stats.png)

---

## Analisis
* Analisis Resource Limit pada Docker

Docker membatasi penggunaan CPU dan memori container menggunakan mekanisme control groups (cgroups) yang disediakan oleh Linux. Dengan cgroups, sistem operasi dapat mengatur berapa banyak sumber daya yang boleh digunakan oleh sebuah container agar tidak mengganggu proses lain di host.

* Mekanisme Pembatasan CPU

Ketika container dijalankan dengan opsi --cpus="0.5", Docker membatasi penggunaan CPU hingga 50%. Artinya, dalam satu periode waktu tertentu, container hanya boleh menggunakan setengah dari waktu CPU yang tersedia. Dampaknya, aplikasi tetap berjalan normal tetapi lebih lambat dibandingkan saat tidak diberi batasan. Semakin kecil nilai CPU yang diberikan, semakin rendah performa aplikasi yang dihasilkan.

* Mekanisme Pembatasan Memori

Saat opsi --memory="256m" digunakan, container hanya diizinkan menggunakan memori maksimal 256 MB. Jika aplikasi mencoba menggunakan memori lebih dari batas tersebut, kernel akan menolak alokasi tambahan. Apabila aplikasi terus memaksa, sistem akan menghentikan proses menggunakan mekanisme Out of Memory (OOM) Killer, dan container akan berhenti secara otomatis. Mekanisme ini penting untuk mencegah sistem host kehabisan memori.

* Isolasi Container

Selain pembatasan resource, Docker juga menggunakan namespace untuk mengisolasi container. Dengan namespace, setiap container memiliki proses, jaringan, hostname, dan sistem file sendiri, sehingga tidak saling mempengaruhi meskipun berjalan di host yang sama.

* Analisis Hasil Pengujian

Hasil pengujian menunjukkan bahwa pembatasan CPU menyebabkan penurunan performa aplikasi secara langsung dan proporsional. Aplikasi tetap berjalan, namun jumlah pekerjaan yang dapat diselesaikan menjadi lebih sedikit. Pada pengujian memori, aplikasi dapat berjalan normal selama penggunaan memori masih di bawah batas yang ditentukan, tetapi akan dihentikan ketika melewati limit.

* Perbandingan Container dan Virtual Machine

Container memiliki overhead yang jauh lebih kecil dibandingkan virtual machine karena tidak memerlukan sistem operasi tamu. Hal ini membuat container lebih cepat dijalankan dan lebih efisien dalam penggunaan resource. Namun, virtual machine memiliki isolasi yang lebih kuat karena berjalan di atas hypervisor dengan kernel terpisah.

* Implikasi Praktis

Pembatasan resource sangat penting pada lingkungan produksi untuk mencegah satu aplikasi menghabiskan seluruh sumber daya server. Dengan resource limit, sistem menjadi lebih stabil, aman, dan efisien. Selain itu, pembatasan yang tepat dapat membantu menghemat biaya infrastruktur, terutama pada lingkungan cloud.

---

## Kesimpulan
Docker resource limit bekerja efektif dalam mengontrol penggunaan CPU dan memori container. Pembatasan CPU mempengaruhi kecepatan aplikasi, sedangkan pembatasan memori mencegah aplikasi merusak stabilitas sistem. Oleh karena itu, penerapan resource limit merupakan praktik yang wajib dilakukan dalam pengelolaan container di lingkungan nyata.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?  
Container perlu dibatasi CPU dan memori karena beberapa alasan penting:
* Mencegah Resource Starvation: Tanpa limit, satu container dapat menghabiskan seluruh resource host dan membuat container lain atau sistem host menjadi tidak responsif.
* Multi-tenancy: Dalam lingkungan production dengan banyak container, pembatasan resource memastikan setiap container mendapat alokasi yang adil (fair sharing).
* Stabilitas Sistem: Membatasi resource mencegah satu aplikasi yang bermasalah (memory leak, infinite loop) mengganggu keseluruhan sistem.
* Predictability: Dengan limit yang jelas, kita dapat memprediksi perilaku aplikasi dan merencanakan kapasitas server dengan lebih baik.
* Cost Optimization: Di cloud environment, pembatasan resource membantu mengoptimalkan biaya dengan memastikan container tidak over-provisioned.
* Keamanan: Mencegah serangan DoS (Denial of Service) di mana attacker mencoba menghabiskan resource sistem.

2.  Apa perbedaan VM dan container dalam konteks isolasi resource?    
VM memiliki isolasi penuh hingga level hardware melalui hypervisor, sedangkan container berbagi kernel host dengan isolasi berbasis cgroups dan namespaces.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
Dampak limit memori terhadap aplikasi yang boros memori:

* OOM Killer (Out of Memory Killer)

  - Ketika aplikasi mencoba mengalokasikan memori melebihi limit, Linux kernel akan mengaktifkan OOM Killer
  - Container akan dihentikan secara paksa (killed) dengan exit code 137
  - Data yang belum tersimpan akan hilang

* Performance Degradation

  - Sebelum mencapai limit, sistem akan melakukan swapping (jika swap diaktifkan)
  - Swapping sangat lambat karena menggunakan disk, menyebabkan aplikasi menjadi sangat lambat
  - Aplikasi mungkin mengalami timeout atau hang

* Allocation Failure

  - Aplikasi menerima MemoryError atau allocation failure
  - Jika tidak ada error handling yang baik, aplikasi akan crash
  - Perlu implement graceful degradation

* Garbage Collection Overhead

  - Pada bahasa dengan GC (Java, Python, Go), GC akan lebih sering berjalan
  - GC pause dapat meningkat drastis mendekati memory limit
  - Throughput aplikasi menurun

* Best Practices:

  - Monitor memory usage menggunakan metrics dan alerting
  - Implement memory pooling dan caching yang efisien
  - Set memory limit dengan buffer (biasanya 1.5-2x expected usage)
  - Gunakan memory request dan limit di orchestration (Kubernetes)
  - Optimize aplikasi untuk mengurangi memory footprint  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
