import os,pickle,json,time
from PIL import Image,ImageDraw
#  © 2024 Dustormn.  All rights reserved.

print('_'*39)
print('[starlit] 1.16.0')

#text indent
ind = 1
ash = '|   '

#value
br = 1

#text color
dawn = '\033[0m'
dawn0 = '\033[90m'
dawn1 = '\033[91m'
dawn2 = '\033[92m'
dawn3 = '\033[93m'
dawn4 = '\033[94m'
dawn5 = '\033[95m'

def urln():print('_' * 39)
def vdln():print(f'{dawn2}{ash*ind}')
def prln(string):print(f'{dawn2}{ash*ind}{dawn}{string}')
def inln(string):return input(f'{dawn2}{ash*ind}{dawn}{string}{dawn4}_')
def clln(string,object):print(f'{dawn2}{ash*ind}{dawn}{string}{dawn4}{object}')

#h for number input
def h0(string):
    mu = int(yu.inln(f"[{string}]select cube"))
    if 0 <= mu <= 255:
        return mu
    else:
        prln(f"[magenic]input number 0-255")
def h1():
    for mu in ['x','y','z']:
        yield int(yu.inputline(mu))
def h2(sh):
    if br == 0:
        prln("[trr]deleteing")
        return 0
    else:
        clln(f"[trr]putting cube",sh)
        return 1

def g0():
    u = s8("[材质]方块名")
    m = s8("[材质]方块主色")
    n = s8("[材质]方块副色")
    j = 0
    c0,c1,c2,c3,c4,c5 = int(m[0:2],16),int(m[2:4],16),int(m[4:6],16),int(n[0:2],16),int(n[2:4],16),int(n[4:6],16)
    c6,c7,c8,c9,c10,c11 = int(c0*0.8),int(c1*0.8),int(c2*0.8),int(c3*0.8),int(c4*0.8),int(c5*0.8)
    s0()
    print()
    time.sleep(0.2)
    i = Image.new('RGB',(208,208), color=(0,0,0))
    l = ImageDraw.Draw(i)
    a = "0000011100000001111111110022111111111223322211122233333332223333333333343333333333334333333333333433333333333343333333333334333333333333433333300333343333300000034300000"
    for x in range(13):
        for y in range(13):
            aj = a[j]
            pos = [16*y,16*x,16*(y+1),16*(x+1)]
            if aj == "1":
                l.rectangle(pos,fill=(c0,c1,c2))
            if aj == "2":
                l.rectangle(pos,fill=(c3,c4,c5))
            if aj == "3":
                l.rectangle(pos,fill=(c6,c7,c8))
            if aj == "4":
                l.rectangle(pos,fill=(c9,c10,c11))
            j+=1
    i.show()
    s0()
    s6(f"[材质]构造方块",u)
    return [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11],u
def g1():
    u1 = s7("[材质]指定资源包")
    u1 = f"r/ch/{u1}/"
    if os.path.exists(u1):
        with open(u1+'a','rb') as f:u2 = pickle.load(f)
        with open(u1+'b','rb') as f:u3 = pickle.load(f)
    else:
        os.makedirs(u1)
        u2 = [[0 for _ in range(12)] for _ in range(256)]
        u3 = ["dvst" for _ in range(256)]
        with open(u1+'a','wb') as f:pickle.dump(u2,f)
        with open(u1+'b','wb') as f:pickle.dump(u3,f)
        s5(f"[材质]创建",u1)
    while True:
        u4 = h0("材质")
        if u4 == 0:
            return
        else:
            u5,u6 = g0()
            u2[u4] = u5
            u3[u4] = u6
            with open(u1+'a','wb') as f:pickle.dump(u2,f)
            with open(u1+'b','wb') as f:pickle.dump(u3,f)
def g2(a,b,c):
    with open(a+'a',"wb") as f:pickle.dump(b,f)
    with open(a+'b',"wb") as f:pickle.dump(c,f)
def g3(l):
    c = s7("[制图]指定资源包")
    c = f"r/ch/{c}/"
    if os.path.exists(c):
        with open(c+'a','rb') as f:a = pickle.load(f)
        with open(c+'b','rb') as f:b = pickle.load(f)
    else:
        s5("[雨声]未找到资源包",c)
        return
    t = s7("[制图]指定地图册")
    t = f"r/tr/{t}/"
    if os.path.exists(t):
        with open(t+'a','rb') as f:ta = pickle.load(f)
        with open(t+'b','rb') as f:tb = pickle.load(f)
    else:
        os.makedirs(t)
        s5("[地质]创建",t)
        ta = [[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        tb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        with open(t+'a','wb') as f:pickle.dump(ta,f)
        with open(t+'b','wb') as f:pickle.dump(tb,f)
    if len(l) == 1:
        s3("2.1 放置方块")
        s3("2.2 放置方块组")
        s3("2.3 选择笔刷")
        s1()
        l = s7(f"[地质]选择支线 2.")
        l = f"2.{l}"
    if l == "2.0":
        return
    d = 1
    p = a[1]
    q = b[1]
    while True:
        if l == "2.0":
            return
        elif l == "2.1":
            x,y,z = h1("[地质]选择坐标")
            ta[x][y][z] = p
            tb[x][y][z] = d
            g2(t,ta,tb)
            s6(f"[地质]在({x},{y},{z})放置方块",q)
        elif l == "2.2":
            x1,y1,z1 = h1("[地质]选择起点坐标")
            x2,y2,z2 = h1("[地质]选择终点坐标")
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    for z in range(z1,z2+1):
                        ta[x][y][z] = p
                        tb[x][y][z] = d
            g2(t,ta,tb)
            s6(f"[地质]从({x1},{y1},{z1})到({x2},{y2},{z2})放置方块",q)
        elif l == "2.3":
            w = h0("材质")
            p = a[w]
            q = b[w]
            d = h2(w,q)
        s1()
        l = s7("2.")
        l = f"2.{l}"
def g4():
    t = s7("[制图]指定地图册")
    t = f"r/tr/{t}/"
    if os.path.exists(t):
        with open(t+'a','rb') as f:u2 = pickle.load(f)
        with open(t+'b','rb') as f:u3 = pickle.load(f)
    else:
        s5(f"[雨声]未找到",t)
        return
    u1 = s7("[制图]指定文件名")
    u1 = f"{u1}.png"
    s3("[制图]传送数据...")
    u4 = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if u3[x][y][z] != 0:
                    u4[x+1][y+1][z+1] = 1
    u5 = [[(0,0,0) for _ in range(193)] for _ in range(193)]
    u6 = [[0 for _ in range(193)] for _ in range(193)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if u3[x][y][z] == 1:
                    u = [u4[x+2][y+1][z+1],u4[x][y+1][z+1],u4[x+1][y+2][z+1],u4[x+1][y][z+1],u4[x+1][y+1][z+2],u4[x+1][y+1][z]]
                    v = u2[x][y][z]
                    a = [[(0,0,0) for _ in range(13)] for _ in range(13)]
                    b = [[0 for _ in range(13)] for _ in range(13)]
                    d0,d1,d2,d3 = (v[i:i+3] for i in range(0,12,3))  
                    if u[4] == 0:
                        a[5][0]=a[6][0]=a[7][0]=a[5][3]=a[6][3]=a[7][3]=d0
                        for i in range(2,11):a[i][1]=d0
                        for i in range(2,11):a[i][2]=d0
                        if u[0] == 0:a[0][2]=a[1][2]=a[2][3]=a[3][3]=a[4][3]=a[5][4]=a[6][4]=d1
                        if u[1] == 0:b[5][0]=b[6][0]=b[7][0]=b[8][1]=b[9][1]=b[10][1]=2
                        if u[2] == 0:a[6][4]=a[7][4]=a[8][3]=a[9][3]=a[10][3]=a[11][2]=a[12][2]=d1
                        if u[3] == 0:b[2][1]=b[3][1]=b[4][1]=b[5][0]=b[6][0]=b[7][0]=2
                    if u[5] == 0:
                        if u[0] == 0:b[0][10]=b[1][10]=b[2][11]=b[3][11]=b[4][11]=b[5][12]=1 
                        if u[2] == 0:b[7][12]=b[8][11]=b[9][11]=b[10][11]=b[11][10]=b[12][10]=1
                    if u[0] == 0:
                        if u[3] == 0:
                            for j in range(3,11):b[0][j] = 3
                        for j in range(3,11):a[0][j] = d2
                        for j in range(3,11):a[1][j] = d2
                        for j in range(4,12):a[2][j] = d2
                        for j in range(4,12):a[3][j] = d2
                        for j in range(4,12):a[4][j] = d2
                        for j in range(5,13):a[5][j] = d2
                    if u[2] == 0:
                        if u[1] == 0:
                            for j in range(3,11):b[12][j] = 3
                        for j in range(5,13):a[7][j] = d2
                        for j in range(4,12):a[8][j] = d2
                        for j in range(4,12):a[9][j] = d2
                        for j in range(4,12):a[10][j] = d2
                        for j in range(3,11):a[11][j] = d2
                        for j in range(3,11):a[12][j] = d2
                    if u[0] == 0 and u[2] == 0:
                        for j in range(5,13):a[6][j] = d3
                    m,n=6*(15-x+y),2*(60+x+y-4*z)
                    for i in range(13):
                        for j in range(2,11):u6[m+i][n+j] = 0 
                    for i in range(2,11):u6[m+i][n+1] = 0
                    for i in range(2,11):u6[m+i][n+11] = 0
                    u6[m+5][n]=u6[m+6][n]=u6[m+7][n]=u6[m+5][n+12]=u6[m+6][n+12]=u6[m+7][n+12]=0
                    for i in range(13):
                        for j in range(13):
                            if a[i][j] != (0,0,0):
                                u5[m+i][n+j] = a[i][j]
                                u6[m+i][n+j] = b[i][j]
    p = []    
    for j in range(193):  
        w = []  
        for i in range(193):
            r,g,b = u5[i][j]  
            if u6[i][j] == 1:
                r,g,b=int(r*0.9),int(g*0.9),int(b*0.9)  
            elif u6[i][j]==2:
                r,g,b=int(r*0.7)+63,int(g*0.7)+63,int(b*0.7)+63  
            elif u6[i][j]==3:
                r,g,b=int(r*0.8),int(g*0.8),int(b*0.8)  
            w.append((r,g,b))
        p.append(w)
    u0=Image.new('RGB',(193,193), color=(255, 255, 255))   
    u0.putdata([l for w in p for l in w])
    u0.save(u1)
    s0()
    s3(f"\n[制图]生成图像\033[94m{u1}")
    print("\n")
    time.sleep(0.2)
    u0.show()
    s0()
def f0():
    l=[]
    s3("[检查]传送数据...")
    s0()
    print("[查看文件目录]")
    u=os.path.abspath('.')
    for v,_,x in os.walk(u):
        y=v.replace(u,'').count(os.sep)
        h="|   "*y+f"[{os.path.basename(v)}]"
        l.append(h+'_'*(34 - len(h))+"\n")
        m='|   '*(y+1)
        l.extend(f'{m}{n}\n' for n in x)
    print("\033[90m"+"".join(l))
    s0()
def f1():
    h = s7(f"[检查]指定资源包")
    try:
        with open(f"r/ch/{h}/b","rb") as f:c=pickle.load(f)
    except Exception:
        s5(f"[雨声]未找到资源包",h)
        return
    p = []
    for i in range(64):
        for j in range(4):
            k=i+j*64
            p.append(f"[{k}]_{c[k]}".ljust(20))
        p.append("\n")
    s0()
    print(f"[检查]查看资源包",h)
    print("\033[90m"+"".join(p))
    s0()
def f2():
    t = s7("[检查]指定地图册")
    t = f"r/tr/{t}/"
    try:
        with open(t+'a','rb') as f:ta = pickle.load(f)
    except Exception:
        s3("[雨声]未找到地图册")
        return
    i = Image.open("lab.png")
    l = ImageDraw.Draw(i)
    for z in range(16):
        for y in range(16):
            for x in range(16):
                c = (ta[x][y][z][0],ta[x][y][z][1],ta[x][y][z][2]) 
                if c!= (0,0,0):
                    l.rectangle([16*x+2,16*y+288*z+2,16*x+17,16*y+288*z+17],fill=c)
    s0()
    print(f"[检查]查看地图册\033[94m{t}")
    i.show()
    s0()
def f3(l):
    if len(l) == 1:
        s3("4.1 文件目录")
        s3("4.2 查看预设")
        s3("4.3 查看地图册")
        l = "4." + s7("[检查]选择支线 4.")
    if l == "4.0":
        return
    elif l == "4.1":f0( )
    elif l == "4.2":f1( )
    elif l == "4.3":f2( )
def p0():
    print("[pickle转json]")
    p = s7("[雨声]指定pickle")
    j = s7("[雨声]指定json")
    with open(p,'rb') as f:
        d = pickle.load(f)
    try:
        d = json.dumps(d,indent=1)
        with open(j,'w') as f:
            f.write(d)
        s5(f"[雨声]保存文件",j)
    except Exception as e:print(e)
def p1():
    print("[json转pickle]")
    j = s7("[雨声]指定json")
    p = s7("[雨声]指定pickle")
    with open(j,'r') as f:
        d = json.load(f)
    with open(p,'wb') as f:
        pickle.dump(d,f)
    s5(f"[雨声]保存文件",p)
def laer():
    while True:
        s1()
        l = s7("[雨声]选择支线")
        if l == "0":
            break
        elif l[0] == "1":g1( )
        elif l[0] == "2":g3(l)
        elif l[0] == "3":g4( )
        elif l[0] == "4":f3(l)
        elif l[0] == "5":p0( )
        elif l[0] == "6":p1( )
        else:
            s0()
            print("""\033[90m[提示]
|
1[编辑预设]
|_输入预设名
|   |_选择索引[0~255]
|   |_输入名称
|   |_输入主色
|   |_输入副色
|
2[编辑地图册]
|_输入预设名
|_输入地图册名
|   2.1[放置单个方块]
|   |_坐标x
|   |_坐标y
|   |_坐标z
|   2.2[放置方块组]
||_起点坐标x
|   |_起点坐标y
|   |_起点坐标z
|   |_终点坐标x
|   |_终点坐标y
|   |_终点坐标z
|   2.3[设置笔刷]
|   |_选择索引[0~255]
|
3[生成例图]
|_输入地图册名
|_输入文件名
|
4[检查目录]
|   4.1[检查文件]
|   4.2[检查预设]
|   |_输入预设名
|   4.3[检查地图册]
|   |_输入地图册名
|
5[导入文件]
|_输入数据路径
|_输入文本路径
|
6[导出文件]
|_输入文本路径
|_输入数据路径""")
            s0()
laer()
