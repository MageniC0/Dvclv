print("[星光]1.6.0\n")
import os
import json
from PIL import Image

while True:

    #输入0以返回
    #输入数字以继续
    print("\n[主页面]\n1. 设计资源册\n2. 设计地图册\n3. 生成图形\n4. 检查文件")
    mode = input("_")

    #0. 退出
    if mode == "0":
        break

    #1. 设计资源册，调用res/chc和res/chj生成res/chc和res/chj
    elif mode == "1":

        print("\n[设计资源册]")

        #1.1 在控制台输入资源册的名字
        res_name = "res/" + input("资源册的名字:")
        chc_name = f"{res_name}/chc.json"
        chj_name = f"{res_name}/chj.json"

        #1.2 若资源册不存在则新建
        di = os.path.dirname(res_name)
        if not os.path.exists(res_name):
            os.makedirs(res_name)
            chc = [[0,0,0,0,0,0,0,0,0,0,0,0]] * 256
            chj = ["cube"] * 256
            with open(chc_name,'w',encoding="utf-8") as file:
                file.write(json.dumps(chc))
            with open(chj_name, 'w',encoding="utf-8") as file:
                file.write(json.dumps(chj))
            print(f"新的{res_name}")

        #1.3 加载图形库
        with open(chc_name,'r',encoding="utf-8") as file:
            chc = json.loads(file.read())

        #1.4 加载译名库
        with open(chj_name,'r',encoding="utf-8") as file:
            chj = json.loads(file.read())

        #1.5 写入方块
        while True:
            index = input("[转到方块]_")
            if index == "0":
                break 
            else:
                #方块的编码
                cube_index = int(index)
                #方块的命名
                cube_name = input("方块名:")
                #主要分布在图形中的颜色
                cube_facecolor = input("面色:")
                #作为图形边缘的颜色
                cube_sidecolor = input("线色:")

                #格式化RGB
                c1,c2,c3 = [int(cube_facecolor[h:h+2], 16) for h in (0, 2, 4)]
                c4,c5,c6 = [int(cube_sidecolor[h:h+2], 16) for h in (0, 2, 4)]

                #生成改动项
                chc[cube_index] = [c1,c2,c3,c4,c5,c6,int(c1*0.75),int(c2*0.75),int(c3*0.75),int(c4*0.75),int(c5*0.75),int(c6*0.75)]
                print(f"[{index}]写入{chc[cube_index]}")
                chj[cube_index] = cube_name

                #1.6 保存图形库和译名库
                with open(chc_name, 'w', encoding="utf-8") as file:
                    json.dump(chc, file, ensure_ascii=False)
                with open(chj_name,'w',encoding="utf-8") as file:
                    json.dump(chj, file, ensure_ascii=False)

    #2. 设计地图册，调用res/chc和res/chj，生成map/tr和map/trb
    elif mode == "2":

        #2.1 调用资源文件
        res_name = "res/" + input("资源册:")
        chj_name = f"{res_name}/chj.json"
        chc_name = f"{res_name}/chc.json"

        #2.2 若找不到资源册，报错并返回到主页面
        di = os.path.dirname(res_name)
        if not os.path.exists(res_name):
            os.makedirs(res_name)
            print(f"未找到资源册")
            continue

       #2.3 写入数据
        with open(chj_name,'r',encoding = "utf-8") as file:
            chj = json.loads(file.read())
        with open(chc_name,'r',encoding = "utf-8") as file:
            chc = json.loads(file.read())

        #2.4 打开地图册的两个数据文件，若没有则新创建
        map = "map/" + input("地图册:")
        tr = f"{map}/tr.json"
        trb = f"{map}/trb.json"
        di = os.path.dirname(map)
        if not os.path.exists(map):
            os.makedirs(map)
            tr = [[[[0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(tr, 'w',encoding="utf-8") as file:
                file.write(json.dumps(tr))
            trb = [[[0 for _ in range(16)]for _ in range(16)]for _ in range(16)]
            with open(trb, 'w',encoding="utf-8") as file:
                file.write(json.dumps(trb))
            print(f"创建新的地图册{map}")

        with open(tr,'r',encoding="utf-8") as file:
            tr = json.loads(file.read())
        with open(trb,'r',encoding="utf-8") as file:
            trb = json.loads(file.read())

        wlk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        cube_index = 1
        ulk = 1
        chc0 = chc[cube_index]
        chj0 = chj[cube_index]
        mode = ''  
        while True:
            print("\n[设计地图]\n2.1_ 放置方块\n2.2_ 选中区域\n2.3_ 处理选区\n2.4_ 设置笔刷\n2.5_ 查看目录")
            mode = input("2.")
            if mode == "0":
                break
            elif mode == "1":
                print("[选中方块]")
                x = int(input("_"))
                y = int(input("_"))
                z = int(input("_"))
                tr[z][y][x] = chc0
                trb[z][y][x] = ulk
                print(f"放置方块于({x},{y},{z})")
                with open(tr, "w") as file:
                    json.dump(tr, file)
                with open(trb, "w") as file:
                    json.dump(trb, file)
            elif mode == "2":
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
                            wlk[z][y][x] = ulk
                print(f"指向从({x1},{y1},{z1})到({x2},{y2},{z2})的方块")
            elif mode == "3":
                print("[选区]\n2.4.1_ 填充但不替换\n2.4.2_ 填充且替换\n2.4.3_ 释放选区")
                mode = input("2.4.")
                if mode == "0":
                    break
                elif mode == "1":
                    if trb[z][y][x] != 0:
                        for z in range(16):
                            for y in range(16):
                                for x in range(16):
                                    if wlk[z][y][x]:
                                        tr[z][y][x] = chc0
                                        trb[z][y][x] = ulk
                                        with open(tr, "w") as file:
                                            json.dump(tr, file)
                                        with open(trb, "w") as file:
                                            json.dump(trb, file)
                elif mode == "2":
                    for z in range(16):
                        for y in range(16):
                            for x in range(16):
                                if wlk[z][y][x]:
                                    tr[z][y][x] = chc0
                                    trb[z][y][x] = ulk
                                    with open(tr, "w") as file:
                                        json.dump(tr,file)
                                    with open(trb, "w") as file:
                                        json.dump(trb,file)
                elif mode == "3":
                    wlk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
            elif mode == "4":
                cube_index = int(input("[设置笔刷]_"))
                if cube_index != 0:
                    chc0 = chc[cube_index]
                    chj0 = chj[cube_index]
                    print(f"持有{chj0}")
                    ulk = 1
                else:
                    print("正在拆除")
                    ulk = 0
            elif mode == "5":
                print("[方块名录]")
                for k in range(256):
                    print(f"[{k}]{chj[k]}")

    #3. 生成地形，调用map/tr和map/trb
    elif mode == "3":
        #3.1 输入信息
        print("\n[人工黎明]")
        map_name = "map/" + input("地图册:")
        h20 = f"{map_name}/map.png"
        tr_name = f"{map_name}/tr.json"
        trb_name = f"{map_name}/trb.json"

        #3.2 若文件夹不存在则报错并返回至主页面
        di = os.path.dirname(map_name)
        if not os.path.exists(map_name):
            os.makedirs(map_name)
            print(f"未找到地图册")
            continue

        #3.3 加载数据
        with open(tr_name,'r',encoding="utf-8") as file:
            tr = json.loads(file.read())
        with open(trb_name,'r',encoding="utf-8") as file:
            trb = json.loads(file.read())


        #3.4 处理数据生成图片

        #用于遮挡判定的邻接序列（将来也用于区块集成的数据传送）
        tr_near = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] != 0:
                        tr_near[z+1][y+1][x+1] = 1

        #用于存储画布填色信息的列表
        img_draw = [[(0,0,0) for _ in range(193)] for _ in range(193)]
        #用于存储渲染信息的列表
        img_dawn = [[0 for _ in range(193)] for _ in range(193)]

        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] == 1:
                        d5 = [[0 for _ in range(13)]for _ in range(13)]
                        ulk = [[(0,0,0) for _ in range(13)]for _ in range(13)]
                        o = tr[z][y][x]
                        h21 = [tr_near[z+1][y+1][x+2],
                               tr_near[z+1][y+1][ x ],
                               tr_near[z+1][y+2][x+1],
                               tr_near[z+1][ y ][x+1],
                               tr_near[z+2][y+1][x+1],
                               tr_near[ z ][y+1][x+1]]
                        u0,u1,u2,u3 = ((o[0],o[1],o[2]),
                                       (o[3],o[4],o[5]),
                                       (o[6],o[7],o[8]),
                                       (o[9],o[10],o[11]))
                        if h21[4] == 0:
                            for j in range(2,11):
                                ulk[1][j] = u0
                            for j in range(2,11):
                                ulk[2][j] = u0
                            ulk[0][5] = u0
                            ulk[0][6] = u0
                            ulk[0][7] = u0
                            ulk[3][5] = u0
                            ulk[3][6] = u0
                            ulk[3][7] = u0
                            if h21[0] == 0:
                                ulk[2][11] = u1
                                ulk[2][12] = u1
                                ulk[3][8] = u1
                                ulk[3][9] = u1
                                ulk[3][10] = u1
                                ulk[4][6] = u1
                                ulk[4][7] = u1
                            if h21[1] == 0:
                                d5[0][5] = 2
                                d5[0][6] = 2
                                d5[0][7] = 2
                                d5[1][2] = 2
                                d5[1][3] = 2
                                d5[1][4] = 2
                            if h21[2] == 0:
                                ulk[2][1] = u1
                                ulk[2][0] = u1
                                ulk[3][4] = u1
                                ulk[3][3] = u1
                                ulk[3][2] = u1
                                ulk[4][6] = u1
                                ulk[4][5] = u1
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
                                ulk[i][12] = u2
                            for i in range(3,11):
                                ulk[i][11] = u2
                            for i in range(4,12):
                                ulk[i][10] = u2 
                            for i in range(4,12):
                                ulk[i][9] = u2  
                            for i in range(4,12):
                                ulk[i][8] = u2
                            for i in range(5,13):
                                ulk[i][7] = u2
                            if h21[3] == 0:
                                if h21[1] == 0:
                                    for k in range(3,11):
                                        d5[k][0] = 3
                        if h21[2] == 0:
                            for i in range(5,13):
                                ulk[i][5] = u2
                            for i in range(4,12):
                                ulk[i][4] = u2
                            for i in range(4,12):
                                ulk[i][3] = u2 
                            for i in range(4,12):
                                ulk[i][2] = u2  
                            for i in range(3,11):
                                ulk[i][1] = u2
                            for i in range(3,11):
                                ulk[i][0] = u2
                            if h21[1] == 0:
                                for i in range(5,11):
                                    for j in range(8):
                                        ulk[i][j] = u2
                        if h21[0] == 0 and h21[2] == 0:
                            for k in range(5,13):
                                ulk[k][6] = u3
                                
                                
                                #图形生成
                        m = 6 * (15 + x - y)
                        n = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                img_dawn[m+i][n+j] = 0 
                        for i in range(2,11):
                            img_dawn[m+i][n+1] = 0
                        for i in range(2,11):
                            img_dawn[m+i][n+11] = 0
                        img_dawn[m+5][n] = 0
                        img_dawn[m+6][n] = 0
                        img_dawn[m+7][n] = 0
                        img_dawn[m+5][n+12] = 0
                        img_dawn[m+6][n+12] = 0
                        img_dawn[m+7][n+12] = 0
                        
                        for i in range(13):
                            for j in range(13):
                                if ulk[i][j] != (0,0,0):
                                    img_draw[m+j][n+i] = ulk[i][j]
                                    img_dawn[m+j][n+i] = d5[i][j]
        d = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                ar,ag,ab = img_draw[i][j]
                if img_dawn[i][j] == 1:
                    ar = int(ar*0.75)
                    ag = int(ag*0.75)
                    ab = int(ab*0.75) 
                if img_dawn[i][j] == 2:
                    ar = int(ar*0.75)+63
                    ag = int(ag*0.75)+63
                    ab = int(ab*0.75)+63
                if img_dawn[i][j] == 3:
                    ar = int(ar*0.875)
                    ag = int(ag*0.875)
                    ab = int(ab*0.875)
                d.putpixel((i,j),(ar,ag,ab,255))
        d.save(h20)
        print(f"saved as {h20}.")
        d.show()

    #4. 检查文件目录
    elif mode== "4":

        print()
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '|   ' * v5
            print(f'{v6}[{os.path.basename(v2)}]')
            v7 = '|   ' * (v5 + 1)
            for v8 in v4:
                print(f'{v7}{v8}')

    #对异常输入的处理
    else:
        print("\n[帮助]\n输入0返回\n输入数字继续")