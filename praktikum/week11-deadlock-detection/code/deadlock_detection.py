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
