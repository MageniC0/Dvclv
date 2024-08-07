import json
with open('Th7','r') as file:qua=json.load(file)
n = int(input("输入坐标\033[94m_"))
with open(qua+"0.json","w") as file: json.dump(n,file)