import json,re
with open("n","r") as file: n = json.load(file)

while True:
    inp = input(str(n)+"_")
    
    if match := re.match(r"(\w+)\s+(\w+)\s+(\d+)", inp):
        name, IP, follow = match.groups()
        follow = int(follow)
        with open(str(n)+".json","w") as file : json.dump({"name":name,"IP":IP,"follow":follow},file)
        
        n = n + 1
        with open("n","w") as file: json.dump(n,file)
    
    else:
        break

print("done.")







import json,re
r = True
n = 1

print("\033[94mname      IP         follow")
while r:
    try:
        with open(str(n)+".json","r") as file: data = json.load(file)
        print(f"[{n}]"+"{:<10} {:<5} {:<10}".format(data['name'], data['IP'], data['follow']))
        n = n + 1
    except Exception:
        r = False

print("_")






import json,re
n = int(input("输入坐标\033[94m_"))

if match := re.match(r"(\w+)\s+(\w+)\s+(\d+)", input("_")):
    name, IP, follow = match.groups()
    follow = int(follow)
    with open(str(n)+".json","w") as file : json.dump({"name":name,"IP":IP,"follow":follow},file)

else:
    print("无法分析的输入")








import json
n = input("输入坐标\033[94m_")
with open(n+".json","r") as file: data = json.load(file)
print(data)






import json
n = int(input("输入坐标\033[94m_"))
with open("n","w") as file: json.dump(n,file)







dic = {
    "澳门": "AM",
    "安徽": "AH",
    "北京": "BJ",
    "重庆": "CQ",
    "福建": "FJ",
    "甘肃": "GS",
    "广东": "GD",
    "广西": "GX",
    "贵州": "GZ",
    "海南": "HI",
    "河北": "HEB",
    "黑龙江": "HLJ",
    "河南": "HE",
    "湖北": "HB",
    "湖南": "HN",
    "吉林": "JL",
    "江苏": "JS",
    "江西": "JX",
    "辽宁": "LN",
    "内蒙古": "NMG",
    "宁夏": "NX",
    "青海": "QH",
    "山东": "SD",
    "四川": "SC",
    "上海": "SH",
    "陕西": "SN",
    "山西": "SX",
    "天津": "TJ",
    "台湾": "TW",
    "西藏": "XZ",
    "新疆": "XJ",
    "香港": "XG",
    "云南": "YN",
    "浙江": "ZJ",
    "未知": "NN"
}
import json
import matplotlib.pyplot as plt

data = []
for n in range(1, 161):
    with open(str(n) + '.json', 'r') as file:
        data.append(json.load(file))

ip_follows = {}
for item in data:
    ip = dic[item['IP']]
    follow = item['follow']
    if ip in ip_follows:
        ip_follows[ip] += 1
    else:
        ip_follows[ip] = 1

ip_counts = {ip: count for ip, count in ip_follows.items()}
sorted_counts = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)

ips = [item[0] for item in sorted_counts]
counts = [item[1] for item in sorted_counts]

plt.figure(figsize=(20, 5))
plt.bar(ips, counts)
plt.savefig('chart2.png')
plt.show()








#排除或针对极端值
Fu=5000
Fd=0

dic = {
    "澳门": "AM",
    "安徽": "AH",
    "北京": "BJ",
    "重庆": "CQ",
    "福建": "FJ",
    "甘肃": "GS",
    "广东": "GD",
    "广西": "GX",
    "贵州": "GZ",
    "海南": "HI",
    "河北": "HEB",
    "黑龙江": "HLJ",
    "河南": "HE",
    "湖北": "HB",
    "湖南": "HN",
    "吉林": "JL",
    "江苏": "JS",
    "江西": "JX",
    "辽宁": "LN",
    "内蒙古": "NMG",
    "宁夏": "NX",
    "青海": "QH",
    "山东": "SD",
    "四川": "SC",
    "上海": "SH",
    "陕西": "SN",
    "山西": "SX",
    "天津": "TJ",
    "台湾": "TW",
    "西藏": "XZ",
    "新疆": "XJ",
    "香港": "XG",
    "云南": "YN",
    "浙江": "ZJ",
    "未知": "NN"
}

import json
import matplotlib.pyplot as plt

data = []
for n in range(1, 161):
    with open(str(n) + '.json', 'r') as file:
        data.append(json.load(file))

ip_follows = {}
for item in data:
    ip = dic[item['IP']]
    follow = item['follow']
    if Fd < follow < Fu:
        if ip in ip_follows:
            ip_follows[ip]['total'] += follow
            ip_follows[ip]['count'] += 1
        else:
            ip_follows[ip] = {'total': follow, 'count': 1}

ip_averages = {ip: info['total'] / info['count'] for ip, info in ip_follows.items()}
sorted_averages = sorted(ip_averages.items(), key=lambda item: item[1], reverse=True)

ips = [item[0] for item in sorted_averages]
averages = [item[1] for item in sorted_averages]

plt.figure(figsize=(20, 5))
plt.bar(ips, averages)
plt.tight_layout()
plt.savefig('chart1.png')
plt.show()





dic = {
    "澳门": "AM",
    "安徽": "AH",
    "北京": "BJ",
    "重庆": "CQ",
    "福建": "FJ",
    "甘肃": "GS",
    "广东": "GD",
    "广西": "GX",
    "贵州": "GZ",
    "海南": "HI",
    "河北": "HEB",
    "黑龙江": "HLJ",
    "河南": "HE",
    "湖北": "HB",
    "湖南": "HN",
    "吉林": "JL",
    "江苏": "JS",
    "江西": "JX",
    "辽宁": "LN",
    "内蒙古": "NMG",
    "宁夏": "NX",
    "青海": "QH",
    "山东": "SD",
    "四川": "SC",
    "上海": "SH",
    "陕西": "SN",
    "山西": "SX",
    "天津": "TJ",
    "台湾": "TW",
    "西藏": "XZ",
    "新疆": "XJ",
    "香港": "XG",
    "云南": "YN",
    "浙江": "ZJ",
    "未知": "NN"
}
rn = {
    "澳门": 682100,
    "安徽": 61027171,
    "北京": 21893095,
    "重庆": 32054159,
    "福建": 41540096,
    "甘肃": 25019831,
    "广东": 126012510,
    "广西": 50126804,
    "贵州": 38246226,
    "海南": 10081232,
    "河北": 74610235,
    "黑龙江": 31850050,
    "河南": 99365519,
    "湖北": 57752557,
    "湖南": 66444864,
    "吉林": 24073453,
    "江苏": 84748016,
    "江西": 45188337,
    "辽宁": 42591407,
    "内蒙古": 24049155,
    "宁夏": 7202654,
    "青海": 5897698,
    "山东": 101527453,
    "四川": 83674866,
    "上海": 24870438,
    "陕西": 39528999,
    "山西": 34917666,
    "天津": 13866009,
    "台湾": 23573259,
    "西藏": 3648100,
    "新疆": 25852345,
    "香港": 7500700,
    "云南": 47209277,
    "浙江": 64567588,
    "未知": 1145141919,
}

import json
import matplotlib.pyplot as plt

d = []
for n in range(1, 161):
    with open(f'{n}.json', 'r') as file:d.append(json.load(file))

iw = {}
for item in d:
    province_name = item['IP']
    if province_name in dic:
        province_code = dic[province_name]
        if province_code in iw:
            iw[province_code]['count'] += 1
        else:
            iw[province_code] = {'count': 1, 'province_name': province_name}
    else:
        print(f"Province {province_name} not found in dictionary.")

p = {pc: fo['count'] / rn[fo['province_name']] for pc, fo in iw.items()}

s = sorted(p.items(), key=lambda x: x[1], reverse=True)

plt.figure(figsize=(20, 5))
plt.bar([i[0] for i in s], [i[1] for i in s])
plt.savefig('chart3.png')
plt.show()





