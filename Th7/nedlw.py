import json,re
n = int(input("输入坐标\033[94m_"))
with open("Th7","r") as file: qua = json.load(file)

if match := re.match(r"(\w+)\s+(\w+)\s+(\d+)", input("_")):
    name, IP, follow = match.groups()
    follow = int(follow)
    with open(qua+f"{n}"+".json","w") as file : json.dump({"name":name,"IP":IP,"follow":follow},file)

else:
    print("无法分析的输入")