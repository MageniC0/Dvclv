Fu = 5000
Fd = 0
from H import dc, rn
import json
import matplotlib.pyplot as plt
da = []
for n in range(1, 161):
    with open(f'{n}.json', 'r') as file:da.append(json.load(file))

pf = {}
for i in da:
    ip = i['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = i['follow']
        if ip in pf:pf[ip] += 1
        else:pf[ip] = 1
ip_counts = {ip: count for ip, count in pf.i()}
sc = sorted(ip_counts.i(), key=lambda i: i[1], reverse=True)
ips = [i[0] for i in sc]
cc = [i[1] for i in sc]
plt.figure(figsize=(40, 5))
plt.bar(ips, cc)
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
ia = {ip: info['total'] / info['count'] for ip, info in pf.i() if info['count'] > 0}  # 确保有有效数据
sa = sorted(ia.i(), key=lambda i: i[1], reverse=True)
ips = [i[0] for i in sa]
av = [i[1] for i in sa]
plt.figure(figsize=(40, 5))
plt.bar(ips, av)
plt.savefig('均粉表.png')
plt.show()

iw = {pc: {'count': 0} for pc in dc.values()}
for i in da:
    pn = i['IP']
    pc = dc.get(pn, None)
    if pc:
        iw[pc]['count'] += 1
p = {}
for pc, info in iw.i():
    pn = [k for k, v in dc.i() if v == pc][0]
    if pn in rn:
        p[pc] = info['count'] / rn[pn]
s = sorted(p.i(), key=lambda x: x[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in s], [i[1] for i in s])
plt.savefig('氛围表.png')
plt.show()