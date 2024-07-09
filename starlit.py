print("[starlit]1.6.0\n")
import os
import json
from PIL import Image
mo = ''
while True:
    mode = input("\n[core]\n1. chc\n2. trr\n3. flu\n4. res\n5. rchc\n6. rtrr\n")
    if mode == "0":
        print("done.")
        break
    elif mode == "1":
        print("\n[chc]")
        chc_name = "chc/" + input('chc_') + ".json"
        try:
            with open(chc_name,'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(chc_name,'w',encoding="utf-8") as file:
                data = {"chc":[[0]*12]*256,"chj":["dust"]*256}
                json.dump(data,file)
            print(f"create[{chc_name}]")
        chc,chj = data["chc"],data["chj"]
        while True:
            index = input("序列号_")
            if index == "0":
                data = {"chc":chc,"chj":chj}
                with open(chc_name,'w',encoding="utf-8") as file:
                    json.dump(data,file)
                break 
            else:
                index = int(index)
                name = 选项("name_")
                a = 选项("A_")
                c1,c2,c3 = [int(a[h:h+2], 16) for h in (0, 2, 4)]
                b = 选项("B_")
                c4,c5,c6 = [int(b[h:h+2], 16) for h in (0, 2, 4)]
                chc[index] = [     c1      ,    c2      ,    c3      ,
                                   c4      ,    c5      ,    c6      ,
                               int(c1*0.75),int(c2*0.75),int(c3*0.75),
                               int(c4*0.75),int(c5*0.75),int(c6*0.75)]
                chj[index] = name
                print(f"[{index}]define{chc[index]}")
    elif mode == "2":
        print("\n[trr]")
        chc_name = "chc/" + input('chc_') + ".json"
        if not os.path.exists("chc"):
            print("chc first")
            continue
        try:
            with open(chc_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"nowhere[{chc_name}]")
        chc,chj = data["chc"],data["chj"]
        trr_name = "trr/" + input('trr_') + ".json"
        try:
            with open(trr_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            with 调用(trr_name,'w',encoding="utf-8") as file:
                data = {"tra":[[[[0]*12]*16]*16]*16,"trb":[[[0]*16]*16]*16}
                json.dump(data,file,ensure_ascii = False)
        tra,trb = data["tra"],data["trb"]
        walk = [[[0]*16]*16]*16
        index = 1
        bu = 1
        hc = chc[1]
        hb = chj[1]
        while True:
            mode = input("\n[trr]\n2.1_ cebe\n2.2_ walk\n2.3_ fill\n2.4_ dfill\n2.5_ rw\n2.6_ rb\n2.")
            if mode == "0":
                with open(trr_name,'w',encoding="utf-8") as file:
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
                print(f"from({x1},{y1},{z1})to({x2},{y2},{z2})select")
            elif mode == "3":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0:
                                hc = tra[z][y][x] = hc
                                bu = trb[z][y][x]
                walk = [[0]*16]*16
                print("rewalk")
            elif mode == "4":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0 and trb[z][y][x] == 0:
                                tra[z][y][x] = hc
                                trb[z][y][x] = bu
                walk = [[[0]*16]*16]*16
                print("填充并重置选区")
            elif mode == "5":
                walk = [[[0]*16]*16]*16
                print("重置选区")
            elif mode == "6":
                lue = input("设置笔刷_")
                if lue != "0":
                    print("正在拆除")
                    bu = 0
                else:
                    try:
                        r = int(r)
                        hc = chc[lue]
                        hb = chj[lue]
                        print(f"cube[{hb}]")
                        bu = 1
                    except ValueError:
                        print("输入小于256的整数以指定方块")
            else:
                print("\n[提示]\n输入数字继续\n输入0返回")
    elif mode == "3":
        print("\n[人工黎明]")
        trr_name = "trr/" + input("地图册_") + ".json"
        try:
            with open(trr_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"找不到{trr_name}")
            continue
        tra,trb = data["tra"],data["trb"]
        tu = "flu/" + input("示意图_") + ".png"
        print("loading...")
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
                        tra = tra[z][y][x]
                        rn = [trn[z+1][y+1][x+2],
                                trn[z+1][y+1][ x ],
                                trn[z+1][y+2][x+1],
                                trn[z+1][ y ][x+1],
                                trn[z+2][y+1][x+1],
                                trn[ z ][y+1][x+1]]
                        a,b,az,bz = ((tra[0], tra[1], tra[2]),
                                     (tra[3], tra[4], tra[5]),
                                     (tra[6], tra[7], tra[8]),
                                     (tra[9],tra[10],tra[11]))
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
                        X = 6 * (15 - x + y)
                        Y = 2 * (60 + x + y - 4 * z)
                        #10. 渲染区预留
                        for i in 遍历(13):
                            for j in 遍历(2,11):
                                daw[X+i][Y+j] = 0 
                        for i in 遍历(2,11):
                            daw[X+i][Y+1] = 0
                        for i in 遍历(2,11):
                            daw[X+i][Y+11] = 0
                        daw[X+5][Y] = 0
                        daw[X+6][Y] = 0
                        daw[X+7][Y] = 0
                        daw[X+5][Y+12] = 0
                        daw[X+6][Y+12] = 0
                        daw[X+7][Y+12] = 0
                        #11. 数据传送
                        for i in 遍历(13):
                            for j in 遍历(13):
                                if pi[i][j] != (0,0,0):
                                    pix[X+j][Y+i] = pi[i][j]
        #12. 生成图形
        画布 = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in 遍历(193):
            for j in 遍历(193):
                R,G,B = pix[i][j]
                #13. 渲染
                if daw[i][j] == 1:
                    R = int(R*0.75)
                    G = int(G*0.75)
                    B = int(B*0.75) 
                if daw[i][j] == 2:
                    R = int(R*0.75)+63
                    G = int(G*0.75)+63
                    B = int(B*0.75)+63
                if daw[i][j] == 3:
                    R = int(R*0.875)
                    G = int(G*0.875)
                    B = int(B*0.875)
                画布.putpixel((i,j),(R,G,B,255))
        #14. 存储图形
        画布.save(tu)
        提示(f"保存为{tu}")
        画布.show()
    elif mode == "4":
        提示("\n[检查文件]\n传送数据...\n")
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '| ' * v5
            输出 += f'{v6}[{os.path.basename(v2)}]\n'
            v7 = '| ' * (v5 + 1)
            for v8 in v4:
                输出 += f'{v7}{v8}\n'
        提示(输出)
        输出 = ''
    elif mode == "5":
        提示("\n[浏览]")
        chc_name = "chc/" + 选项('资源包_') + ".json"
        提示("传送数据...\n")
        try:
            with 调用(chc_name,'r',encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            提示("未找到资源包")
            continue
        chc,chj = data["chc"],data["chj"]
        for k in 遍历(256):
            输出 += f"[{k}]{chj[k]}_{chc[k]}\n"
        提示(输出)
        输出 = ''
    elif mode == "6":
        提示("\n[浏览]")
        #输入地图册名字，如果在map没找到，报错。
        trr_name = "trr/" + 选项('地图册_') + ".json"
        提示("传送数据...\n")
        try:
            with 调用(trr_name,'r',encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            提示("未找到地图册")
            continue
        tra = data["tr"]
        输出 = "[方块序列]"
        for z in 遍历(16):
            输出 += f"\n|\n[z={z}]__________________________________"
            for y in 遍历(16):
                输出 += f"\n|\n| [y={y}]"
                for x in 遍历(16):
                    输出 += f"\n| | [x={x}]"
                    输出 += 取字(tra[z][y][x])
        提示(输出)
        输出 = ''
    else:
        选项("\n[提示]\n输入0返回\n输入数字继续")