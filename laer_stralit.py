print("[星光]1.6.0")

import os
import json
from PIL import Image
def pos(x,y,z):
    m = 15 + x - y
    n = 60 + x + y - 4 * z
    return m * 6, n * 2

while True:
    print("\n[主页面]\n1_ 设计资源包\n2_ 设计地图\n3_ 生成图形\n4_ 检查文件")
    i1 = input("._")
    if i1 == "0":
        print("告辞。")
        break
    elif i1 == "1":
        print("\n[设计资源包]")
        ch = "res/" + input("输入资源册名:")
        chc_n = f"{ch}/chc.json"
        chj_n = f"{ch}/chj.json"
        di = os.path.dirname(ch)
        if not os.path.exists(ch):
            os.makedirs(ch)
            print(f"创建新的资源册{ch}")
        try:
            with open(chc_n,'r') as file:
                data = file.read()
            chc = json.loads(data)
        except FileNotFoundError:
            chc = [(0,0,0,0,0,0,0,0,0,0,0,0)] * 256
            json_data = json.dumps(chc)
            with open(chc_n, 'w') as file:
                file.write(json_data)
            print(f"创建新的图形库{chc_n}")
        try:
            with open(chj_n,'r') as file:
                data = file.read()
            chj = json.loads(data)
        except FileNotFoundError:
            chj = ["cube"] * 256
            json_data = json.dumps(chj)
            with open(chj_n, 'w') as file:
                file.write(json_data)
            print(f"创建新的译名库{chj_n}")
        while True:
            inp = input("[通过序列号转到方块]_")
            if inp == "0":
                for k in range(256):
                    print(f"[{k}]{chj[k]}:{chc[k]}")
                break
            else:
                n = int(inp)
                c = input("方块名:")
                a = input("面色:")
                b = input("线色:")
                a = [int(a[i:i+2], 16) for i in (0, 2, 4)]
                ac = [int(u * 0.75) for u in a]
                b = [int(b[i:i+2], 16) for i in (0, 2, 4)]
                bc = [int(u * 0.75) for u in b]
                chc[n] = a+b+ac+bc
                chj[n] = c
                with open(chc_n,'w',encoding="utf-8") as file:
                    file.write(str(chc))
                with open(chj_n,'w',encoding="utf-8") as file:
                    file.write(str(chj))
    elif i1 == "2":
        ch = "res/" + input("输入资源册名:")
        chj_n = f"{ch}/chj.json"
        try:
            with open(chj_n,'r',encoding = "utf-8") as file:
                data = file.read()
            chj = json.loads(data)
        except FileNotFoundError:
            print("请先制作或导入资源册")
        chc_n = f"{ch}/chc.json"
        with open(chc_n,'r') as file:
            data = file.read()
        chc = json.loads(data)
        mp = "map/" + input("输入地图册名:")
        trr_n = f"{mp}/trr.json"
        di = os.path.dirname(mp)
        if not os.path.exists(mp):
            os.makedirs(mp)
            print(f"创建新的地图册{mp}")
        try:
            with open(trr_n,'r') as file:
                data = file.read()
            trr = json.loads(data)
        except FileNotFoundError:
            trr = [[[0 for _ in range(16)]for _ in range(16)]for _ in range(16)]
            json_data = json.dumps(trr)
            with open(trr_n, 'w') as file:
                file.write(json_data)
            print(f"创建新的地质库{chj_n}")
        qu = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        bru = 1
        cb = chc[bur]
        cn = chj[bur]
        i2 = ''
        for k in range(256):
            print(f"[{k}]{chj[k]}")
        while True:
            print("\n[设计地图]\n2.1_ 选中方块\n2.2_ 选中区域\n2.3_ 设置笔刷\n2.4_ 处理选区")
            i2 = input("2._")
            if i2 == "0":
                print("[返回]")
                print(trr)
                break
            elif i2 == "1":
                print("[选中方块]")
                x = int(input("x_"))
                y = int(input("y_"))
                z = int(input("z_"))
                trr[z][y][x] = cb
                print(f"放置方块于({x},{y},{z})")
                with open(trr_n, "w") as file:
                    json.dump(trr, file)
            elif i2 == "2":
                print("[选中区域]")
                print("from")
                x1 = int(input("_"))
                y1 = int(input("_"))
                z1 = int(input("_"))
                print("to")
                x2 = int(input("_"))
                y2 = int(input("_"))
                z2 = int(input("_"))
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            qu[z][y][x] = 1
                print(f"指向从({x1},{y1},{z1})到({x2},{y2},{z2})的方块")
            elif i2 == "3":
                bur = int(input("[设置笔刷]_"))
                if bur != 0:
                    cb = chc[bur]
                    cn = chj[bur]
                    print(f"持有{cn}")
                else:
                    print("正在拆除")
            elif i2 == "4":
                print("[选区]\n2.4.1_ 填充但不替换\n2.4.2_填充且替换\n2.4.3_ 释放选区")
                i3 = input("2.4._")
                if i3 == "1":
                    if trr[bur] != (0,0,0,0,0,0,0,0,0,0,0,0):
                        for z in range(16):
                            for y in range(16):
                                for x in range(16):
                                    if qu[z][y][x]:
                                        trr[z][y][x] = cb
                                        with open(trr_n, "w") as file:
                                            json.dump(trr, file)
                if i3 == "2":
                    for z in range(16):
                        for y in range(16):
                            for x in range(16):
                                if qu[z][y][x]:
                                    trr[z][y][x] = cb
                                    with open(trr_n, "w") as file:
                                        json.dump(trr, file)
                if i3 == "3":
                    qu = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
    elif i1 == "3":
        print("[人工黎明]")
        im_n = input("图像:")+".png"
        tr_n = input("地图册:")+".json"

        with open(tr_name) as file:
            tr = json.load(file)
        tr_n = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if tr[z][y][x] == 1:
                        tr_n[z+1][y+1][x+1] = 1
        tr_r = [[[[0,0,0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        for z in range(1,17):
            for y in range(1,17):
                for x in range(1,17):
                    tr_r[z-1][y-1][x-1] = [tr_n[z][y][x + 1],
                                           tr_n[z][y][x - 1],
                                           tr_n[z][y + 1][x],
                                           tr_n[z][y - 1][x],
                                           tr_n[z + 1][y][x],
                                           tr_n[z - 1][y][x],
                                           tr_n[z][y-1][x+1],
                                           tr_n[z][y+1][x-1]]
        B = [[0 for _ in range(193)] for _ in range(193)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if tr[z][y][x] == 1:
                        r = tr_r[z][y][x]
                        s = [[0 for _ in range(13)] for _ in range(13)]
                        if r[4] == 0 and r[3] == 0:
                            s[0][5] = 1
                            s[0][6] = 1
                            s[0][7] = 1
                            s[1][8] = 1
                            s[1][9] = 1
                            s[1][10] = 1
                        if r[4] == 0 and r[1] == 0:
                            s[1][2] = 1
                            s[1][3] = 1
                            s[1][4] = 1
                            s[0][5] = 1
                            s[0][6] = 1
                            s[0][7] = 1
                        if r[5] == 0 and r[2] == 0:
                            s[10][0] = 1
                            s[10][1] = 1
                            s[11][2] = 1
                            s[11][3] = 1
                            s[11][4] = 1
                            s[12][5] = 1
                        if r[5] == 0 and r[0] == 0:
                            s[10][11] = 1
                            s[10][12] = 1
                            s[11][8] = 1
                            s[11][9] = 1
                            s[11][10] = 1
                            s[12][7] = 1
                        if r[0] == 0 and r[3] == 0 and r[6] == 0:
                            for k in range(3,11):
                                s[k][12] = 1
                        if r[1] == 0 and r[2] == 0 and r[7] == 0:
                            for k in range(3,11):
                                s[k][0] = 1
                        if r[0] == 0 and r[2] == 0:
                            for k in range(5,13):
                                s[k][6] = 1
                        m,n = pos(x,y,z)
                        for i in range(13):
                            for j in range(2,11):
                                B[m+i][n+j] = 0
                        B[m+5][n] = 0
                        B[m+6][n+12] = 0
                        B[m+7][n+12] = 0
                        j = 12
                        B[m+5][n+12] = 0
                        B[m+6][n+12] = 0
                        B[m+7][n+12] = 0
                        j = 1
                        for i in range(2,11):
                            B[m+i][n+j] = 0
                        j = 11
                        for i in range(2,11):
                            B[m+i][n+j] = 0
                        for i in range(13):
                            for j in range(13):
                                if s[i][j]:
                                    B[m+j][n+i] = 1
        im = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                if B[i][j]:
                    im.putpixel((i,j),(0,0,0,255))
        im.save(im_name)
        print(f"saved as {im_name}.")
    elif i1 == "4":
        h1 = os.path.abspath('.')
        for h2, h3, h4 in os.walk(h1):
            h5 = h2.replace(h1,'').count(os.sep)
            h6 = '|   ' * h5
            print(f'{h6}[{os.path.basename(h2)}]')
            h7 = '|   ' * (h5 + 1)
            for h8 in h4:
                print(f'{h7}{h8}')
    else:
        print("\n[参考文档]\n输入0返回\n输入数字继续")