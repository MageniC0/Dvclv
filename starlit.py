print("[starlit]1.6.0\n")
import os
import json
from PIL import Image
op = ""
while True:
    mode = input("\n[core]\n1. dust chc\n2. dust trr\n3. dust flu\n4. view res\n5. view chc\n6. view trr\n")
    if mode == "0":
        print("[core]done.")
        break
    elif mode == "1":
        print("\n[chc]")
        chc_n = "chc/" + input("chc_") + ".json"
        try:
            with open(chc_n,'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(chc_n,'w',encoding="utf-8") as file:
                data = {"chc":[[0]*12]*256,"chj":["dust"]*256}
                json.dump(data,file)
            print(f"[chc]create[{chc_n}]")
        chc,chj = data["chc"],data["chj"]
        while True:
            index = input("[chc]index_")
            if index == "0":
                data = {"chc":chc,"chj":chj}
                with open(chc_n,'w',encoding="utf-8") as file:
                    json.dump(data,file)
                break 
            else:
                index = int(index)
                name = input("[chc]name_")
                a = input("[chc]A_")
                c1,c2,c3 = [int(a[h:h+2], 16) for h in (0, 2, 4)]
                b = input("[chc]B_")
                c4,c5,c6 = [int(b[h:h+2], 16) for h in (0, 2, 4)]
                chc[index] = [     c1      ,    c2      ,    c3      ,
                                   c4      ,    c5      ,    c6      ,
                               int(c1*0.75),int(c2*0.75),int(c3*0.75),
                               int(c4*0.75),int(c5*0.75),int(c6*0.75)]
                chj[index] = name
                print(f"[chc]define{[index]}{chc[index]}")
    elif mode == "2":
        print("\n[trr]")
        chc_n = "chc/" + input('chc_') + ".json"
        if not os.path.exists("chc"):
            print("[trr]chc first")
            continue
        try:
            with open(chc_n, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"[trr]nowhere[{chc_n}]")
        chc,chj = data["chc"],data["chj"]
        trr_n = "trr/" + input('trr_') + ".json"
        try:
            with open(trr_n, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(trr_n,'w',encoding="utf-8") as file:
                data = {"tra":[[[[0]*12]*16]*16]*16,"trb":[[[0]*16]*16]*16}
                json.dump(data,file,ensure_ascii = False)
            print(f"[trr]create[{trr_n}]")
        tra,trb = data["tra"],data["trb"]
        walk = [[[0]*16]*16]*16
        index = 1
        bu = 1
        hc = chc[1]
        hb = chj[1]
        while True:
            mode = input("\n[trr]\n2.1_ set only cube\n2.2_ walk\n2.3_ fill walk\n2.4_ fill walk with destroy\n2.5_ rewalk\n2.6_ select cube\n2.")
            if mode == "0":
                with open(trr_n,'w',encoding="utf-8") as file:
                    json.dump({"tra":tra,"trb":trb},file)
                break
            elif mode == "1":
                print("[pos]")
                x = int(input("_"))
                y = int(input("_"))
                z = int(input("_"))
                tra[z][y][x] = hc
                trb[z][y][x] = bu
                print(f"set[{hb}]at({x},{y},{z})")
            elif mode == "2":
                print("[from]")
                x1 = int(input("_"))
                y1 = int(input("_"))
                z1 = int(input("_"))
                print("[to]")
                x2 = int(input("_"))
                y2 = int(input("_"))
                z2 = int(input("_"))
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            walk[z][y][x] = bu
                print(f"[trr]walk from({x1},{y1},{z1})to({x2},{y2},{z2})")
            elif mode == "3":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0:
                                hc = tra[z][y][x] = hc
                                bu = trb[z][y][x]
                walk = [[0]*16]*16
                print("[trr]rewalk")
            elif mode == "4":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0 and trb[z][y][x] == 0:
                                tra[z][y][x] = hc
                                trb[z][y][x] = bu
                walk = [[[0]*16]*16]*16
                print("[trr]fill")
            elif mode == "5":
                walk = [[[0]*16]*16]*16
                print("[trr]reselect")
            elif mode == "6":
                lue = input("[trr]set cube_")
                if lue != "0":
                    print("[trr]delet")
                    bu = 0
                else:
                    try:
                        r = int(r)
                        hc = chc[lue]
                        hb = chj[lue]
                        print(f"[trr]cube[{hb}]")
                        bu = 1
                    except ValueError:
                        print("[core]input 1~255 for cube or 0 for deleting")
            else:
                print("\n[core]\ninput number for continue\n input 0 for going back")
    elif mode == "3":
        print("\n[dvclv]")
        trr_n = "trr/" + input("trr_") + ".json"
        try:
            with open(trr_n, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"[demo]nowhere{trr_n}")
            continue
        tra,trb = data["tra"],data["trb"]
        tu = "map/" + input("map_") + ".png"
        print("[dimo]loading...")
        trn = [[[0]*18]*18]*18
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] != 0:
                        trn[z+1][y+1][x+1] = 1
        pix = [[(0,0,0)]*193]*193
        daw = [[0]*193]*193
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] == 1:
                        pi = [[(0,0,0)]*13]*13
                        da = [[0]*13]*13
                        t = tra[z][y][x]
                        rn = [trn[z+1][y+1][x+2],
                              trn[z+1][y+1][ x ],
                              trn[z+1][y+2][x+1],
                              trn[z+1][ y ][x+1],
                              trn[z+2][y+1][x+1],
                              trn[ z ][y+1][x+1]]
                        a,b,az,bz = ((t[0],t[1],t[2]),
                                     (t[3],t[4],t[5]),
                                     (t[6],t[7],t[8]),
                                     (t[9],t[10],t[11]))
                        if rn[4] == 0:
                            for j in range(2,11):
                                pi[1][j] = a
                            for j in range(2,11):
                                pi[2][j] = a
                            pi[0][5] = a
                            pi[0][6] = a
                            pi[0][7] = a
                            pi[3][5] = a
                            pi[3][6] = a
                            pi[3][7] = a
                            if rn[0] == 0:
                                pi[2][0] = b
                                pi[2][1] = b
                                pi[3][2] = b
                                pi[3][3] = b
                                pi[3][4] = b
                                pi[4][5] = b
                                pi[4][6] = b
                            if rn[1] == 0:
                                da[0][5] = 2
                                da[0][6] = 2
                                da[0][7] = 2
                                da[1][8] = 2
                                da[1][9] = 2
                                da[1][10] = 2
                            if rn[2] == 0:
                                pi[2][12] = b
                                pi[2][11] = b
                                pi[3][10] = b
                                pi[3][9] = b
                                pi[3][8] = b
                                pi[4][7] = b
                                pi[4][6] = b
                            if rn[3] == 0:
                                da[0][7] = 2
                                da[0][6] = 2
                                da[0][5] = 2
                                da[1][4] = 2
                                da[1][3] = 2
                                da[1][2] = 2
                        if rn[5] == 0:
                            if rn[0] == 0:
                                da[10][0] = 1
                                da[10][1] = 1
                                da[11][2] = 1
                                da[11][3] = 1
                                da[11][4] = 1
                                da[12][5] = 1 
                            if rn[2] == 0:
                                da[10][12] = 1
                                da[10][11] = 1
                                da[11][10] = 1
                                da[11][9] = 1
                                da[11][8] = 1
                                da[12][7] = 1
                        if rn[0] == 0:
                            if rn[3] == 0:
                                for k in range(3,11):
                                    da[k][12] = 3
                            for i in range(3,11):
                                pi[i][0] = az
                            for i in range(3,11):
                                pi[i][1] = az
                            for i in range(4,12):
                                pi[i][2] = az 
                            for i in range(4,12):
                                pi[i][3] = az  
                            for i in range(4,12):
                                pi[i][4] = az
                            for i in range(5,13):
                                pi[i][5] = az
                        if rn[2] == 0:
                            if rn[1] == 0:
                                for k in range(3,11):
                                    da[k][12] = 3
                            for i in range(5,13):
                                pi[i][12] = az
                            for i in range(5,13):
                                pi[i][11] = az
                            for i in range(4,12):
                                pi[i][10] = az 
                            for i in range(4,12):
                                pi[i][9] = az  
                            for i in range(4,12):
                                pi[i][8] = az
                            for i in range(3,11):
                                pi[i][7] = az
                        if rn[0] == 0 and rn[2] == 0:
                            for k in range(5,13):
                                pi[k][6] = bz
                        m = 6 * (15 - x + y)
                        n = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                daw[m+i][n+j] = 0 
                        for i in range(2,11):
                            daw[m+i][n+1] = 0
                        for i in range(2,11):
                            daw[m+i][n+11] = 0
                        daw[m+5][n] = 0
                        daw[m+6][n] = 0
                        daw[m+7][n] = 0
                        daw[m+5][n+12] = 0
                        daw[m+6][n+12] = 0
                        daw[m+7][n+12] = 0
                        for i in range(13):
                            for j in range(13):
                                if pi[i][j] != (0,0,0):
                                    pix[m+j][n+i] = pi[i][j]
        img = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                r,g,b = pix[i][j]
                if daw[i][j] == 1:
                    r = int(r*0.75)
                    g = int(g*0.75)
                    b = int(b*0.75) 
                if daw[i][j] == 2:
                    r = int(r*0.75)+63
                    g = int(g*0.75)+63
                    b = int(b*0.75)+63
                if daw[i][j] == 3:
                    r = int(r*0.875)
                    g = int(g*0.875)
                    b = int(b*0.875)
                img.putpixel((i,j),(r,g,b,255))
        img.save(tu)
        print(f"[dimo]save[{tu}]")
        img.show()
    elif mode == "4":
        print("\n[view]\nloading...\n")
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '| ' * v5
            op += f'{v6}[{os.path.basename(v2)}]\n'
            v7 = '| ' * (v5 + 1)
            for v8 in v4:
                op += f'{v7}{v8}\n'
        print(op)
        op = ''
    elif mode == "5":
        print("\n[view]")
        chc_n = "chc/" + input('chc_') + ".json"
        print("[core]loading...\n")
        try:
            with open(chc_n,'r',encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("[core]nowhere[{chc_n}]")
            continue
        chc,chj = data["chc"],data["chj"]
        for k in range(256):
            op += f"[{k}]{chj[k]}_{chc[k]}\n"
        print(op)
        op = ''
    elif mode == "6":
        print("\n[view]")
        trr_n = "trr/" + input('trr_') + ".json"
        print("[core]loading...\n")
        try:
            with open(trr_n,'r',encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("[core]nowhere[{trr_n}]")
            continue
        tra = data["tr"]
        op = "[list]"
        for z in range(16):
            op += f"\n|\n[z={z}]__________________________________"
            for y in range(16):
                op += f"\n|\n| [y={y}]"
                for x in range(16):
                    op += f"\n| | [x={x}]"
                    op += str(tra[z][y][x])
        print(op)
        op = ''
        print("qwp")
    else:
        print("\n[core]\ninput number for continue\ninput 0 for going back")
        if mode == "51121":
            print("[某些磁砖]面对疾风吧！")
        elif mode == "114514" or mode == "1919810" or mode == "1145141919810":
            print("[某些磁砖]你在挑战人类的极限！qwq")
        elif mode == "-1":
            print("awa")
        elif mode == "qiqi" or mode == "q":
            print("qwp")
        else:
            core = input()