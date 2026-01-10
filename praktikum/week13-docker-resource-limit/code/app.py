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