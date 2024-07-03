from PIL import Image
import json

ch_n = input("res name:")+".png"
tr_n = input("trr name:")+".json"  #0/1
fi_n = input("save as:")+".png"

with open(ch_name) as f1:
    ch = json.load(f1)
with open(tr_name) as f2:
    tr = json.load(f2)

def pos(x, y, z):
    m = 15+ x - y
    n = 60 + x + y - 4 * z
    return m * 6, n * 2

A = Image.new("RGBA", (193, 193),(255,255,255,0))
B = [[0 for _ in range(193)] for _ in range(193)]
tr_n = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
tr_r = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
    
for z in range(16):
    for y in range(16):
        for x in range(16):
            if tr[z][y][x] != 0:
                tr_n[z+1][y+1][x+1] = 1

for z in range(1,17):
    for y in range(1,17):
        for x in range(1,17):
            tr_r[z-1][y-1][x-1] = [tr_n[z][y][x + 1],tr_n[z][y][x - 1],tr_n[z][y + 1][x],tr_n[z][y - 1][x],tr_n[z + 1][y][x],tr_n[z - 1][y][x]]

for z in range(16):
    for y in range(16):
        for x in range(16):
            if tr[z][y][x] != 0:
                s = tr_n = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
                m,n = pos(x,y,z)
                r = tr_r[z][y][x]


                if r[4] == 0 and r[3] == 0:
                    #左后方无方块
                    s[0][5] = 1
                    s[0][6] = 1
                    s[0][7] = 1
                    s[1][8] = 1
                    s[1][9] = 1
                    s[1][10] = 1
                if r[4] == 0 and r[1] == 0:
                    #右后方无方块
                    s[1][2] = 1
                    s[1][3] = 1
                    s[1][4] = 1
                    s[0][5] = 1
                    s[0][6] = 1
                    s[0][7] = 1
                if r[5] == 0 and r[2] == 0:
                    #右下方无方块
                    s[10][0] = 1
                    s[10][1] = 1
                    s[11][2] = 1
                    s[11][3] = 1
                    s[11][4] = 1
                    s[12][5] = 1
                if r[5] == 0 and r[0] == 0:
                    #左下方无方块
                    s[10][11] = 1
                    s[10][12] = 1
                    s[11][8] = 1
                    s[11][9] = 1
                    s[11][10] = 1
                    s[12][7] = 1
                if r[0] == 0 and r[3] == 0:
                    #左侧棱稍暗
                    for k in range(3,11):
                        s[k][12] = 1
                if r[1] == 0 and r[2] == 0:
                    #右侧棱稍暗
                    for k in range(3,11):
                        s[k][0] = 1
                if r[0] == 0 and r[2] == 0:
                    #中侧棱稍暗
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
                #清空后填色（0或1）
                for i in range(13):
                    for j in range(13):
                        if s[i][j]:
                            B[m+j][n+i] = 1
#最后通过PIL将列表转化为图片。
im = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
for i in range(193):
    for j in range(193):
        if B[i][j]:
            #构造：如果此处信息为1，则涂黑色。
            #实际上应该涂（0，0，0，95），只不过这个支线只是用于测试，所以就采用不透明白色了。
            im.putpixel((i,j),(255,255,255,255))

im.save(im_name)
im.show()
print(f"{im_name} 已保存.")
