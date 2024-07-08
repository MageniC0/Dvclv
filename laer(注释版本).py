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
        dim_dawn = 1
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
                trb[z][y][x] = dim_dawn
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
                            wlk[z][y][x] = dim_dawn
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
                                        trb[z][y][x] = dim_dawn
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
                                    trb[z][y][x] = dim_dawn
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
                    dim_dawn = 1
                else:
                    print("正在拆除")
                    dim_dawn = 0
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

        #核心环节
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    #对于区块内的每一个方块
                    if trb[z][y][x] == 1:
                        dim_draw = [[0 for _ in range(13)]for _ in range(13)]
                        dim_dawn = [[(0,0,0) for _ in range(13)]for _ in range(13)]
                        dim_chc = tr[z][y][x]
                        dim_near = [tr_near[z+1][y+1][x+2],
                               tr_near[z+1][y+1][ x ],
                               tr_near[z+1][y+2][x+1],
                               tr_near[z+1][ y ][x+1],
                               tr_near[z+2][y+1][x+1],
                               tr_near[ z ][y+1][x+1]]
                        u0,u1,u2,u3 = ((dim_chc[0], dim_chc[1], dim_chc[2]),
                                       (dim_chc[3], dim_chc[4], dim_chc[5]),
                                       (dim_chc[6], dim_chc[7], dim_chc[8]),
                                       (dim_chc[9],dim_chc[10],dim_chc[11]))
                        if dim_near[4] == 0:
                            for j in range(2,11):
                                dim_dawn[1][j] = u0
                            for j in range(2,11):
                                dim_dawn[2][j] = u0
                            dim_dawn[0][5] = u0
                            dim_dawn[0][6] = u0
                            dim_dawn[0][7] = u0
                            dim_dawn[3][5] = u0
                            dim_dawn[3][6] = u0
                            dim_dawn[3][7] = u0
                            if dim_near[0] == 0:
                                dim_dawn[2][11] = u1
                                dim_dawn[2][12] = u1
                                dim_dawn[3][8] = u1
                                dim_dawn[3][9] = u1
                                dim_dawn[3][10] = u1
                                dim_dawn[4][6] = u1
                                dim_dawn[4][7] = u1
                            if dim_near[1] == 0:
                                dim_draw[0][5] = 2
                                dim_draw[0][6] = 2
                                dim_draw[0][7] = 2
                                dim_draw[1][2] = 2
                                dim_draw[1][3] = 2
                                dim_draw[1][4] = 2
                            if dim_near[2] == 0:
                                dim_dawn[2][1] = u1
                                dim_dawn[2][0] = u1
                                dim_dawn[3][4] = u1
                                dim_dawn[3][3] = u1
                                dim_dawn[3][2] = u1
                                dim_dawn[4][6] = u1
                                dim_dawn[4][5] = u1
                            if dim_near[3] == 0:
                                dim_draw[0][7] = 2
                                dim_draw[0][6] = 2
                                dim_draw[0][5] = 2
                                dim_draw[1][10] = 2
                                dim_draw[1][9] = 2
                                dim_draw[1][8] = 2
                        if dim_near[5] == 0:
                            if dim_near[0] == 0:
                                dim_draw[10][12] = 1
                                dim_draw[10][11] = 1
                                dim_draw[11][10] = 1
                                dim_draw[11][9] = 1
                                dim_draw[11][8] = 1
                                dim_draw[12][5] = 1 
                            if dim_near[2] == 0:
                                dim_draw[10][1] = 1
                                dim_draw[10][0] = 1
                                dim_draw[11][4] = 1
                                dim_draw[11][3] = 1
                                dim_draw[11][2] = 1
                                dim_draw[12][5] = 1
                        if dim_near[0] == 0:
                            if dim_near[3] == 0:
                                for k in range(3,11):
                                    dim_draw[k][12] = 3
                            for i in range(3,11):
                                dim_dawn[i][12] = u2
                            for i in range(3,11):
                                dim_dawn[i][11] = u2
                            for i in range(4,12):
                                dim_dawn[i][10] = u2 
                            for i in range(4,12):
                                dim_dawn[i][9] = u2  
                            for i in range(4,12):
                                dim_dawn[i][8] = u2
                            for i in range(5,13):
                                dim_dawn[i][7] = u2
                            if dim_near[3] == 0:
                                if dim_near[1] == 0:
                                    for k in range(3,11):
                                        dim_draw[k][0] = 3
                        if dim_near[2] == 0:
                            for i in range(5,13):
                                dim_dawn[i][5] = u2
                            for i in range(4,12):
                                dim_dawn[i][4] = u2
                            for i in range(4,12):
                                dim_dawn[i][3] = u2 
                            for i in range(4,12):
                                dim_dawn[i][2] = u2  
                            for i in range(3,11):
                                dim_dawn[i][1] = u2
                            for i in range(3,11):
                                dim_dawn[i][0] = u2
                            if dim_near[1] == 0:
                                for i in range(5,11):
                                    for j in range(8):
                                        dim_dawn[i][j] = u2
                        if dim_near[0] == 0 and dim_near[2] == 0:
                            for k in range(5,13):
                                dim_dawn[k][6] = u3
                                
                                
                                #图形生成
                        dim_x = 6 * (15 + x - y)
                        dim_y = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                img_dawn[dim_x+i][dim_y+j] = 0 
                        for i in range(2,11):
                            img_dawn[dim_x+i][dim_y+1] = 0
                        for i in range(2,11):
                            img_dawn[dim_x+i][dim_y+11] = 0
                        img_dawn[dim_x+5][dim_y] = 0
                        img_dawn[dim_x+6][dim_y] = 0
                        img_dawn[dim_x+7][dim_y] = 0
                        img_dawn[dim_x+5][dim_y+12] = 0
                        img_dawn[dim_x+6][dim_y+12] = 0
                        img_dawn[dim_x+7][dim_y+12] = 0
                        
                        for i in range(13):
                            for j in range(13):
                                if dim_dawn[i][j] != (0,0,0):
                                    img_draw[dim_x+j][dim_y+i] = dim_dawn[i][j]
                                    img_dawn[dim_x+j][dim_y+i] = dim_draw[i][j]
        img = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                pix_r,pix_g,pix_b = img_draw[i][j]
                if img_dawn[i][j] == 1:
                    pix_r = int(pix_r*0.75)
                    pix_g = int(pix_g*0.75)
                    pix_b = int(pix_b*0.75) 
                if img_dawn[i][j] == 2:
                    pix_r = int(pix_r*0.75)+63
                    pix_g = int(pix_g*0.75)+63
                    pix_b = int(pix_b*0.75)+63
                if img_dawn[i][j] == 3:
                    pix_r = int(pix_r*0.875)
                    pix_g = int(pix_g*0.875)
                    pix_b = int(pix_b*0.875)
                img.putpixel((i,j),(pix_r,pix_g,pix_b,255))
        img.save(h20)
        print(f"saved as {h20}.")
        img.show()

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