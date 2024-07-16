import os,pickle,json
from PIL import Image,ImageDraw
#本程序[starlit星光]由Dustormn风尘结社开发，由后勤部负责人MageniC（磁砖）主持开发工作，受到版权法保护。
#禁止私自转载或商业性质使用。
#此版本为没有文本色彩样式的副本
def s1():
    print("_"*68)
def s2(n):
    print("|   "*n)
def s3(s,n):
    print('|   '*n+s)
def s4(s,n):
    a = input('|   '*n+s)
    if len(a) == 0:
        return "0"
    return a
def h0(s):
    while True:
        s2(2)
        u = s4(f"[{s}]选择方块_",2)
        try:
            u = int(u)
            if 0 <= u <= 255:
                return u
            else:
                s3(f"[提示]输入数字于0～255",3)
        except ValueError:
            s3(f"[提示]输入数字于0～255",3)
def g0():
    u,m,n,j = s4("[材质]方块名_",3),s4("[材质]方块主色_",3),s4("[材质]方块副色_",3),0
    c0,c1,c2,c3,c4,c5 = int(m[0:2],16),int(m[2:4],16),int(m[4:6],16),int(n[0:2],16),int(n[2:4],16),int(n[4:6],16)
    c6,c7,c8,c9,c10,c11 = int(c0*0.8),int(c1*0.8),int(c2*0.8),int(c3*0.8),int(c4*0.8),int(c5*0.8)
    s3(f"[材质]构造方块_{u}",3)
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
    return [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11],u
def g1():
    u1 = "r/ch/" + s4("[材质]指定资源包_",2) + "/"
    if os.path.exists(u1):
        with open(u1+'a','rb') as f:u2 = pickle.load(f)
        with open(u1+'b','rb') as f:u3 = pickle.load(f)
    else:
        os.makedirs(u1)
        u2 = [[0 for _ in range(12)] for _ in range(256)]
        u3 = ["dust" for _ in range(256)]
        with open(u1+'a','wb') as f:pickle.dump(u2,f)
        with open(u1+'b','wb') as f:pickle.dump(u3,f)
        s3(f"[材质]创建_{u1}",2)
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
def h1(s):
    s3(s,3)
    x = int(s4("x_",3))
    y = int(s4("y_",3))
    z = int(s4("z_",3))
    return x,y,z
def g2(a,b,c,d):
    with open(a+'a',"wb") as f:pickle.dump(b,f)
    with open(a+'b',"wb") as f:pickle.dump(c,f)
    s3(d,3)
def h2(u,v):
    if u == 0:
        s3("[地质]正在拆除",2)
        return 0
    else:
        s3(f"[地质]持有方块_{v}",2)
        return 1
def g3(l):
    c = "r/ch/" + s4("[制图]指定资源包_",2) + "/"
    if os.path.exists(c):
        with open(c+'a','rb') as f:a = pickle.load(f)
        with open(c+'b','rb') as f:b = pickle.load(f)
    else:
        s3("[雨声]未找到资源包",2)
        return
    t = "r/tr/" + s4("[制图]指定地图册_",2) + "/"
    if os.path.exists(t):
        with open(t+'a','rb') as f:ta = pickle.load(f)
        with open(t+'b','rb') as f:tb = pickle.load(f)
    else:
        os.makedirs(t)
        s3(f"[地质]创建{t}",2)
        ta = [[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        tb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        with open(t+'a','wb') as f:pickle.dump(ta,f)
        with open(t+'b','wb') as f:pickle.dump(tb,f)
    if len(l) == 1:
        s3("",2)
        s3("2.1 放置方块",2)
        s3("2.2 放置方块组",2)
        s3("2.3 选择笔刷",2)
        l = "2." + s4(f"[地质]选择支线 2.",2)
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
            g2(t,ta,tb,f"[地质]在({x},{y},{z})放置方块_{q}")
        elif l == "2.2":
            x1,y1,z1 = h1("[地质]选择起点坐标")
            x2,y2,z2 = h1("[地质]选择终点坐标")
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    for z in range(z1,z2+1):
                        ta[x][y][z] = p
                        tb[x][y][z] = d
            g2(t,ta,tb,f"[地质]从({x1},{y1},{z1})到({x2},{y2},{z2})放置方块_{q}")
        elif l == "2.3":
            w = h0("材质")
            p = a[w]
            q = b[w]
            d = h2(w,q)
            s3("",2)
        s2(2)
        l = "2." + s4("2._",2)
def g4():
    t = "r/tr/" + s4("[制图]指定地图册_",2) + "/"
    if os.path.exists(t):
        with open(t+'a','rb') as f:u2 = pickle.load(f)
        with open(t+'b','rb') as f:u3 = pickle.load(f)
    else:
        s3(f"[雨声]未找到_{t}",2)
        return
    u1 = s4("[制图]指定文件名_",2)+".png"
    s3("[制图]传送数据...",2)
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
    print(f"\n[制图]生成图像[{u1}]")
    u0.show()
def f0():
    l=[]
    s3("[检查]传送数据...",1)
    s1()
    print("[查看文件目录]")
    u=os.path.abspath('.')
    for v,_,x in os.walk(u):
        y=v.replace(u,'').count(os.sep)
        h="|   "*y+f"[{os.path.basename(v)}]"
        l.append(h+'_'*(34 - len(h))+"\n")
        m='|   '*(y+1)
        l.extend(f'{m}{n}\n' for n in x)
    print("".join(l))
    s1()
def f1():
    h = s4(f"[检查]指定资源包_",1)
    try:
        with open(f"r/ch/{h}/b","rb") as f:c=pickle.load(f)
    except Exception:
        s3(f"[雨声]未找到资源包_{h}",1)
    p = []
    for i in range(64):
        for j in range(4):
            k=i+j*64
            p.append(f"[{k}]_{c[k]}".ljust(20))
        p.append("\n")
    s1()
    print(f"[检查]查看资源包_{h}")
    print(''.join(p))
    s1()
def f2():
    t = "r/tr/" + s4("[检查]指定地图册_",1) + "/"
    try:
        with open(t+'a','rb') as f:ta = pickle.load(f)
    except Exception:
        s4("[雨声]未找到地图册",1)
    i = Image.open("lab.png")
    l = ImageDraw.Draw(i)
    for z in range(16):
        for y in range(16):
            for x in range(16):
                c = (ta[x][y][z][0],ta[x][y][z][1],ta[x][y][z][2]) 
                if c!= (0,0,0):
                    l.rectangle([16*x+2,16*y+288*z+2,16*x+17,16*y+288*z+17],fill=c)
    s1()
    print(f"[查看地检查]图册{t}")
    i.show()
    s1()
def f3(l):
    if len(l) == 1:
        s3("4.1 文件目录",2)
        s3("4.2 查看预设",2)
        s3("4.3 查看地图册",2)
        l = "4." + s4("[检查]选择支线 4.",1)
    if l == "4.0":
        return
    elif l == "4.1":f0( )
    elif l == "4.2":f1( )
    elif l == "4.3":f2( )
def p0():
    print("[pickle转json]")
    p = s4("[雨声]指定pickle_",2)
    j = s4("[雨声]指定json_",2)
    with open(p,'rb') as f:
        d = pickle.load(f)
    try:
        d = json.dumps(d,indent=1)
        with open(j,'w') as f:
            f.write(d)
        s3(f"[雨声]保存文件_{j}",2)
    except Exception as e:print(e)
def p1():
    print("[json转pickle]")
    j = s4("[雨声]指定json_",2)
    p = s4("[雨声]指定pickle_",2)
    with open(j,'r') as f:
        d = json.load(f)
    with open(p,'wb') as f:
        pickle.dump(d,f)
    s3(f"[雨声]保存文件_{p}",2)
print("[星光]_1.12.4")
while True:
    s2(1)
    l = s4("[雨声]选择支线_",1)
    if l == "0":
        break
    elif l[0] == "1":g1( )
    elif l[0] == "2":g3(l)
    elif l[0] == "3":g4( )
    elif l[0] == "4":f3(l)
    elif l[0] == "5":p0( )
    elif l[0] == "6":p1( )
    else:
        s1()
        print("""
[提示]
1[编辑资源包]
2[编辑地图册]
|   2.1[放置单个方块]
|   |选择坐标
|   2.2[放置方块组]
｜
|   2.3[设置笔刷]
3[生成例图]
4[检查目录]
|   4.1[检查文件目录]
|   4.2[检查资源包]
|   4.3[检查地图册]
5[导入资源包]
6[导出资源包]""")
        s1()