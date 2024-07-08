print("[星光]1.6.0\n")
import os
import json
from PIL import Image
while True:
    print("\n[主页面]\n1_ 设计资源册\n2_ 设计地图\n3_ 生成图形\n4_ 检查文件")
    h1 = input("._")
    if h1 == "0":
        break
    elif h1 == "1":
        print("\n[设计资源册]")
        h2 = "res/" + input("输入资源册名:")
        h3 = f"{h2}/chc.json"
        h4 = f"{h2}/chj.json"
        di = os.path.dirname(h2)
        if not os.path.exists(h2):
            os.makedirs(h2)
            print(f"创建新的{h2}")
        try:
            with open(h3,'r',encoding="utf-8") as file:
                h5 = json.loads(file.read())
        except FileNotFoundError:
            h5 = [[0,0,0,0,0,0,0,0,0,0,0,0]] * 256
            with open(h3,'w',encoding="utf-8") as file:
                file.write(json.dumps(h5))
            print(f"创建新的{h3}")
        try:
            with open(h4,'r',encoding="utf-8") as file:
                h6 = json.loads(file.read())
        except FileNotFoundError:
            h6 = ["cube"] * 256
            with open(h4, 'w',encoding="utf-8") as file:
                file.write(json.dumps(h6))
            print(f"创建新的{h4}")
        while True:
            h11 = input("[转到方块]_")
            if h11 == "0":
                break         
            else:
                h7 = int(h11)
                h8 = input("方块名:")
                h9 = input("面色:")
                h10 = input("线色:")
                c1,c2,c3 = [int(h9[h:h+2], 16) for h in (0, 2, 4)]
                c4,c5,c6 = [int(h10[h:h+2], 16) for h in (0, 2, 4)]
                h5[h7] = [c1,c2,c3,c4,c5,c6,int(c1*0.75),int(c2*0.75),int(c3*0.75),int(c4*0.75),int(c5*0.75),int(c6*0.75)]
                print(f"[{h11}]{h5[h7]}")
                h6[h7] = h8
                with open(h3, 'w', encoding="utf-8") as file:
                    json.dump(h5, file, ensure_ascii=False)
                with open(h4,'w',encoding="utf-8") as file:
                    json.dump(h6, file, ensure_ascii=False)
    elif h1 == "2":
        h2 = "res/" + input("资源册:")
        h4 = f"{h2}/chj.json"
        h3 = f"{h2}/chc.json"
        try:
            with open(h4,'r',encoding = "utf-8") as file:
                h6 = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到资源册")
        try:
            with open(h3,'r',encoding = "utf-8") as file:
                h5 = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到图形库")
        h12 = "map/" + input("地图册:")
        h13 = f"{h12}/tr.json"
        h14 = f"{h12}/trb.json"
        di = os.path.dirname(h12)
        if not os.path.exists(h12):
            os.makedirs(h12)
            print(f"创建新的地图册{h12}")
        try:
            with open(h13,'r',encoding="utf-8") as file:
                h15 = json.loads(file.read())
        except FileNotFoundError:
            h15 = [[[[0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(h13, 'w',encoding="utf-8") as file:
                file.write(json.dumps(h15))
            print(f"创建新的地质库{h13}")
        try:
            with open(h14,'r',encoding="utf-8") as file:
                h16 = json.loads(file.read())
        except FileNotFoundError:
            h16 = [[[0 for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(h14, 'w',encoding="utf-8") as file:
                file.write(json.dumps(h16))
            print(f"创建新的地形库{h14}")
        h17 = [[[1 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        c = 1
        d6 = 1
        h18 = h5[c]
        h19 = h6[c]
        h11 = ''  
        while True:
            print("\n[设计地图]\n2.1_ 放置方块\n2.2_ 选中区域\n2.3_ 处理选区\n2.4_ 设置笔刷\n2.5_ 查看目录")
            h11 = input("2._")
            if h11 == "0":
                break
            elif h11 == "1":
                print("[选中方块]")
                x = int(input("_"))
                y = int(input("_"))
                z = int(input("_"))
                h15[z][y][x] = h18
                h16[z][y][x] = d6
                print(f"放置方块于({x},{y},{z})")
                with open(h13, "w") as file:
                    json.dump(h15, file)
                with open(h14, "w") as file:
                    json.dump(h16, file)
            elif h11 == "2":
                print("[选中区域]")
                print("选中起点:")
                x1 = int(input("_"))
                y1 = int(input("_"))
                z1 = int(input("_"))
                print("选中终点:")
                x2 = int(input("_"))
                y2 = int(input("_"))
                z2 = int(input("_"))
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            h17[z][y][x] = d6
                print(f"指向从({x1},{y1},{z1})到({x2},{y2},{z2})的方块")
            elif h11 == "3":
                print("[选区]\n2.4.1_ 填充但不替换\n2.4.2_ 填充且替换\n2.4.3_ 释放选区")
                i3 = input("2.4._")
                if i3 == "0":
                    break
                elif i3 == "1":
                    if h16[z][y][x] != 0:
                        for z in range(16):
                            for y in range(16):
                                for x in range(16):
                                    if h17[z][y][x]:
                                        h15[z][y][x] = h18
                                        h16[z][y][x] = d6
                                        with open(h13, "w") as file:
                                            json.dump(h15, file)
                                        with open(h14, "w") as file:
                                            json.dump(h16, file)
                elif i3 == "2":
                    for z in range(16):
                        for y in range(16):
                            for x in range(16):
                                if h17[z][y][x]:
                                    h15[z][y][x] = h18
                                    h16[z][y][x] = d6
                                    with open(h13, "w") as file:
                                        json.dump(h15,file)
                                    with open(h14, "w") as file:
                                        json.dump(h16,file)
                elif i3 == "3":
                    h17 = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
            elif h11 == "4":
                c = int(input("[设置笔刷]_"))
                if c != 0:
                    h18 = h5[c]
                    h19 = h6[c]
                    print(f"持有{h19}")
                    d6 = 1
                else:
                    print("正在拆除")
                    d6 = 0
            elif h11 == "5":
                print("[方块名录]")
                for k in range(256):
                    print(f"[{k}]{h6[k]}")
    #done⬆️
    
    #something hard⬇️
    elif h1 == "3":
        print("\n[人工黎明]")
        h12 = "map/" + input("地图册:")
        h20 = f"{h12}/map.png"
        h13 = f"{h12}/tr.json"
        h14 = f"{h12}/trb.json"
        try:
            with open(h13,'r',encoding="utf-8") as file:
                h15 = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到地质库") 
        try:
            with open(h14,'r',encoding="utf-8") as file:
                h16 = json.loads(file.read())
        except FileNotFoundError:
            print(f"未找到地形库") 
        d1 = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if h16[z][y][x] != 0:
                        d1[z+1][y+1][x+1] = 1 
        d2 = [[[[0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        for z in range(1,17):
            for y in range(1,17):
                for x in range(1,17):
                    d2[z-1][y-1][x-1] = [d1[z][y][x + 1],
                                         d1[z][y][x - 1],
                                         d1[z][y + 1][x],
                                         d1[z][y - 1][x],
                                         d1[z + 1][y][x],
                                         d1[z - 1][y][x]]
        d3 = [[(0,0,0) for _ in range(193)] for _ in range(193)]
        d4 = [[0 for _ in range(193)] for _ in range(193)]      
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if h16[z][y][x] == 1:
                        d5 = [[0 for _ in range(13)]for _ in range(13)]
                        d6 = [[(0,0,0) for _ in range(13)]for _ in range(13)]
                        h21 = d2[z][y][x]
                        o = h15[z][y][x]
                        u0,u1,u2,u3 = ((o[0],o[1],o[2]),
                                       (o[3],o[4],o[5]),
                                       (o[6],o[7],o[8]),
                                       (o[9],o[10],o[11]))
                        if h21[4] == 0:
                            for j in range(2,11):
                                d6[1][j] = u0
                            for j in range(2,11):
                                d6[2][j] = u0
                            d6[0][5] = u0
                            d6[0][6] = u0
                            d6[0][7] = u0
                            d6[3][5] = u0
                            d6[3][6] = u0
                            d6[3][7] = u0
                            if h21[0] == 0:
                                d6[2][11] = u1
                                d6[2][12] = u1
                                d6[3][8] = u1
                                d6[3][9] = u1
                                d6[3][10] = u1
                                d6[4][6] = u1
                                d6[4][7] = u1
                            if h21[1] == 0:
                                d5[0][5] = 2
                                d5[0][6] = 2
                                d5[0][7] = 2
                                d5[1][2] = 2
                                d5[1][3] = 2
                                d5[1][4] = 2
                            if h21[2] == 0:
                                d6[2][1] = u1
                                d6[2][0] = u1
                                d6[3][4] = u1
                                d6[3][3] = u1
                                d6[3][2] = u1
                                d6[4][6] = u1
                                d6[4][5] = u1
                            if h21[3] == 0:
                                d5[0][7] = 2
                                d5[0][6] = 2
                                d5[0][5] = 2
                                d5[1][10] = 2
                                d5[1][9] = 2
                                d5[1][8] = 2
                        if h21[5] == 0:
                            if h21[0] == 0:
                                d5[10][12] = 1
                                d5[10][11] = 1
                                d5[11][10] = 1
                                d5[11][9] = 1
                                d5[11][8] = 1
                                d5[12][5] = 1 
                            if h21[2] == 0:
                                d5[10][1] = 1
                                d5[10][0] = 1
                                d5[11][4] = 1
                                d5[11][3] = 1
                                d5[11][2] = 1
                                d5[12][5] = 1
                        if h21[0] == 0:
                            if h21[3] == 0:
                                for k in range(3,11):
                                    d5[k][12] = 3
                            for i in range(3,11):
                                d6[i][12] = u2
                            for i in range(3,11):
                                d6[i][11] = u2
                            for i in range(4,12):
                                d6[i][10] = u2 
                            for i in range(4,12):
                                d6[i][9] = u2  
                            for i in range(4,12):
                                d6[i][8] = u2
                            for i in range(5,13):
                                d6[i][7] = u2
                            if h21[3] == 0:
                                if h21[1] == 0:
                                    for k in range(3,11):
                                        d5[k][0] = 3
                        if h21[2] == 0:
                            for i in range(5,13):
                                d6[i][5] = u2
                            for i in range(4,12):
                                d6[i][4] = u2
                            for i in range(4,12):
                                d6[i][3] = u2 
                            for i in range(4,12):
                                d6[i][2] = u2  
                            for i in range(3,11):
                                d6[i][1] = u2
                            for i in range(3,11):
                                d6[i][0] = u2
                            if h21[1] == 0:
                                for i in range(5,11):
                                    for j in range(8):
                                        d6[i][j] = u2
                        if h21[0] == 0 and h21[2] == 0:
                            for k in range(5,13):
                                d6[k][6] = u3
                                
                                
                                #图形生成
                        m = 6 * (15 + x - y)
                        n = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                d4[m+i][n+j] = 0 
                        for i in range(2,11):
                            d4[m+i][n+1] = 0
                        for i in range(2,11):
                            d4[m+i][n+11] = 0
                        d4[m+5][n] = 0
                        d4[m+6][n] = 0
                        d4[m+7][n] = 0
                        d4[m+5][n+12] = 0
                        d4[m+6][n+12] = 0
                        d4[m+7][n+12] = 0
                        
                        for i in range(13):
                            for j in range(13):
                                if d6[i][j] != (0,0,0):
                                    d3[m+j][n+i] = d6[i][j]
                                    d4[m+j][n+i] = d5[i][j]
        d = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                ar,ag,ab = d3[i][j]
                if d4[i][j] == 1:
                    ar = int(ar*0.75)
                    ag = int(ag*0.75)
                    ab = int(ab*0.75) 
                if d4[i][j] == 2:
                    ar = int(ar*0.75)+63
                    ag = int(ag*0.75)+63
                    ab = int(ab*0.75)+63
                if d4[i][j] == 3:
                    ar = int(ar*0.875)
                    ag = int(ag*0.875)
                    ab = int(ab*0.875)
                d.putpixel((i,j),(ar,ag,ab,255))
        d.save(h20)
        print(f"saved as {h20}.")
        d.show()
    #something hard⬆️
    
    #done⬇️
    elif h1== "4":
        print()
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '|   ' * v5
            print(f'{v6}[{os.path.basename(v2)}]')
            v7 = '|   ' * (v5 + 1)
            for v8 in v4:
                print(f'{v7}{v8}')
    else:
        print("\n[参考文档]\n输入0返回\n输入数字继续")