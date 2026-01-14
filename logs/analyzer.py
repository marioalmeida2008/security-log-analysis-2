from collections import Counter

failed_ips = []

with open("logs/auth.log") as file:
for line in file:
if "Failed password" in line:
ip = line.split()[-1]
failed_ips.append(ip)

counter = Counter(failed_ips)

print("Failed login attempts:\n")
for ip, count in counter.items():
print(f"{ip}: {count} attempts")

print("\nSuspicious IPs:")
for ip, count in counter.items():
if count >= 2:
print(f"{ip} (possible brute force)")
