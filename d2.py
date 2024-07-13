import pickle
def f(lin,ch_,tr_):
    try:
        with open(ch_+'a','rb') as file:cha = pickle.load(file)
        with open(ch_+'b','rb') as file:chb = pickle.load(file)
    except Exception:print("[地质]未找到资源包")
    try:
        with open(tr_+'a','rb') as file:tra = pickle.load(file)
        with open(tr_+'b','rb') as file:trb = pickle.load(file)
    except Exception:print(f"[地质]创建[{tr_}]")
        tra = [[[[0,0,0,0,0,0,0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
        trb = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
    with open(tr_+'a','wb') as file:pickle.dump(tra,file)
    with open(tr_+'b','wb') as file:pickle.dump(trb,file)
    bu = 1
    ha = cha[1]
    hb = chb[1]
    if len(lin)==1:
        lin = "2."+input("[地质]生成地图册\n2.1:放置单个方块\n2.2:放置方块组\n2.3:设置笔刷\n[地质]选择模块\033[94m2._")
    while True:
        if lin == "2.0":
            print(f"[地质]返回.")
            break
        elif lin == "2.1":
            print("[地质]输入坐标")
            x = int(input("x\033[94m_"))
            y = int(input("y\033[94m_"))
            z = int(input("z\033[94m_"))
            tra[x][y][z] = ha
            trb[x][y][z] = bu
            with open(tr_+'a',"wb") as file:pickle.dump(tra,file)
            with open(tr_+'b',"wb") as file:pickle.dump(trb,file)
            print(f"[地质]在(\033[94m{x}\033[95m,\033[94m{y}\033[95m,\033[94m{z}\033[95m)放置方块\033[94m{hb}")
            lin = "2."+input("\n[地质]2.\033[94m_")
        elif lin == "2.2":
            print("[地质]选择起点")
            x1 = int(input("x\033[94m_"))
            y1 = int(input("y\033[94m_"))
            z1 = int(input("z\033[94m_"))
            print("[地质]选择终点")
            x2 = int(input("x\033[94m_"))
            y2 = int(input("y\033[94m_"))
            z2 = int(input("z\033[94m_"))
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    for z in range(z1,z2+1):
                        tra[x][y][z] = ha
                        trb[x][y][z] = bu
            print(f"[地质]填充\033[94m{hb}从\033[95m(\033[94m{x1}\033[95m,\033[94m{y1}\033[95m,\033[94m{z1}\033[94m)到(\033[94m{x2}\033[95m,\033[94m{y2}\033[95m,\033[94m{z2}\033[95m)")
            with open(tr_+'a',"wb") as file:pickle.dump(tra,file)
            with open(tr_+'b',"wb") as file:pickle.dump(trb,file)
            lin = "2."+input("\n[地质]2.\033[94m_")
        elif lin == "2.3":
            lue = input("[地质]选择方块\n\033[94m_")
            try:
                lue = int(lue)
                ha = cha[lue]
                hb = chb[lue]
                if lue == 0:
                    print("[地质]正在拆除")
                    bu = 0
                else:
                    print(f"[地质]持有方块\033[94m{hc}")
                    bu = 1
            except Exception:print("[地质]输入1～255的数字以选择方块或输入0以选择空方块")
            lin = "2."+input("\n[地质]2.\033[94m_")