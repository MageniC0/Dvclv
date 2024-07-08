print("[星光]1.6.0\n")
import os
import json
from PIL import Image
选项 = print
提示 = print
输入 = input
调用 = open
取整 = int
模式 = ''
while True:
    选项("\n[主页面]\n1. 资源包\n2. 地图册\n3. 图形\n4. 检查文件")
    模式 = input()
    if 模式 == "0":
        break
    elif 模式 == "1":
        提示("\n[资源包]")
        资源包_名 = f"chc/{输入('调用资源包_')}.json"
        if not os.path.exists("chc/"):
            os.makedirs("chc/")
            数据 = {"chc":[[0 for _ in range(12)]]*256,"chj":["dust"]*256}
            with 打开(资源包_名,'w',encoding="utf-8") as 资源包:
                json.dump(数据,资源包)
            print(f"创建{资源包_名}")
        with 打开(资源包_名, 'r', encoding="utf-8") as 资源包:
            数据 = json.load(资源包)
        图形库,译名库 = 数据["chc"],数据["chj"]
        while True:
            序列号 = 输入("序列号_")
            if 序列号 == "0":
                数据 = {"chc":图形库,"chj":译名库}
                with 打开(资源包_名,'w',encoding="utf-8") as 资源包:
                    json.dump(数据,资源包)
                break 
            else:
                方块_序列 = 取整(index)
                方块_标签 = 输入("标签_")
                方块_主色 = 输入("主色_")
                c1,c2,c3 = [取整(方块_主色[h:h+2], 16) for h in (0, 2, 4)]
                方块_副色 = 输入("副色_")
                c4,c5,c6 = [取整(方块_副色[h:h+2], 16) for h in (0, 2, 4)]
                图形库[方块_序列] = [    c1      ,    c2      ,    c3      ,
                                         c4      ,    c5      ,    c6      ,
                                     取整(c1*0.75),取整(c2*0.75),取整(c3*0.75),
                                     取整(c4*0.75),取整(c5*0.75),取整(c6*0.75)]
                译名库[方块_序列] = 方块_标签
                print(f"[{序列号}]写入{图形库[方块_序列]}")
    elif 模式 == "2":
        提示("\n[地图册]")
        资源包_名 = f"chc/{输入('调用资源包_')}.json"
        if not os.path.exists("chc_name"):
            print(f"未找到资源包")
            continue
        with open(chc_name,'r',encoding="utf-8") as chc_file:
            data = json.load(chc_file)
        chc = data["chc"]
        chj = data["chj"]
        map_name = "map/" + input("地图册:")
        di = os.path.dirname(map_name)
        if not os.path.exists(map_name):
            os.makedirs(map_name)
            with open(map_name,'x',encoding="utf-8") as map_file:
                json.dump({"tr":[[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)],"trb":[[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]},map_file)
            print(f"创建新的地图册{map_name}")
        with open(map_name,'r',encoding="utf-8") as map_file:
            data = json.load(map_file)
        tr = data["tr"]
        trb = data["trb"]
        vale_walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
        vale_index = 1
        vale_brush = 1
        chc0 = chc[vale_index]
        chj0 = chj[vale_index]
        while True:
            print("\n[设计地图]\n2.1_ 放置方块\n2.2_ 选中区域\n2.3_ 选区内填充但不替换\n2.4_ 选区内填充\n2.5_ 重置选区\n2.6_ 设置笔刷\n2.7_ 查看笔刷名录")
            模式 = input("2.")
            if 模式 == "0":
                with open(map_name,'w',encoding="utf-8") as map_file:
                    json.dump({"tr":tr,"trb":trb},trb_file)
                break
            elif mode == "1":
                print("[坐标]")
                x = int(input("_"))
                y = int(input("_"))
                z = int(input("_"))
                tr[z][y][x] = chc0
                trb[z][y][x] = vale_brush
                print(f"放置方块[{chj0}]于({x},{y},{z})")
            elif mode == "2":
                print("[起点坐标]")
                x1 = int(input("_"))
                y1 = int(input("_"))
                z1 = int(input("_"))
                print("[终点坐标]")
                x2 = int(input("_"))
                y2 = int(input("_"))
                z2 = int(input("_"))
                for x in range(x1, x2+1):
                    for y in range(y1, y2+1):
                        for z in range(z1, z2+1):
                            vale_walk[z][y][x] = vale_brush
                print(f"指向从({x1},{y1},{z1})到({x2},{y2},{z2})的方块")
            elif mode == "3":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0:
                                tr[z][y][x] = chc0
                                trb[z][y][x] = vale_brush
                vale_walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("填充并重置选区")
            elif mode == "4":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if vale_walk[z][y][x] != 0 and trb[z][y][x] == 0:
                                tr[z][y][x] = chc0
                                trb[z][y][x] = vale_brush
                vale_walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("填充并重置选区")
            elif mode == "5":
                vale_walk = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
                print("重置选区")
            elif mode == "6":
                vale_index = input("[设置笔刷]_")
                if vale_index != "0":
                    print("正在拆除")
                    vale_brush = 0
                else:
                    try:
                        r = int(r)
                        chc0 = chc[vale_index]
                        chj0 = chj[vale_index]
                        print(f"持有{chj0}")
                        vale_brush = 1
                    except ValueError:
                        print("输入小于256的整数以指定方块")
            elif mode == "7":
                print("[笔刷名录]")
                for k in range(256):
                    print(f"[{k}]{chj[k]}")
            else:
                print("\n[提示]\n输入数字继续\n输入0返回")
    elif mode == "3":
        print("\n[人工黎明]")
        map_name = "map/" + input("地图册:")
        img_name = f"{map_name}/map.png"
        tr_name = f"{map_name}/tr.json"
        trb_name = f"{map_name}/trb.json"
        di = os.path.dirname(map_name)
        if not os.path.exists(map_name):
            os.makedirs(map_name)
            print(f"未找到地图册")
            continue
        with open(tr_name,'r',encoding="utf-8") as file:
            tr = json.load(file)
        with open(trb_name,'r',encoding="utf-8") as file:
            trb = json.load(file)
        tr_near = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] != 0:
                        tr_near[z+1][y+1][x+1] = 1
        img_dawn = [[(0,0,0) for _ in range(193)] for _ in range(193)]
        img_draw = [[0 for _ in range(193)] for _ in range(193)]
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    if trb[z][y][x] == 1:
                        dim_dawn = [[(0,0,0) for _ in range(13)]for _ in range(13)]
                        dim_draw = [[0 for _ in range(13)]for _ in range(13)]
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
                                dim_dawn[2][0] = u1
                                dim_dawn[2][1] = u1
                                dim_dawn[3][2] = u1
                                dim_dawn[3][3] = u1
                                dim_dawn[3][4] = u1
                                dim_dawn[4][5] = u1
                                dim_dawn[4][6] = u1
                            if dim_near[1] == 0:
                                dim_draw[0][5] = 2
                                dim_draw[0][6] = 2
                                dim_draw[0][7] = 2
                                dim_draw[1][8] = 2
                                dim_draw[1][9] = 2
                                dim_draw[1][10] = 2
                            if dim_near[2] == 0:
                                dim_dawn[2][12] = u1
                                dim_dawn[2][11] = u1
                                dim_dawn[3][10] = u1
                                dim_dawn[3][9] = u1
                                dim_dawn[3][8] = u1
                                dim_dawn[4][7] = u1
                                dim_dawn[4][6] = u1
                            if dim_near[3] == 0:
                                dim_draw[0][7] = 2
                                dim_draw[0][6] = 2
                                dim_draw[0][5] = 2
                                dim_draw[1][4] = 2
                                dim_draw[1][3] = 2
                                dim_draw[1][2] = 2
                        if dim_near[5] == 0:
                            if dim_near[0] == 0:
                                dim_draw[10][0] = 1
                                dim_draw[10][1] = 1
                                dim_draw[11][2] = 1
                                dim_draw[11][3] = 1
                                dim_draw[11][4] = 1
                                dim_draw[12][5] = 1 
                            if dim_near[2] == 0:
                                dim_draw[10][12] = 1
                                dim_draw[10][11] = 1
                                dim_draw[11][10] = 1
                                dim_draw[11][9] = 1
                                dim_draw[11][8] = 1
                                dim_draw[12][7] = 1
                        if dim_near[0] == 0:
                            if dim_near[3] == 0:
                                for k in range(3,11):
                                    dim_draw[k][12] = 3
                            for i in range(3,11):
                                dim_dawn[i][0] = u2
                            for i in range(3,11):
                                dim_dawn[i][1] = u2
                            for i in range(4,12):
                                dim_dawn[i][2] = u2 
                            for i in range(4,12):
                                dim_dawn[i][3] = u2  
                            for i in range(4,12):
                                dim_dawn[i][4] = u2
                            for i in range(5,13):
                                dim_dawn[i][5] = u2
                        if dim_near[2] == 0:
                            if dim_near[1] == 0:
                                for k in range(3,11):
                                    dim_draw[k][12] = 3
                            for i in range(5,13):
                                dim_dawn[i][12] = u2
                            for i in range(5,13):
                                dim_dawn[i][11] = u2
                            for i in range(4,12):
                                dim_dawn[i][10] = u2 
                            for i in range(4,12):
                                dim_dawn[i][9] = u2  
                            for i in range(4,12):
                                dim_dawn[i][8] = u2
                            for i in range(3,11):
                                dim_dawn[i][7] = u2
                        if dim_near[0] == 0 and dim_near[2] == 0:
                            for k in range(5,13):
                                dim_dawn[k][6] = u3
                        dim_x = 6 * (15 - x + y)
                        dim_y = 2 * (60 + x + y - 4 * z)
                        for i in range(13):
                            for j in range(2,11):
                                img_draw[dim_x+i][dim_y+j] = 0 
                        for i in range(2,11):
                            img_draw[dim_x+i][dim_y+1] = 0
                        for i in range(2,11):
                            img_draw[dim_x+i][dim_y+11] = 0
                        img_draw[dim_x+5][dim_y] = 0
                        img_draw[dim_x+6][dim_y] = 0
                        img_draw[dim_x+7][dim_y] = 0
                        img_draw[dim_x+5][dim_y+12] = 0
                        img_draw[dim_x+6][dim_y+12] = 0
                        img_draw[dim_x+7][dim_y+12] = 0
                        for i in range(13):
                            for j in range(13):
                                if dim_dawn[i][j] != (0,0,0):
                                    img_draw[dim_x+j][dim_y+i] = dim_draw[i][j]
        img = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for i in range(193):
            for j in range(193):
                pix_r,pix_g,pix_b = img_dawn[i][j]
                if img_draw[i][j] == 1:
                    pix_r = int(pix_r*0.75)
                    pix_g = int(pix_g*0.75)
                    pix_b = int(pix_b*0.75) 
                if img_draw[i][j] == 2:
                    pix_r = int(pix_r*0.75)+63
                    pix_g = int(pix_g*0.75)+63
                    pix_b = int(pix_b*0.75)+63
                if img_draw[i][j] == 3:
                    pix_r = int(pix_r*0.875)
                    pix_g = int(pix_g*0.875)
                    pix_b = int(pix_b*0.875)
                img.putpixel((i,j),(pix_r,pix_g,pix_b,255))
        img.save(img_name)
        print(f"saved as {img_name}.")
        img.show()
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
    else:
        print("\n[提示]\n输入0返回\n输入数字继续")