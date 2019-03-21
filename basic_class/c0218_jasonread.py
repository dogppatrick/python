import json
f = open("pm25.json", "r", encoding="utf-8")
pm_data = json.load(f)
f.close()
for data in pm_data:
    print(data["Site"], data["PM25"])

