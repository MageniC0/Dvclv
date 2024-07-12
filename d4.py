import os,pickle
from PIL import Image,ImageDraw
def f(lin,ch_,tr_):
    op = ''
    if len(lin)==1:
        lin="4."+input("[检查]查看本地存储\n4.1:查看文件目录\n4.2:查看资源包\n4.3:查看地图册\n[检查]选择模块\033[94m4._")
    if lin == "4.1":
        print("\n[检查]传送数据...\n")
        v1 = os.path.abspath('.')
        for v2, v3, v4 in os.walk(v1):
            v5 = v2.replace(v1,'').count(os.sep)
            v6 = '| ' * v5
            op += f'{v6}[{os.path.basename(v2)}]\n'
            v7 = '| ' * (v5 + 1)
            for v8 in v4:op += f'{v7}{v8}\n'
        print("\033[90m"+op)
    if lin == "4.2":
        print("\n[检查]传送数据...\n")
        with open(ch_+'a','rb') as file:cha = pickle.load(file)
        with open(ch_+'b','rb') as file:chb = pickle.load(file)
        for k in range(256):op += f"[{k}]{chb[k]}_{cha[k]}\n"
        print("\033[90m"+op)
    if lin == "4.3":
        with open(tr_+'a','rb') as file:tra = pickle.load(file)
        op = "[terrain list]"
        li = Image.open("lab.png")
        lid = ImageDraw.Draw(li)
        for z in range(16):
            for y in range(16):
                for x in range(16):
                    cd = (tra[x][y][z][0],tra[x][y][z][1],tra[x][y][z][2])
                    if cd != (0,0,0):
                        lid.rectangle([16*x+2,16*y+4*z+2,16*x+18,16*y+4*z+18], fill = cd)
        li.show()
    op = ''