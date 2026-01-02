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

def page_replacement_lru(reference_string, num_frames):
    """Simulasi algoritma LRU."""
    frames = []
    page_faults = 0
    
    print(f"\n--- LRU: Frames={num_frames} ---")
    print("Reference String:", ', '.join(map(str, reference_string)))

    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) < num_frames:
                # Frame belum penuh, tambahkan saja
                frames.append(page)
            else:
                # Frame penuh, cari yang LRU (index 0, jika frames diurutkan)
                # Di sini, kita asumsikan halaman di index 0 adalah yang LRU saat ini
                frames.pop(0) 
                frames.append(page)
            
            status = "FAULT"
        else:
            status = "HIT"
            # Halaman diakses, pindahkan ke akhir list (Most Recently Used)
            frames.remove(page)
            frames.append(page)
            
        print(f"Akses: {page} | Frames: {frames} | Status: {status}")
        
    return page_faults

if __name__ == "__main__":
    # Sesuai dengan spesifikasi tugas
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    num_frames = 3

    print("\n=======================================================")
    print("        SIMULASI PAGE REPLACEMENT (FIFO & LRU)         ")
    print("=======================================================")

    faults_fifo = page_replacement_fifo(reference_string, num_frames)
    print(f"\nTotal Page Faults (FIFO): {faults_fifo}")

    faults_lru = page_replacement_lru(reference_string, num_frames)
    print(f"\nTotal Page Faults (LRU): {faults_lru}")

    print("\n=======================================================")
    print(f"Perbandingan: FIFO={faults_fifo} Faults, LRU={faults_lru} Faults")
    print("=======================================================\n")