import os,pickle,re
from PIL import Image,ImageDraw
def f0(s,z):
    print('\033[92m'+'|   '*z+'\033[95m'+s)
def ip(s,z):
    return input('\033[92m'+'|   '*z+'\033[95m'+s)
def f1(s):
    while True:
        w = ip(f"\033[92m|\n\033[95m[{s}]选择方块\033[94m_",1)
        try:
            w = int(w)
            if 0 <= w <= 255:
                return w
            else:
                f0(f"[提示]输入数字于0～255",1)
        except ValueError:
            f0(f"[提示]输入数字于0～255",1)
def f2():
    c = str(ip("[材质]方块名\033[94m_",2))
    a = str(ip("[材质]方块主色\033[94m_",2))
    b = str(ip("[材质]方块副色\033[94m_",2))
    c1,c2,c3 = [int(a[h:h+2],16) for h in (0,2,4)]
    c4,c5,c6 = [int(b[h:h+2],16) for h in (0,2,4)]
    f0(f"[材质]构造方块\033[94m{c}",1)
    print("\033[92m|")
    return [c1,c2,c3,c4,c5,c6,int(c1*0.8),int(c2*0.8),int(c3*0.8),int(c4*0.8),int(c5*0.8),int(c6*0.8)],c
def f3():
    c = "r/ch/" + ip("[材质]指定资源包\033[94m_",1) + "/"
    if os.path.exists(c):
        with open(c+'a','rb') as f:a = pickle.load(f)
        with open(c+'b','rb') as f:b = pickle.load(f)
    else:
        os.makedirs(c)
        a = [[0 for _ in range(12)] for _ in range(256)]
        b = ["dust" for _ in range(256)]
        with open(c+'a','wb') as f:pickle.dump(a,f)
        with open(c+'b','wb') as f:pickle.dump(b,f)
        f0(f"[材质]创建\033[94m{c}",1)
    while True:
        w = f1("材质")
        if w == 0:
            return
        else:
            r,s = f2()
            a[w] = r
            b[w] = s
            with open(c+'a','wb') as f:pickle.dump(a,f)
            with open(c+'b','wb') as f:pickle.dump(b,f)
def f4(s):
    f0(s,2)
    x = int(ip("x\033[94m_",2))
    y = int(ip("y\033[94m_",2))
    z = int(ip("z\033[94m_",2))
    return x,y,z
def f5(tr,ta,tb,s):
    with open(tr+'a',"wb") as f:pickle.dump(ta,f)
    with open(tr+'b',"wb") as f:pickle.dump(tb,f)
    f0(s,2)
def f6(w):
    if w == 0:
        f0("[地质]正在拆除",1)
        return 0
    else:
        f0(f"[地质]持有方块\033[94m{hb}",1)
        return 1
def f7(l):
    c = "r/ch/" + ip("[制图]指定资源包\033[94m_",1) + "/"
    if os.path.exists(c):
        with open(c+'a','rb') as f:a = pickle.load(f)
        with open(c+'b','rb') as f:b = pickle.load(f)
    else:
        f0("[地质]未找到资源包",1)
        return
    tr = "r/tr/" + ip("[制图]指定地图册\033[94m_",1) + "/"
    if os.path.exists(tr):
        with open(tr+'a','rb') as f:ta = pickle.load(f)
        with open(tr+'b','rb') as f:tb = pickle.load(f)
    else:
        os.makedirs(tr)
        f0(f"[地质]创建\033[94m{tr}",1)
        ta = [[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        tb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        with open(tr+'a','wb') as f:pickle.dump(ta,f)
        with open(tr+'b','wb') as f:pickle.dump(tb,f)
    if len(l) == 1:
        l = "2." + input(f"\033[92m|\n|   \033[95m[地图册]选择支线\n\033[92m|   \033[95m2.1 放置方块\n\033[92m|   \033[95m2.2 放置方块组\n\033[92m|   \033[95m2.3 选择笔刷\n\033[92m|   \033[95m2.\033[94m_")
    if l == "2.0":
        return
    bu = 1
    ha = a[1]
    hb = b[1]
    while True:
        if l == "2.0":
            return
        elif l == "2.1":
            x,y,z = f4("[地质]选择坐标")
            ta[x][y][z] = ha
            tb[x][y][z] = bu
            f5(tr,ta,tb,f"[地质]在\033[94m({x},{y},{z})\033[95m放置方块\033[94m{hb}")
        elif l == "2.2":
            x1,y1,z1 = f4("[地质]选择起点")
            x2,y2,z2 = f4("[地质]选择终点")
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    for z in range(z1,z2+1):
                        ta[x][y][z] = ha
                        tb[x][y][z] = bu
            f5(tr,ta,tb,f"[地质]填充\033[94m{hb}\033[95m从\033[94m({x1}\033[95m,{y1},{z1})\033[95m到\033[94m({x2},{y2},{z2})")
        elif l == "2.3":
            w = f1()
            bu = vc(w)
            ha = ca[w]
            hb = cb[w]
        l = "2." + ip("\033[94m|\n|   \033[95m[地质]选择支线\033[94m_",1)
def f8():
    tr = "r/tr/" + ip("[制图]指定地图册\033[94m_",1) + "/"
    nm = "r/pl/" + ip("[制图]指定文件名\033[94m_",1) + ".png"
    if os.path.exists(tr):
        with open(tr+'a','rb') as f:ta = pickle.load(f)
        with open(tr+'b','rb') as f:tb = pickle.load(f)
    else:
        f0(f"[制图]未找到\033[94m{tr}",1)
        return
    f0("[制图]传送数据...",1)
    tn = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if tb[x][y][z] != 0:
                    tn[x+1][y+1][z+1] = 1
    px = [[(0,0,0) for _ in range(193)] for _ in range(193)]
    dw = [[0 for _ in range(193)] for _ in range(193)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if tb[x][y][z] == 1:
                    a = [[(0,0,0) for _ in range(13)] for _ in range(13)]
                    b = [[0 for _ in range(13)] for _ in range(13)]
                    t = ta[x][y][z]
                    rn = [
                        tn[x+2][y+1][z+1],
                        tn[ x ][y+1][z+1],
                        tn[x+1][y+2][z+1],
                        tn[x+1][ y ][z+1],
                        tn[x+1][y+1][z+2],
                        tn[x+1][y+1][ z ]]
                    ad = (t[0],t[1],t[2])
                    bd = (t[3],t[4],t[5])
                    az = (t[6],t[7],t[8])
                    bz = (t[9],t[10],t[11])
                    if rn[4] == 0:
                        for i in range(2,11):a[i][1] = ad
                        for i in range(2,11):a[i][2] = ad
                        a[5][0] = ad
                        a[6][0] = ad
                        a[7][0] = ad
                        a[5][3] = ad
                        a[6][3] = ad
                        a[7][3] = ad
                        if rn[0] == 0:
                            a[0][2] = bd
                            a[1][2] = bd
                            a[2][3] = bd
                            a[3][3] = bd
                            a[4][3] = bd
                            a[5][4] = bd
                            a[6][4] = bd
                        if rn[1] == 0:
                            b[5][0] = 2
                            b[6][0] = 2
                            b[7][0] = 2
                            b[8][1] = 2
                            b[9][1] = 2
                            b[10][1] = 2
                        if rn[2] == 0:
                            a[6][4] = bd
                            a[7][4] = bd
                            a[8][3] = bd
                            a[9][3] = bd
                            a[10][3] = bd
                            a[11][2] = bd
                            a[12][2] = bd
                        if rn[3] == 0:
                            b[2][1] = 2
                            b[3][1] = 2
                            b[4][1] = 2
                            b[5][0] = 2
                            b[6][0] = 2
                            b[7][0] = 2
                    if rn[5] == 0:
                        if rn[0] == 0:
                            b[0][10] = 1
                            b[1][10] = 1
                            b[2][11] = 1
                            b[3][11] = 1
                            b[4][11] = 1
                            b[5][12] = 1 
                        if rn[2] == 0:
                            b[7][12] = 1
                            b[8][11] = 1
                            b[9][11] = 1
                            b[10][11] = 1
                            b[11][10] = 1
                            b[12][10] = 1
                    if rn[0] == 0:
                        if rn[3] == 0:
                            for j in range(3,11):b[0][j] = 3
                        for j in range(3,11):a[0][j] = az
                        for j in range(3,11):a[1][j] = az
                        for j in range(4,12):a[2][j] = az
                        for j in range(4,12):a[3][j] = az
                        for j in range(4,12):a[4][j] = az
                        for j in range(5,13):a[5][j] = az
                    if rn[2] == 0:
                        if rn[1] == 0:
                            for j in range(3,11):b[12][j] = 3
                        for j in range(5,13):a[7][j] = az
                        for j in range(4,12):a[8][j] = az
                        for j in range(4,12):a[9][j] = az
                        for j in range(4,12):a[10][j] = az
                        for j in range(3,11):a[11][j] = az
                        for j in range(3,11):a[12][j] = az
                    if rn[0] == 0 and rn[2] == 0:
                        for j in range(5,13):a[6][j] = bz
                    m = 6 * (15 - x + y)
                    n = 2 * (60 + x + y - 4 * z)
                    for i in range(13):
                        for j in range(2,11):
                            dw[m+i][n+j] = 0 
                    for i in range(2,11):dw[m+i][n+1] = 0
                    for i in range(2,11):dw[m+i][n+11] = 0
                    dw[m+5][n] = 0
                    dw[m+6][n] = 0
                    dw[m+7][n] = 0
                    dw[m+5][n+12] = 0
                    dw[m+6][n+12] = 0
                    dw[m+7][n+12] = 0
                    for i in range(13):
                        for j in range(13):
                            if a[i][j] != (0,0,0):
                                px[m+i][n+j] = a[i][j]
                                dw[m+i][n+j] = b[i][j]
    mg = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
    for i in range(193):
        for j in range(193):
            r,g,b = px[i][j]
            if dw[i][j] == 1:
                r = int(r*0.9)
                g = int(g*0.9)
                b = int(b*0.9) 
            elif dw[i][j] == 2:
                r = int(r*0.7)+63
                g = int(g*0.7)+63
                b = int(b*0.7)+63
            elif dw[i][j] == 3:
                r = int(r*0.8)
                g = int(g*0.8)
                b = int(b*0.8)
            mg.putpixel((i,j),(r,g,b,255))
    mg.save(nm)
    f0(f"\n[制图]生成图像\033[94m{nm}\n",1)
    mg.show()
def f9():
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
def fa():
    h = ip(f"[检查]指定资源包\033[94m_",1)
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
def fb():
    tr = "r/tr/" + ip("[制图]指定地图册\033[94m_",1) + "/"
    with open(tr+'a','rb') as f:ta = pickle.load(f)
    i = Image.open("lab.png")
    l = ImageDraw.Draw(i)
    for z in range(16):
        for y in range(16):
            for x in range(16):
                c = (ta[x][y][z][0],ta[x][y][z][1],ta[x][y][z][2])
                if c != (0,0,0):
                    l.rectangle([16*x+2,16*y+4*z+2,16*x+18,16*y+4*z+18],fill=c)
    f0(f"[查看地图册]\033[94m{tr}\n",1)
    i.show()