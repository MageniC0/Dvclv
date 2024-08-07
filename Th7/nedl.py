import json
with open("Th7","r") as file: qua = json.load(file)
n = input("输入坐标\033[94m_")
with open(qua+f"{n}"+".json","r") as file: data = json.load(file)
print(data)