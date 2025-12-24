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

def print_table(title, data):
    print(title)
    print("-" * 45)
    print(f"{'Proses':<10}{'Waiting':<15}{'Turnaround':<15}")
    print("-" * 45)
    total_wait = 0
    total_turn = 0
    for p in data:
        total_wait += p[1]
        total_turn += p[2]
        print(f"{p[0]:<10}{p[1]:<15}{p[2]:<15}")
    n = len(data)
    print("-" * 45)
    print(f"Rata-rata Waiting Time     : {total_wait / n:.2f}")
    print(f"Rata-rata Turnaround Time  : {total_turn / n:.2f}")
    print()

fcfs_result = fcfs(processes)

print_table("=== FCFS Scheduling ===", fcfs_result)

