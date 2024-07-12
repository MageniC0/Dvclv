import pickle
def f(lin,ch_):
    try:
        with open(ch_+'a','rb') as file:cha = pickle.load(file)
        with open(ch_+'b','rb') as file:chb = pickle.load(file)
    except FileNotFoundError:
        cha = [[0 for _ in range(12)] for _ in range(256)]
        chb = ["余烬" for _ in range(256)]
        with open(ch_+'a','wb') as file:pickle.dump(cha,file)
        with open(ch_+'a','wb') as file:pickle.dump(chb,file)
        print(f"[材质]创建[{ch_}]")
    while True:
        ind = int(input("\n[材质]选择方块\033[94m_"))
        if ind == 0:
            print(f"\n[材质]返回.")
            break
        else:
            c_ = str(input("[材质]方块名\033[94m_"))
            ac = str(input("[材质]方块主色\033[94m_"))
            bc = str(input("[材质]方块副色\033[94m_"))
            c1,c2,c3 = [int(ac[h:h+2],16) for h in (0,2,4)]
            c4,c5,c6 = [int(bc[h:h+2],16) for h in (0,2,4)]
            cha[ind] = [c1,c2,c3,c4,c5,c6,int(c1*0.8),int(c2*0.8),int(c3*0.8),int(c4*0.8),int(c5*0.8),int(c6*0.8)]
            chb[ind] = c_
            with open(ch_+'a','wb') as file:pickle.dump(cha,file)
            with open(ch_+'b','wb') as file:pickle.dump(chb,file)
            print(f"[材质]在索引\033[94m[{ind}]\033[95m构造方块\033[94m{c_}")