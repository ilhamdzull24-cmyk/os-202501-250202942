import csv

processes = []
allocation = {}
request = {}

with open("dataset_deadlock.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        processes.append(p)
        allocation[p] = [row["Allocation"]]
        request[p] = [row["Request"]]

available = []
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

deadlock = [p for p in processes if not finish[p]]

print("=== HASIL DETEKSI DEADLOCK ===")
if deadlock:
    print("Deadlock terdeteksi pada proses:", deadlock)
else:
    print("Tidak terjadi deadlock")
