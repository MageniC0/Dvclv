import json
with open("Th7","w") as file: json.dump(qua,file)
n = input("输入坐标\033[94m_")
with open(n+".json","r") as file: data = json.load(file)
print(data)