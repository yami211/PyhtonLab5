
import json

with open("people.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(" Вміст файлу people.json:\n")
for surname, info in data.items():
    print(f"{surname}: {info[0]} {info[1]}, рік народження — {info[2]}")