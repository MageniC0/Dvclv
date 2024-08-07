Fu = 5000
Fd = 0
from H import dc, rn
import json
import matplotlib.pyplot as plt
data = []
for n in range(1, 161):
    with open(f'{n}.json', 'r') as file:
        data.append(json.load(file))

ip_follows = {}
for item in data:
    ip = item['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = item['follow']
        if ip in ip_follows:ip_follows[ip] += 1
        else:ip_follows[ip] = 1
ip_counts = {ip: count for ip, count in ip_follows.items()}
sorted_counts = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)
ips = [item[0] for item in sorted_counts]
counts = [item[1] for item in sorted_counts]
plt.figure(figsize=(40, 5))
plt.bar(ips, counts)
plt.savefig('均值表.png')
plt.show()

ip_follows = {ip: {'total': 0, 'count': 0} for ip in ip_follows}
for item in data:
    ip = item['IP']
    if ip != '未知':
        ip = dc[ip]
        follow = item['follow']
        if Fd <= follow <= Fu:
            ip_follows[ip]['total'] += follow
            ip_follows[ip]['count'] += 1
ip_averages = {ip: info['total'] / info['count'] for ip, info in ip_follows.items() if info['count'] > 0}  # 确保有有效数据
sorted_averages = sorted(ip_averages.items(), key=lambda item: item[1], reverse=True)
ips = [item[0] for item in sorted_averages]
averages = [item[1] for item in sorted_averages]
plt.figure(figsize=(40, 5))
plt.bar(ips, averages)
plt.savefig('均粉表.png')
plt.show()

iw = {pc: {'count': 0} for pc in dc.values()}
for item in data:
    province_name = item['IP']
    province_code = dc.get(province_name, None)
    if province_code:
        iw[province_code]['count'] += 1
p = {}
for pc, info in iw.items():
    province_name = [k for k, v in dc.items() if v == pc][0]
    if province_name in rn:
        p[pc] = info['count'] / rn[province_name]
s = sorted(p.items(), key=lambda x: x[1], reverse=True)
plt.figure(figsize=(40, 5))
plt.bar([i[0] for i in s], [i[1] for i in s])
plt.savefig('氛围表.png')
plt.show()