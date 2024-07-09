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
        burst = 1
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
                trb[z][y][x] = burst
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
                            walk[z][y][x] = burst
                提示(f"from({x1},{y1},{z1})to({x2},{y2},{z2})select")
            elif mode == "3":
                for z in range(16):
                    for y in range(16):
                        for x in range(16):
                            if walk[z][y][x] != 0:
                                hc = tra[z][y][x] = hc
                                burst = trb[z][y][x]
                walk = [[0]*16]*16
                提示("rewalk")
            elif mode == "4":
                for z in 遍历(16):
                    for y in 遍历(16):
                        for x in 遍历(16):
                            if walk[z][y][x] != 0 and trb[z][y][x] == 0:
                                tra[z][y][x] = hc
                                trb[z][y][x] = burst
                walk = [[[0 for _ in 遍历(16)] for _ in 遍历(16)] for _ in 遍历(16)]
                提示("填充并重置选区")
            elif mode == "5":
                walk = [[[0 for _ in 遍历(16)] for _ in 遍历(16)] for _ in 遍历(16)]
                提示("重置选区")
            elif mode == "6":
                参数 = 选项("设置笔刷_")
                if 参数 != "0":
                    print("正在拆除")
                    burst = 0
                else:
                    try:
                        r = 取整(r)
                        hc = chc[参数]
                        hb = chj[参数]
                        提示(f"持有{hb}")
                        burst = 1
                    except ValueError:
                        提示("输入小于256的整数以指定方块")
            else:
                提示("\n[提示]\n输入数字继续\n输入0返回")
    elif mode == "3":
        提示("\n[人工黎明]")
        #1. 加载数据
        trr_name = "trr/" + 选项("地图册_") + ".json"
        try:
            with 调用(trr_name, 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            提示(f"找不到{trr_name}")
            continue
        地质库,地形库 = data["tr"],data["trb"]
        图 = "flu/" + 选项("示意图_") + ".png"
        提示("传送数据...")
        #2. 生成邻接序列
        邻接库 = [[[0]*18]*18]*18
        for z in 遍历(16):
            for y in 遍历(16):
                for x in 遍历(16):
                    if 地形库[z][y][x] != 0:
                        邻接库[z+1][y+1][x+1] = 1
        #3. 生成总画布
        取色库 = [[(0,0,0)]*193]*193
        渲染库 = [[0]*193]*193
        #4. 生成像素分布序列
        for z in 遍历(16):
            for y in 遍历(16):
                for x in 遍历(16):
                    #5. 对于每一个不透明的方块
                    if 地形库[z][y][x] == 1:
                        #6. 创建画布
                        取色 = [[(0,0,0)]*13]*13
                        渲染 = [[0]*13]*13
                        #7. 加载数据
                        tra = 地质库[z][y][x]
                        邻接 = [邻接库[z+1][y+1][x+2],
                                邻接库[z+1][y+1][ x ],
                                邻接库[z+1][y+2][x+1],
                                邻接库[z+1][ y ][x+1],
                                邻接库[z+2][y+1][x+1],
                                邻接库[ z ][y+1][x+1]]
                        a,b,暗主色,暗副色 = ((tra[0], tra[1], tra[2]),
                                                   (tra[3], tra[4], tra[5]),
                                                   (tra[6], tra[7], tra[8]),
                                                   (tra[9],tra[10],tra[11]))
                        print(邻接)
                        #8. 填色
                        if 邻接[4] == 0:
                            for 纵 in 遍历(2,11):
                                取色[1][纵] = a
                            for 纵 in 遍历(2,11):
                                取色[2][纵] = a
                            取色[0][5] = a
                            取色[0][6] = a
                            取色[0][7] = a
                            取色[3][5] = a
                            取色[3][6] = a
                            取色[3][7] = a
                            if 邻接[0] == 0:
                                取色[2][0] = b
                                取色[2][1] = b
                                取色[3][2] = b
                                取色[3][3] = b
                                取色[3][4] = b
                                取色[4][5] = b
                                取色[4][6] = b
                            if 邻接[1] == 0:
                                渲染[0][5] = 2
                                渲染[0][6] = 2
                                渲染[0][7] = 2
                                渲染[1][8] = 2
                                渲染[1][9] = 2
                                渲染[1][10] = 2
                            if 邻接[2] == 0:
                                取色[2][12] = b
                                取色[2][11] = b
                                取色[3][10] = b
                                取色[3][9] = b
                                取色[3][8] = b
                                取色[4][7] = b
                                取色[4][6] = b
                            if 邻接[3] == 0:
                                渲染[0][7] = 2
                                渲染[0][6] = 2
                                渲染[0][5] = 2
                                渲染[1][4] = 2
                                渲染[1][3] = 2
                                渲染[1][2] = 2
                        if 邻接[5] == 0:
                            if 邻接[0] == 0:
                                渲染[10][0] = 1
                                渲染[10][1] = 1
                                渲染[11][2] = 1
                                渲染[11][3] = 1
                                渲染[11][4] = 1
                                渲染[12][5] = 1 
                            if 邻接[2] == 0:
                                渲染[10][12] = 1
                                渲染[10][11] = 1
                                渲染[11][10] = 1
                                渲染[11][9] = 1
                                渲染[11][8] = 1
                                渲染[12][7] = 1
                        print(取色)
                        if 邻接[0] == 0:
                            if 邻接[3] == 0:
                                for 粒子 in 遍历(3,11):
                                    渲染[粒子][12] = 3
                            for 横 in 遍历(3,11):
                                取色[横][0] = 暗主色
                            for 横 in 遍历(3,11):
                                取色[横][1] = 暗主色
                            for 横 in 遍历(4,12):
                                取色[横][2] = 暗主色 
                            for 横 in 遍历(4,12):
                                取色[横][3] = 暗主色  
                            for 横 in 遍历(4,12):
                                取色[横][4] = 暗主色
                            for 横 in 遍历(5,13):
                                取色[横][5] = 暗主色
                        if 邻接[2] == 0:
                            if 邻接[1] == 0:
                                for 粒子 in 遍历(3,11):
                                    渲染[粒子][12] = 3
                            for 横 in 遍历(5,13):
                                取色[横][12] = 暗主色
                            for 横 in 遍历(5,13):
                                取色[横][11] = 暗主色
                            for 横 in 遍历(4,12):
                                取色[横][10] = 暗主色 
                            for 横 in 遍历(4,12):
                                取色[横][9] = 暗主色  
                            for 横 in 遍历(4,12):
                                取色[横][8] = 暗主色
                            for 横 in 遍历(3,11):
                                取色[横][7] = 暗主色
                        if 邻接[0] == 0 and 邻接[2] == 0:
                            for 粒子 in 遍历(5,13):
                                取色[粒子][6] = 暗副色
                        print(渲染)
                        #9. 从空间坐标到平面坐标
                        X = 6 * (15 - x + y)
                        Y = 2 * (60 + x + y - 4 * z)
                        #10. 渲染区预留
                        for 横 in 遍历(13):
                            for 纵 in 遍历(2,11):
                                渲染库[X+横][Y+纵] = 0 
                        for 横 in 遍历(2,11):
                            渲染库[X+横][Y+1] = 0
                        for 横 in 遍历(2,11):
                            渲染库[X+横][Y+11] = 0
                        渲染库[X+5][Y] = 0
                        渲染库[X+6][Y] = 0
                        渲染库[X+7][Y] = 0
                        渲染库[X+5][Y+12] = 0
                        渲染库[X+6][Y+12] = 0
                        渲染库[X+7][Y+12] = 0
                        #11. 数据传送
                        for 横 in 遍历(13):
                            for 纵 in 遍历(13):
                                if 取色[横][纵] != (0,0,0):
                                    取色库[X+纵][Y+横] = 取色[横][纵]
        #12. 生成图形
        画布 = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
        for 横 in 遍历(193):
            for 纵 in 遍历(193):
                R,G,B = 取色库[横][纵]
                #13. 渲染
                if 渲染库[横][纵] == 1:
                    R = int(R*0.75)
                    G = int(G*0.75)
                    B = int(B*0.75) 
                if 渲染库[横][纵] == 2:
                    R = int(R*0.75)+63
                    G = int(G*0.75)+63
                    B = int(B*0.75)+63
                if 渲染库[横][纵] == 3:
                    R = int(R*0.875)
                    G = int(G*0.875)
                    B = int(B*0.875)
                画布.putpixel((横,纵),(R,G,B,255))
        #14. 存储图形
        画布.save(图)
        提示(f"保存为{图}")
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
        for 粒子 in 遍历(256):
            输出 += f"[{粒子}]{chj[粒子]}_{chc[粒子]}\n"
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