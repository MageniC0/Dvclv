import os,pickle,re
from PIL import Image,ImageDraw
def f0(s,z):
    print('\033[92m'+'|   '*z+'\033[95m'+s)
def f1(s,z):
    return input('\033[92m'+'|   '*z+'\033[95m'+s)
def f2(s):
    while True:
        u = f1(f"\033[92m|\n\033[95m[{s}]选择方块\033[94m_",1)
        try:
            u = int(u)
            if 0 <= u <= 255:
                return u
            else:
                f0(f"[提示]输入数字于0～255",1)
        except ValueError:
            f0(f"[提示]输入数字于0～255",1)
def f3():
    u1 = str(f1("[材质]方块名\033[94m_",2))
    u2 = str(f1("[材质]方块主色\033[94m_",2))
    u3 = str(f1("[材质]方块副色\033[94m_",2))
    c1,c2,c3 = [int(u2[u:u+2],16) for u in (0,2,4)]
    c4,c5,c6 = [int(u3[u:u+2],16) for u in (0,2,4)]
    f0(f"[材质]构造方块\033[94m{f3}",1)
    print("\033[92m|")
    return [c1,c2,c3,c4,c5,c6,int(c1*0.8),int(c2*0.8),int(c3*0.8),int(c4*0.8),int(c5*0.8),int(c6*0.8)],f3
def f4():
    u1 = "r/ch/" + f1("[材质]指定资源包\033[94m_",1) + "/"
    if os.path.exists(u1):
        with open(u1+'a','rb') as f:u2 = pickle.load(f)
        with open(u1+'b','rb') as f:u3 = pickle.load(f)
    else:
        os.makedirs(u1)
        u2 = [[0 for _ in range(12)] for _ in range(256)]
        u3 = ["dust" for _ in range(256)]
        with open(u1+'a','wb') as f:pickle.dump(u2,f)
        with open(u1+'b','wb') as f:pickle.dump(u3,f)
        f0(f"[材质]创建\033[94m{u1}",1)
    while True:
        u4 = f2("材质")
        if u4 == 0:
            return
        else:
            u5,u6 = f2()
            u2[u4] = u5
            u3[u4] = u6
            with open(u1+'a','wb') as f:pickle.dump(u2,f)
            with open(u1+'b','wb') as f:pickle.dump(u3,f)
def f5(s):
    f0(s,2)
    x = int(f1("x\033[94m_",2))
    y = int(f1("y\033[94m_",2))
    z = int(f1("z\033[94m_",2))
    return x,y,z
def f6(a,b,c,d):
    with open(a+'a',"wb") as f:pickle.dump(b,f)
    with open(a+'b',"wb") as f:pickle.dump(c,f)
    f0(d,2)
def f7(u,v):
    if u == 0:
        f0("[地质]正在拆除",1)
        return 0
    else:
        f0(f"[地质]持有方块\033[94m{v}",1)
        return 1
def f8(l):
    c = "r/ch/" + f1("[制图]指定资源包\033[94m_",1) + "/"
    if os.path.exists(c):
        with open(c+'a','rb') as f:a = pickle.load(f)
        with open(c+'b','rb') as f:b = pickle.load(f)
    else:
        f0("[地质]未找到资源包",1)
        return
    t = "r/tr/" + f1("[制图]指定地图册\033[94m_",1) + "/"
    if os.path.exists(t):
        with open(t+'a','rb') as f:ta = pickle.load(f)
        with open(t+'b','rb') as f:tb = pickle.load(f)
    else:
        os.makedirs(t)
        f0(f"[地质]创建\033[94m{t}",1)
        ta = [[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        tb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        with open(t+'a','wb') as f:pickle.dump(ta,f)
        with open(t+'b','wb') as f:pickle.dump(tb,f)
    if len(l) == 1:
        l = "2." + input(f"\033[92m|\n|   \033[95m[地图册]选择支线\n\033[92m|   \033[95m2.1 放置方块\n\033[92m|   \033[95m2.2 放置方块组\n\033[92m|   \033[95m2.3 选择笔刷\n\033[92m|   \033[95m2.\033[94m_")
    if l == "2.0":
        return
    d = 1
    p = a[1]
    q = b[1]
    while True:
        if l == "2.0":
            return
        elif l == "2.1":
            x,y,z = f5("[地质]选择坐标")
            ta[x][y][z] = p
            tb[x][y][z] = d
            f6(t,ta,tb,f"[地质]在\033[94m({x},{y},{z})\033[95m放置方块\033[94m{q}")
        elif l == "2.2":
            x1,y1,z1 = f5("[地质]选择起点")
            x2,y2,z2 = f5("[地质]选择终点")
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    for z in range(z1,z2+1):
                        ta[x][y][z] = p
                        tb[x][y][z] = d
            f6(t,ta,tb,f"[地质]填充\033[94m{q}\033[95m从\033[94m({x1}\033[95m,{y1},{z1})\033[95m到\033[94m({x2},{y2},{z2})")
        elif l == "2.3":
            w = f2()
            p = ca[w]
            q = cb[w]
            d = f7(w,q)
        l = "2." + f1("\033[94m|\n|   \033[95m[地质]选择支线\033[94m_",1)
def f9():
    t = "r/tr/" + f1("[制图]指定地图册\033[94m_",1) + "/"
    u1 = "r/pl/" + f1("[制图]指定文件名\033[94m_",1) + ".png"
    if os.path.exists(t):
        with open(t+'a','rb') as f:u2 = pickle.load(f)
        with open(t+'b','rb') as f:u3 = pickle.load(f)
    else:
        f0(f"[制图]未找到\033[94m{t}",1)
        return
    f0("[制图]传送数据...",1)
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
                    a = [[(0,0,0) for _ in range(13)] for _ in range(13)]
                    b = [[0 for _ in range(13)] for _ in range(13)]
                    u7 = u2[x][y][z]
                    u8 = [
                        u4[x+2][y+1][z+1],
                        u4[ x ][y+1][z+1],
                        u4[x+1][y+2][z+1],
                        u4[x+1][ y ][z+1],
                        u4[x+1][y+1][z+2],
                        u4[x+1][y+1][ z ]]
                    d1 = (u7[0],u7[1],u7[2])
                    d2 = (u7[3],u7[4],u7[5])
                    d3 = (u7[6],u7[7],u7[8])
                    d4 = (u7[9],u7[10],u7[11])
                    if u8[4] == 0:
                        for i in range(2,11):a[i][1] = d1
                        for i in range(2,11):a[i][2] = d1
                        a[5][0] = d1
                        a[6][0] = d1
                        a[7][0] = d1
                        a[5][3] = d1
                        a[6][3] = d1
                        a[7][3] = d1
                        if u8[0] == 0:
                            a[0][2] = d2
                            a[1][2] = d2
                            a[2][3] = d2
                            a[3][3] = d2
                            a[4][3] = d2
                            a[5][4] = d2
                            a[6][4] = d2
                        if u8[1] == 0:
                            b[5][0] = 2
                            b[6][0] = 2
                            b[7][0] = 2
                            b[8][1] = 2
                            b[9][1] = 2
                            b[10][1] = 2
                        if u8[2] == 0:
                            a[6][4] = d2
                            a[7][4] = d2
                            a[8][3] = d2
                            a[9][3] = d2
                            a[10][3] = d2
                            a[11][2] = d2
                            a[12][2] = d2
                        if u8[3] == 0:
                            b[2][1] = 2
                            b[3][1] = 2
                            b[4][1] = 2
                            b[5][0] = 2
                            b[6][0] = 2
                            b[7][0] = 2
                    if u8[5] == 0:
                        if u8[0] == 0:
                            b[0][10] = 1
                            b[1][10] = 1
                            b[2][11] = 1
                            b[3][11] = 1
                            b[4][11] = 1
                            b[5][12] = 1 
                        if u8[2] == 0:
                            b[7][12] = 1
                            b[8][11] = 1
                            b[9][11] = 1
                            b[10][11] = 1
                            b[11][10] = 1
                            b[12][10] = 1
                    if u8[0] == 0:
                        if u8[3] == 0:
                            for j in range(3,11):b[0][j] = 3
                        for j in range(3,11):a[0][j] = d3
                        for j in range(3,11):a[1][j] = d3
                        for j in range(4,12):a[2][j] = d3
                        for j in range(4,12):a[3][j] = d3
                        for j in range(4,12):a[4][j] = d3
                        for j in range(5,13):a[5][j] = d3
                    if u8[2] == 0:
                        if u8[1] == 0:
                            for j in range(3,11):b[12][j] = 3
                        for j in range(5,13):a[7][j] = d3
                        for j in range(4,12):a[8][j] = d3
                        for j in range(4,12):a[9][j] = d3
                        for j in range(4,12):a[10][j] = d3
                        for j in range(3,11):a[11][j] = d3
                        for j in range(3,11):a[12][j] = d3
                    if u8[0] == 0 and u8[2] == 0:
                        for j in range(5,13):a[6][j] = d4
                    m = 6 * (15 - x + y)
                    n = 2 * (60 + x + y - 4 * z)
                    for i in range(13):
                        for j in range(2,11):
                            u6[m+i][n+j] = 0 
                    for i in range(2,11):u6[m+i][n+1] = 0
                    for i in range(2,11):u6[m+i][n+11] = 0
                    u6[m+5][n] = 0
                    u6[m+6][n] = 0
                    u6[m+7][n] = 0
                    u6[m+5][n+12] = 0
                    u6[m+6][n+12] = 0
                    u6[m+7][n+12] = 0
                    for i in range(13):
                        for j in range(13):
                            if a[i][j] != (0,0,0):
                                u5[m+i][n+j] = a[i][j]
                                u6[m+i][n+j] = b[i][j]
    u0 = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
    for i in range(193):
        for j in range(193):
            r,g,b = u5[i][j]
            if u6[i][j] == 1:
                r = int(r*0.9)
                g = int(g*0.9)
                b = int(b*0.9) 
            elif u6[i][j] == 2:
                r = int(r*0.7)+63
                g = int(g*0.7)+63
                b = int(b*0.7)+63
            elif u6[i][j] == 3:
                r = int(r*0.8)
                g = int(g*0.8)
                b = int(b*0.8)
            u0.putpixel((i,j),(r,g,b,255))
    u0.save(u1)
    f0(f"\n[制图]生成图像\033[94m{u1}\n",1)
    u0.show()
def fa():
    l = []
    f0("[检查]传送数据...\n",1)
    u=os.path.abspath('.')
    for v,_,x in os.walk(u):
        y=v.replace(u,'').count(os.sep)
        z='|   '*y
        h=f"{z}[{os.path.basename(v)}]"
        l.append(h+'_'*(34 - len(h))+"\n")
        m='|   '*(y+1)
        l.extend(f'{m}{n}\n' for n in x)
    print(f"\033[90m{''.join(l)}")
def fb():
    h = f1(f"[检查]指定资源包\033[94m_",1)
    try:
        with open(f'r/ch/{h}/b','rb') as f:
            c = pickle.load(f)
    except Exception:
        f0(f"[检查]未找到资源包\033[94m{h}",1)
    p = []
    for i in range(64):
        for j in range(4):
            k=i+j*64
            p.append(f"[{k}]_{c[k]}".ljust(20))
        p.append("\n")
    o = ''.join(p)
    f0(f"[查看资源包\033[94m{h}",1)
    print(f"\033[90m{o}")
def fc():
    t = "r/tr/" + f1("[制图]指定地图册\033[94m_",1) + "/"
    with open(t+'a','rb') as f:ta = pickle.load(f)
    i = Image.open("lab.png")
    l = ImageDraw.Draw(i)
    for z in range(16):
        for y in range(16):
            for x in range(16):
                c = (ta[x][y][z][0],ta[x][y][z][1],ta[x][y][z][2])
                if c != (0,0,0):
                    l.rectangle([16*x+2,16*y+4*z+2,16*x+18,16*y+4*z+18],fill=c)
    f0(f"[查看地图册]\033[94m{t}\n",1)
    i.show()