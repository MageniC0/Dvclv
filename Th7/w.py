import json,re
with open("Th7","r") as file: qua = json.load(file)
r = True
n = 1

print("\033[94mname      IP         follow")
while r:
    try:
        with open(qua+str(n)+".json","r") as file: data = json.load(file)
        print(f"[{n}]"+"{:<10} {:<5} {:<10}".format(data['name'], data['IP'], data['follow']))
        n = n + 1
    except Exception:
        r = False

print("_")