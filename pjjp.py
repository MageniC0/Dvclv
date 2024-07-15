import pickle,json,os
def ptj(p, j):
    with open(p,'rb') as f:d = pickle.load(f)
    try:
        d = json.dumps(d, indent=4)
        with open(j,'w') as f:f.write(d)
        print(f"保存为\033[94m{j}")
    except Exception as e:print(e)
def jtp(j,p):
    with open(j,'r') as f:d = json.load(f)
    with open(p,'wb') as f:pickle.dump(d,f)
    print(f"保存为\033[94m{p}")
while True:
    i = input("\n[主页]选择支线\033[94m_")
    if i == "0":
        print("[主页]告辞.")
        break
    elif i == "1":
        p = input("[pickle]\033[94m_")
        j = input("[json]\033[94m_")
        ptj(p,j)
        continue
    elif i == "2":
        j = input("[json]\033[94m_")
        p = input("[pickle]\033[94m_")
        jtp(j,p)
        continue
    elif i == ".":
        o = []
        print("\n[检查]传送数据...\n")
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '| ' * v5
            o.append(f'{v6}[{os.path.basename(v2)}]\n')
            v7 = '| ' * (v5 + 1)
            for v8 in v4:o.append(f'{v7}{v8}\n')
        print(f"\033[90m{''.join(o)}")
    else:print("[提示]\n1.pickle转json\n2.json转pickle")