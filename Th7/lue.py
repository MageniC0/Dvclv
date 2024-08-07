Fu = 5000
Fd = 0
with open("Th7","w") as file: json.dump(qua,file)
dc = {
    "澳门": "AoMen",
    "安徽": "AnHui",
    "北京": "BeiJin",
    "重庆": "ChongQing",
    "福建": "FuJian",
    "甘肃": "GanSu",
    "广东": "GuangDong",
    "广西": "GuangXi",
    "贵州": "GuiZhou",
    "海南": "HaiNan",
    "河北": "HeBei",
    "黑龙江": "HeiLJ",
    "河南": "HeNan",
    "湖北": "HuBei",
    "湖南": "HuNan",
    "吉林": "JiLin",
    "江苏": "JiangSu",
    "江西": "JiangXi",
    "辽宁": "LiaoNing",
    "内蒙古": "NeiMG",
    "宁夏": "NingXia",
    "青海": "QingHai",
    "山东": "ShanDong",
    "四川": "SiChuan",
    "上海": "ShangHai",
    "陕西": "ShanXi",
    "山西": "ShanXi",
    "天津": "TianJing",
    "台湾": "TaiWan",
    "西藏": "XiZang",
    "新疆": "XinJiang",
    "香港": "XiangGang",
    "云南": "YunNan",
    "浙江": "ZheJiang",
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
}
import json
import matplotlib.pyplot as plt
da = []
for n in range(1, 161):
    with open(qua+f'{n}.json', 'r') as f:da.append(json.load(f))

pf = {}
for i in da:
    ip = i['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = i['follow']
        if ip in pf:pf[ip] += 1
        else:pf[ip] = 1
ip_counts = {ip: count for ip, count in pf.items()}
sc = sorted(ip_counts.items(), key=lambda i: i[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in sc],[i[1] for i in sc])
plt.savefig('均值表.png')
plt.show()

pf = {ip: {'total': 0, 'count': 0} for ip in pf}
for i in da:
    ip = i['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = i['follow']
        if Fd <= follow <= Fu:
            pf[ip]['total'] += follow
            pf[ip]['count'] += 1
ia = {ip: info['total'] / info['count'] for ip, info in pf.items() if info['count'] > 0}
s = sorted(ia.items(), key=lambda i: i[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in s],[i[1] for i in s])
plt.savefig('均粉表.png')
plt.show()

iw = {pc: {'count': 0} for pc in dc.values()}
for i in da:
    pn = i['IP']
    pc = dc.get(pn, None)
    if pc:
        iw[pc]['count'] += 1
p = {}
for pc, info in iw.items():
    pn = [k for k, v in dc.items() if v == pc][0]
    if pn in rn:
        p[pc] = info['count'] / rn[pn]
s = sorted(p.items(), key=lambda x: x[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in s], [i[1] for i in s])
plt.savefig('氛围表.png')
plt.show()