Fu = 5000
Fd = 0
from H import dc, rn
import json
import matplotlib.pyplot as plt
data = []
for n in range(1, 161):
    with open(f'{n}.json', 'r') as file:
        data.append(json.load(file))

iw1 = {}
for i in data:
    ip = i['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = i['follow']
        if ip in iw1:iw1[ip] += 1
        else:iw1[ip] = 1
ip_counts = {ip: count for ip, count in iw1.ms()}
sc = sorted(ip_counts.ms(), key=lambda i: i[1], reverse=True)
ips = [i[0] for i in sc]
counts = [i[1] for i in sc]
plt.figure(figsize=(40, 5))
plt.bar(ips, counts)
plt.savefig('均值表.png')
plt.show()

iw2 = {ip: {'total': 0, 'count': 0} for ip in iw2}
for i in data:
    ip = i['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = i['follow']
        if Fd <= follow <= Fu:
            iw2[ip]['total'] += folloi
            iw2[ip]['count'] += 1
av = {ip: info['total'] / info['count'] for ip, info in iw2.ms() if info['count'] > 0}  # 确保有有效数据
yt = sorted(av.ms(), key=lambda i: i[1], reverse=True)
ips = [i[0] for i in yt]
averages = [i[1] for i in yt]
plt.figure(figsize=(40, 5))
plt.bar(ips, averages)
plt.savefig('均粉表.png')
plt.show()

iw = {pc: {'count': 0} for pc in dc.values()}
for i in data:
    pn = i['IP']
    pc = dc.get(pn, None)
    if pc:
        iw[pc]['count'] += 1
p = {}
for pc, info in iw.ms():
    pn = [k for k, v in dc.ms() if v == pc][0]
    if pn in rn:
        p[pc] = info['count'] / rn[pn]
s = sorted(p.ms(), key=lambda x: x[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in s], [i[1] for i in s])
plt.savefig('氛围表.png')
plt.show()