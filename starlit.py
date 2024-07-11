print("\033[92m[starlit]1.6.0")
import os
import json
import pickle
import time
from PIL import Image,ImageDraw
op = ""
with open("path",'r') as file: path = json.load(file)
chc_ = path["chc_"]
chc_c = chc_ + "/chc"
chc_j = chc_+ "/chj"
trr_ = path["trr_"]
trr_a = trr_ + "/a"
trr_b = trr_+ "/b"
flu_ = path["flu_"]
if not os.path.exists(chc_):os.makedirs(chc_)
if not os.path.exists(trr_):os.makedirs(trr_)
if not os.path.exists(flu_):os.makedirs(flu_)
while True:
    line = input("\n\033[92m[core]")
    if line == "0":
        print("\n\033[92m[core]done.")
        break
    elif line == "1":
        try:
            with open(chc_c, 'rb') as file:chc = pickle.load(file)
            with open(chc_j,'rb') as file:chj = pickle.load(file)
        except FileNotFoundError:
            chc = [[0]*12]*256
            with open(chc_c,'wb') as file:pickle.dump(chc,file)
            chj = ["dust"]*256
            with open(chc_j,'wb') as file:pickle.dump(chj,file)
            print(f"[chc]create[{chc_}]")
        while True:
            index = input("\n[chc]index_")
            if index == "0":
                print(f"\n[chc]save[{chc_}]")
                break
            else:
                index = int(index)
                name,ac,bc = map(str,[input("[chc]name_"),input("[chc]A_"),input("[chc]B_")])
                c1, c2, c3 = [int(ac[h:h+2], 16) for h in (0, 2, 4)]
                c4, c5, c6 = [int(bc[h:h+2], 16) for h in (0, 2, 4)]
                chc[index] = [c1,c2,c3,c4,c5,c6,int(c1*0.75),int(c2*0.75),int(c3*0.75),int(c4*0.75),int(c5*0.75),int(c6*0.75)]
                chj[index] = name
                with open(chc_c,'wb') as file:pickle.dump(chc,file)
                with open(chc_j,'wb') as file:pickle.dump(chj,file)
                print(f"[chc]define {index}")
    elif line == "2":
        try:
            with open(chc_c,'rb') as file:chc = pickle.load(file)
            with open(chc_j,'rb') as file:chj = pickle.load(file)
        except FileNotFoundError:
            print("[trr]chc first")
        try:
            with open(trr_a,'rb') as file:tra = pickle.load(file)
            with open(trr_b,'rb') as file:trb = pickle.load(file)
        except FileNotFoundError:
            tra = [[[[0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
            with open(trr_a,'wb') as file:pickle.dump(tra,file)
            trb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
            with open(trr_b,'wb') as file:pickle.dump(trb,file)
            print(f"[trr]creat[{trr_}]")
        walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        index = 1
        bu = 1
        hb = chc[1]
        hc = chj[1]
        while True:
            mode = input("\n[trr]2.")
            if mode == "0":
                print(f"[trr]save[{trr_}]")
                break
            elif mode == "1":
                print("[pos]")
                x, y, z = map(int,[input("x_"),input("y_"),input("z_")])
                tra[x][y][z] = hb[:]
                trb[x][y][z] = bu
                with open(trr_a,"wb") as file:pickle.dump(tra,file)
                with open(trr_b,"wb") as file:pickle.dump(trb,file)
                print(f"set[{hc}]at({x},{y},{z})")
            elif mode == "2":
                print("[from]")
                x1,y1,z1 = map(int,[input("x_"),input("y_"),input("z_")])
                print("[to]")
                x2,y2,z2 = map(int,[input("x_"),input("y_"),input("z_")])
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            walk[x][y][z] = bu
                print(f"[trr]walk from({x1},{y1},{z1})to({x2},{y2},{z2})")
            elif mode == "3":
                for x in range(16):
                    for y in range(16):
                        for z in range(16):
                            if walk[x][y][z] != 0:
                                tra[x][y][z] = hb[:]
                                trb[x][y][z] = bu
                with open(trr_a,"wb") as file:pickle.dump(tra,file)
                with open(trr_b,"wb") as file:pickle.dump(trb,file)
                walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("[trr]rewalk")
            elif mode == "4":
                for x in range(16):
                    for y in range(16):
                        for z in range(16):
                            if walk[x][y][s] != 0 and trb[x][y][z] == 0:
                                tra[x][y][z] = hb[:]
                                trb[x][y][z] = bu
                with open(trr_a,"wb") as file:pickle.dump(tra,file)
                with open(trr_b,"wb") as file:pickle.dump(trb,file)
                walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("[trr]fill")
            elif mode == "5":
                walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("[trr]reselect")
            elif mode == "6":
                lue = input("[trr]set cube_")
                try:
                    lue = int(lue)
                    hb = chc[lue]
                    hc = chj[lue]
                    if lue == "0":
                        print("[trr]delet")
                        bu = 0
                    else:
                        print(f"[trr]cube[{hc}]")
                        bu = 1
                except ValueError:
                    print("\033[92m[core]input 1~255 for cube or 0 for deleting")
    elif line == "3":
        print("\n\033[94m[dvclv]")
        nm = flu_ + input("flu_") + ".png"
        try:
            with open(trr_a,'rb') as file:tra = pickle.load(file)
            with open(trr_b,'rb') as file:trb = pickle.load(file)
        except FileNotFoundError:
            print(f"\033[92m[demo]nowhere{trr_}")
            continue
        print("\033[92m[demo]loading...")
        trn = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for x in range(16):
            for y in range(16):
                for z in range(16):
                    if trb[x][y][z] != 0:
                        trn[x+1][y+1][z+1] = 1
        pix = [[(0,0,0) for _ in range(193)] for _ in range(193)]
        daw = [[0 for _ in range(193)] for _ in range(193)]
        for x in range(16):
            for y in range(16):
                for z in range(16):
                    if trb[x][y][z] == 1:
                        pi = [[(0,0,0) for _ in range(13)] for _ in range(13)]
                        da = [[0 for _ in range(13)] for _ in range(13)]
                        t = tra[x][y][z]
                        rn = [trn[x+2][y+1][z+1],
                              trn[ x ][y+1][z+1],
                              trn[x+1][y+2][z+1],
                              trn[x+1][ y ][z+1],
                              trn[x+1][y+1][z+2],
                              trn[x+1][y+1][ z ]]
                        a,b,az,bz = ((t[0],t[1],t[2]),
                                     (t[3],t[4],t[5]),
                                     (t[6],t[7],t[8]),
                                     (t[9],t[10],t[11]))
                        if rn[4] == 0:
                            for i in range(2,11):pi[i][1] = a
                            for i in range(2,11):pi[i][2] = a
                            pi[5][0] = a
                            pi[6][0] = a
                            pi[7][0] = a
                            pi[5][3] = a
                            pi[6][3] = a
                            pi[7][3] = a
                            if rn[0] == 0:
                                pi[0][2] = b
                                pi[1][2] = b
                                pi[2][3] = b
                                pi[3][3] = b
                                pi[4][3] = b
                                pi[5][4] = b
                                pi[6][4] = b
                            if rn[1] == 0:
                                da[5][0] = 2
                                da[6][0] = 2
                                da[7][0] = 2
                                da[8][1] = 2
                                da[9][1] = 2
                                da[10][1] = 2
                            if rn[2] == 0:
                                pi[6][4] = b
                                pi[7][4] = b
                                pi[8][3] = b
                                pi[9][3] = b
                                pi[10][3] = b
                                pi[11][2] = b
                                pi[12][2] = b
                            if rn[3] == 0:
                                da[2][1] = 2
                                da[3][1] = 2
                                da[4][1] = 2
                                da[5][0] = 2
                                da[6][0] = 2
                                da[7][0] = 2
                        if rn[5] == 0:
                            if rn[0] == 0:
                                da[0][10] = 1
                                da[1][10] = 1
                                da[2][11] = 1
                                da[3][11] = 1
                                da[4][11] = 1
                                da[5][12] = 1 
                            if rn[2] == 0:
                                da[7][12] = 1
                                da[8][11] = 1
                                da[9][11] = 1
                                da[10][11] = 1
                                da[11][10] = 1
                                da[12][10] = 1
                        if rn[0] == 0:
                            if rn[3] == 0:
                                for j in range(3,11):da[0][j] = 3
                            for j in range(3,11):pi[0][j] = az
                            for j in range(3,11):pi[1][j] = az
                            for j in range(4,12):pi[2][j] = az
                            for j in range(4,12):pi[3][j] = az
                            for j in range(4,12):pi[4][j] = az
                            for j in range(5,13):pi[5][j] = az
                        if rn[2] == 0:
                            if rn[1] == 0:
                                for j in range(3,11):da[12][j] = 3
                            for j in range(5,13):pi[7][j] = az
                            for j in range(4,12):pi[8][j] = az
                            for j in range(4,12):pi[9][j] = az
                            for j in range(4,12):pi[10][j] = az
                            for j in range(3,11):pi[11][j] = az
                            for j in range(3,11):pi[12][j] = az
                        if rn[0] == 0 and rn[2] == 0:
                            for j in range(5,13):pi[6][j] = bz
                        m = 6 * (15 - x + y)
                        n = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                daw[m+i][n+j] = 0 
                        for i in range(2,11):daw[m+i][n+1] = 0
                        for i in range(2,11):daw[m+i][n+11] = 0
                        daw[m+5][n] = 0
                        daw[m+6][n] = 0
                        daw[m+7][n] = 0
                        daw[m+5][n+12] = 0
                        daw[m+6][n+12] = 0
                        daw[m+7][n+12] = 0
                        for i in range(13):
                            for j in range(13):
                                if pi[i][j] != (0,0,0):
                                    daw[m+i][n+j] = da[i][j]
                                    pix[m+i][n+j] = pi[i][j]
        img = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                r,g,b = pix[i][j]
                if daw[i][j] == 1:
                    r = int(r*0.9)
                    g = int(g*0.9)
                    b = int(b*0.9) 
                if daw[i][j] == 2:
                    r = int(r*0.7)+63
                    g = int(g*0.7)+63
                    b = int(b*0.7)+63
                if daw[i][j] == 3:
                    r = int(r*0.85)
                    g = int(g*0.85)
                    b = int(b*0.85)
                img.putpixel((i,j),(r,g,b,255))
        img.save(nm)
        print(f"\n\033[92m[dimo]save map as[{nm}].\n")
        img.show()
    elif line == "4":
        print("\n\033[91m[view]loading...\n")
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '| ' * v5
            op += f'{v6}[{os.path.basename(v2)}]\n'
            v7 = '| ' * (v5 + 1)
            for v8 in v4:op += f'{v7}{v8}\n'
        print(op)
        op = ''
    elif line == "5":
        print("\n\033[91m[view]loading...\n\n")
        try:
            with open(chc_c,'rb') as file:
                chc = pickle.load(file)
            with open(chc_j,'rb') as file:
                chj = pickle.load(file)
        except FileNotFoundError:
            print(f"\033[92m[core]nowhere[{chc_}]")
            continue
        for k in range(256):
            op += f"[{k}]{chj[k]}_{chc[k]}\n"
        print("\033[91m"+op)
        op = ''
    elif line == "6":
        print("\n\033[91m[view]loading...")
        try:
            with open(trr_a,'rb') as file:
                tra = pickle.load(file)
        except FileNotFoundError:
            print(f"\033[91m[core]nowhere[{trr_a}]")
            continue
        op = "[terrain list]"
        for z in range(16):
            time.sleep(2)
            print(f"\n\033[92m[z={z}]__________________________________\n")
            li = Image.open("lab.png")
            lid = ImageDraw.Draw(li)
            for y in range(16):
                for x in range(16):
                    cd = (tra[x][y][z][0],tra[x][y][z][1],tra[x][y][z][2])
                    if cd != (0,0,0):
                        lid.rectangle([16*x,16*y,16*(x+1),16*(y+1)], fill = cd)
            li.show()
        op = ''
    elif line == "7":
        with open("path",'r')as file: pa = json.load(file)
        print("\n\033[92m[zelan]define file path.")
        while True:
            mode = input("\n\033[92m[zelan]")
            if mode == "0":break
            elif mode == "1":chc_ = "chc/" + input("chc_") + "/"
            elif mode == "2":trr_ = "trr/" + input("trr_") + "/"
            elif mode == "3":flu_ = "flu/" + input("flu_") + "/"
            else:print("\033[92m[zelan]?")
        with open("path",'w')as file: json.dump({"chc_":chc_, "chc_c": chc_ + "chc", "chc_j": chc_ + "chj", "trr_": trr_, "trr_a":  trr_ + "tra", "trr_b": trr_ + "trb", "flu_": flu_},file)
    else:
        if line == "51121":print("\033[94m[某些磁砖]面对疾风吧！ovo")
        elif line == "114514" or line == "1919810" or line == "1145141919810":print("\033[94m[某些磁砖]你在挑战人类的极限！qwq")
        elif line == "-1":print("\033[94mawa")
        elif line == "qiqi" or line == "q" or line == "Q":print("\033[94mqwp")
        else:
            core = input("\n\033[94m[MageniC]need help? (reply 'yes' for text)\n")
            if core == "yes":
                with open("reference.txt","r") as file:text = file.read()
                print(text)
            elif core == "no" or core == "never":print("\033[94m[某些磁砖]awa")