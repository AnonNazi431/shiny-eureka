import re
from collections import defaultdict
import csv

LOG_FILE = "auth.log"
OUTPUT_FILE = "bruteforce_report.csv"

pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

attempts = defaultdict(int)

with open(LOG_FILE, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            attempts[ip] += 1

with open(OUTPUT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Attempts"])
    for ip, count in sorted(attempts.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([ip, count])

print(f"[✔] Brute-force report saved to {OUTPUT_FILE}")
