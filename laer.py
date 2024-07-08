print("[星光]1.6.0")

import os
import json
from PIL import Image


while True:
    
    print("\n[主页面]\n1_ 设计资源包\n2_ 设计地图\n3_ 生成图形\n4_ 检查文件")
    i1 = input("._")
    
    
    if i1 == "0":
        print("告辞。")
        break
    
    
    elif i1 == "1":
        
        print("\n[设计资源包]")
        ch = "res/" + input("输入资源册名:")
        chcn = f"{ch}/chc.json"
        chjn = f"{ch}/chj.json"
        
        di = os.path.dirname(ch)
        if not os.path.exists(ch):
            os.makedirs(ch)
            print(f"创建新的资源册{ch}")
        
        try:
            with open(chcn,'r',encoding="utf-8") as file:
                chc = json.loads(file.read())
        except FileNotFoundError:
            chc = [[0,0,0,0,0,0,0,0,0,0,0,0]] * 256
            with open(chcn,'w',encoding="utf-8") as file:
                file.write(json.dumps(chc))
            print(f"创建新的图形库{chcn}")
        try:
            with open(chjn,'r',encoding="utf-8") as file:
                chj = json.loads(file.read())
        except FileNotFoundError:
            chj = ["cube"] * 256
            with open(chjn, 'w',encoding="utf-8") as file:
                file.write(json.dumps(chj))
            print(f"创建新的译名库{chjn}")
        
        
        while True:
            i2 = input("[转到方块]_")
            
            
            if i2 == "0":
                break
            
            
            else:
                num = int(i2)
                cell = input("方块名:")
                alpha = input("面色:")
                beta = input("线色:")
                
                a1,a2,a3 = [int(alpha[i:i+2], 16) for i in (0, 2, 4)]
                a4 = int(a1 * 0.75)
                a5 = int(a2 * 0.75)
                a6 = int(a3 * 0.75)
                b1,b2,b3 = [int(beta[i:i+2], 16) for i in (0, 2, 4)]
                b4 = int(b1 * 0.75)
                b5 = int(b2 * 0.75)
                b6 = int(b3 * 0.75)
                chc[num] = [a1,a2,a3,b1,b2,b3,a4,a5,a6,b4,b5,b6]
                
                print(f"[{i2}]{chc[num]}")
                chj[num] = cell
                
                with open(chcn, 'w', encoding="utf-8") as file:
                    json.dump(chc, file, ensure_ascii=False)
                
                with open(chjn,'w',encoding="utf-8") as file:
                    json.dump(chj, file, ensure_ascii=False)


    elif i1 == "2":
        
        ch = "res/" + input("资源册:")
        chjn = f"{ch}/chj.json"
        chcn = f"{ch}/chc.json"
        
        try:
            with open(chjn,'r',encoding = "utf-8") as file:
                chj = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到资源册")
        try:
            with open(chcn,'r',encoding = "utf-8") as file:
                chc = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到图形库")
        
        mp = "map/" + input("地图册:")
        trn = f"{mp}/tr.json"
        trbn = f"{mp}/trb.json"
        
        di = os.path.dirname(mp)
        if not os.path.exists(mp):
            os.makedirs(mp)
            print(f"创建新的地图册{mp}")
        
        try:
            with open(trn,'r',encoding="utf-8") as file:
                tr = json.loads(file.read())
        except FileNotFoundError:
            tr = [[[[0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(trn, 'w',encoding="utf-8") as file:
                file.write(json.dumps(tr))
            print(f"创建新的地质库{trn}")
        
        try:
            with open(trbn,'r',encoding="utf-8") as file:
                trb = json.loads(file.read())
        except FileNotFoundError:
            trb = [[[1 for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(trbn, 'w',encoding="utf-8") as file:
                file.write(json.dumps(trb))
            print(f"创建新的地形库{trbn}")

        qu = [[[1 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        bur = 1
        lin = 1
        cb = chc[bur]
        cn = chj[bur]
        i2 = ''
        
        while True:
            
            print("\n[设计地图]\n2.1_ 放置方块\n2.2_ 选中区域\n2.3_ 处理选区\n2.4_ 设置笔刷\n2.5_ 查看目录")
            i2 = input("2._")
            
            if i2 == "0":
                break
            
            elif i2 == "1":
                
                print("[选中方块]")
                x = int(input("_"))
                y = int(input("_"))
                z = int(input("_"))
                tr[z][y][x] = cb
                trb[z][y][x] = lin
                
                print(f"放置方块于({x},{y},{z})")
                with open(trn, "w") as file:
                    json.dump(tr, file)
                with open(trbn, "w") as file:
                    json.dump(trb, file)
                
            elif i2 == "2":
                
                print("[选中区域]")
                
                print("起点:")
                x1 = int(input("_"))
                y1 = int(input("_"))
                z1 = int(input("_"))
                
                print("终点:")
                x2 = int(input("_"))
                y2 = int(input("_"))
                z2 = int(input("_"))
                
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            qu[z][y][x] = lin
                
                print(f"指向从({x1},{y1},{z1})到({x2},{y2},{z2})的方块")
                
                
                
            elif i2 == "3":
                
                print("[选区]\n2.4.1_ 填充但不替换\n2.4.2_ 填充且替换\n2.4.3_ 释放选区")
                
                i3 = input("2.4._")
                
                if i3 == "0":
                    break
                
                elif i3 == "1":
                    
                    if trb[z][y][x] != 0:
                        
                        for z in range(16):
                            for y in range(16):
                                for x in range(16):
                                    
                                    if qu[z][y][x]:
                                        
                                        tr[z][y][x] = cb
                                        trb[z][y][x] = lin
                                        
                                        with open(trn, "w") as file:
                                            json.dump(tr, file)
                                        with open(trbn, "w") as file:
                                            json.dump(trb, file)
                
                elif i3 == "2":
                    
                    for z in range(16):
                        for y in range(16):
                            for x in range(16):
                                
                                if qu[z][y][x]:
                                    
                                    tr[z][y][x] = cb
                                    trb[z][y][x] = lin
                                    
                                    with open(trn, "w") as file:
                                        json.dump(tr,file)
                                    with open(trbn, "w") as file:
                                        json.dump(trb,file)
                
                elif i3 == "3":
                    
                    qu = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                    
                    
            elif i2 == "4":
                
                bur = int(input("[设置笔刷]_"))
                
                if bur != 0:
                    cb = chc[bur]
                    cn = chj[bur]
                    print(f"持有{cn}")
                    lin = 1
                
                else:
                    print("正在拆除")
                    lin = 0
            
            elif i2 == "5":
                
                print("[方块名录]")
                
                for k in range(256):
                    print(f"[{k}]{chj[k]}")
            
    
    
    
    
    
    elif i1 == "3":
        
        print("\n[人工黎明]")
        mp = "map/" + input("地图册:")
        imn = f"{mp}/map.png"
        trn = f"{mp}/tr.json"
        trbn = f"{mp}/trb.json"
        
        try:
            with open(trn,'r',encoding="utf-8") as file:
                tr = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到地质库")
        
        try:
            with open(trbn,'r',encoding="utf-8") as file:
                trb = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到地形库")
        
        tr_n = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] != 0:
                        tr_n[z+1][y+1][x+1] = 1
        
        tr_r = [[[[0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        for z in range(1,17):
            for y in range(1,17):
                for x in range(1,17):
                    tr_r[z-1][y-1][x-1] = [tr_n[z][y][x + 1],
                                           tr_n[z][y][x - 1],
                                           tr_n[z][y + 1][x],
                                           tr_n[z][y - 1][x],
                                           tr_n[z + 1][y][x],
                                           tr_n[z - 1][y][x]]
        
        
        
        
        
        
        
        ai = [[(0,0,0) for _ in range(193)] for _ in range(193)]
        be = [[0 for _ in range(193)] for _ in range(193)]
        
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] == 1:
                        
                        s = [[0 for _ in range(13)]for _ in range(13)]
                        h = [[(0,0,0) for _ in range(13)]for _ in range(13)]
                                                
                        r = tr_r[z][y][x]
                        o = tr[z][y][x]
                        a = (o[0],o[1],o[2])
                        b = (o[3],o[4],o[5])
                        a0 = (o[6],o[7],o[8])
                        b0 = (o[9],o[10],o[11])
                        
                        if r[4] == 0:
                            
                            for i in range(2,11):
                                for j in range(1,2):
                                    h[i][j] = a
                            
                            h[0][5] = a
                            h[0][6] = a
                            h[0][7] = a
                            h[3][5] = a
                            h[3][6] = a
                            h[3][7] = a
                            
                            if r[3] == 0:
                                s[0][5] = 2
                                s[0][6] = 2
                                s[0][7] = 2
                                s[1][8] = 2
                                s[1][9] = 2
                                s[1][10] = 2
                                
                            if r[1] == 0:
                                s[1][2] = 2
                                s[1][3] = 2
                                s[1][4] = 2
                                s[0][5] = 2
                                s[0][6] = 2
                                s[0][7] = 2
                                
                            if r[0] == 0:
                                h[2][0] = b
                                h[2][1] = b
                                h[3][2] = b
                                h[3][3] = b
                                h[3][4] = b
                                h[4][5] = b
                                h[4][6] = b
                                
                            if r[2] == 0:
                                h[2][12] = b
                                h[2][11] = b
                                h[3][10] = b
                                h[3][9] = b
                                h[3][8] = b
                                h[4][7] = b
                                h[4][6] = b
                                
                        if r[5] == 0:
                            
                            if r[2] == 0:
                                s[10][0] = 1
                                s[10][1] = 1
                                s[11][2] = 1
                                s[11][3] = 1
                                s[11][4] = 1
                                s[12][5] = 1
                                
                            if r[0] == 0:
                                s[10][11] = 1
                                s[10][12] = 1
                                s[11][8] = 1
                                s[11][9] = 1
                                s[11][10] = 1
                                s[12][7] = 1
                                
                        if r[0] == 0:
                            
                            for i in range(5,11):
                                for j in range(5):
                                    h[i][j] = a0
                                    
                            i = 4
                            for j in range(5):
                                h[i][j] = a0
                            
                            i = 11
                            for j in range(2,6):
                                h[i][j] = a0
                            
                            h[3][0] = a0
                            h[3][1] = a0
                            h[12][5] = a0
                            
                            if r[3] == 0:
                                
                                for k in range(3,11):
                                    s[k][12] = 3
                        if r[2] == 0:
                            
                            for i in range(5,11):
                                for j in range(7,13):
                                    h[i][j] = a0
                            
                            i = 4
                            for j in range(8,13):
                                h[i][j] = a0
                            
                            i = 11
                            for j in range(7,11):
                                h[i][j] = a0
                            
                            h[3][11] = a0
                            h[3][12] = a0
                            h[12][7] = a0
                            
                            if r[1] == 0:
                                for k in range(3,11):
                                    s[k][0] = 3
                        
                        if r[0] == 0 and r[2] == 0:
                            
                            for k in range(5,13):
                                h[k][6] = b0
                                s[k][6] = 1
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        m = 6 * (15 + x - y)
                        n = 2 * (60 + x + y - 4 * z)
                        
                        for i in range(13):
                            for j in range(2,11):
                                
                                be[m+i][n+j] = 0
                        
                        
                        be[m+5][n+12] = 0
                        be[m+6][n+12] = 0
                        be[m+7][n+12] = 0
                        be[m+5][n+1] = 0
                        be[m+6][n+1] = 0
                        be[m+7][n+1] = 0
                        
                        j = 1
                        for i in range(2,11):
                            be[m+i][n+j] = 0
                        
                        j = 11
                        for i in range(2,11):
                            be[m+i][n+j] = 0
                        
                        
                        for i in range(13):
                            for j in range(13):
                                
                                ai[m+j][n+i] = h[i][j]
                                be[m+j][n+i] = s[i][j]
                           
        im = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        
        for i in range(193):
            for j in range(193):
                
                ar,ag,ab = ai[i][j]
                
                if be[i][j] == 1:
                    ar = int(ar*0.75)
                    ag = int(ag*0.75)
                    ab = int(ab*0.75)
                    
                if be[i][j] == 2:
                    ar = int(ar*0.75)+63
                    ag = int(ag*0.75)+63
                    ab = int(ab*0.75)+63
                    
                if be[i][j] == 3:
                    ar = int(ar*0.875)
                    ag = int(ag*0.875)
                    ab = int(ab*0.875)
                    
                im.putpixel((i,j),(ar,ag,ab,255))
                
        im.save(imn)
        print(f"saved as {imn}.")
        im.show()
        
        
        
        
        
        
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