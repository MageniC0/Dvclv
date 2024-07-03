from PIL import Image
import json

ch_n = input("res name:")+".png"
tr_n = input("trr name:")+".json"  #0/1
im_n = input("save as:")+".png"

with open(tr_name) as f1:
    tr = json.load(f1)
with open(ch_name) as f1:
    ch = json.load(f1)

def pos(x, y, z):
    m = 15+ x - y
    n = 60 + x + y - 4 * z
    return m * 6, n * 2

def sop(u,v):
    r,g,b = u
    r = int(r * v)
    g = int(g * v)
    b = int(b * v)
    return r,g,b

im = Image.new("RGBA", (193, 193),(255,255,255,0))
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
            tr_r[z-1][y-1][x-1] = [tr_n[z][y][x + 1],
                                   tr_n[z][y][x - 1],
                                   tr_n[z][y + 1][x],
                                   tr_n[z][y - 1][x],
                                   tr_n[z + 1][y][x],
                                   tr_n[z - 1][y][x]]

for z in range(16):
    for y in range(16):
        for x in range(16):
            if tr[z][y][x] != 0:
                m,n = pos(x,y,z)
                s = [[0 for _ in range(13)] for _ in range(13)]
                t = [[(255,255,255,0) for _ in range(13)] for _ in range(13)]
                c = tr[z][y][x]
                c_a,c_b = ch[c]
                c_c = sop(c_a,0.75 )
                c_d = sop(c_b,0.875)
                r = tr_r[z][y][x]
                if r[4] == 0:
                    t[0 ][5 ] = c_a
                    if r[3 ] == 0:
                        s[0 ][5 ] = 2
                        s[0 ][6 ] = 2
                        s[0 ][7 ] = 2
                        s[1 ][8 ] = 2
                        s[1 ][9 ] = 2
                        s[1 ][10] = 2
                    if r[1 ] == 0:
                        s[1 ][2 ] = 2
                        s[1 ][3 ] = 2
                        s[1 ][4 ] = 2
                        s[0 ][5 ] = 2
                        s[0 ][6 ] = 2
                        s[0 ][7 ] = 2
                if r[5] == 0 and r[2] == 0:
                    s[10][0] = 1
                    s[10][1] = 1
                    s[11][2] = 1
                    s[11][3] = 1
                    s[11][4] = 1
                    s[12][5] = 1
                if r[5] == 0 and r[0] == 0:
                    s[10][11] = 1
                    s[10][12] = 1
                    s[11][8] = 1
                    s[11][9] = 1
                    s[11][10] = 1
                    s[12][7] = 1
                if r[0] == 0 and r[3] == 0:
                    for k in range(3,11):
                        s[k][12] = 1
                if r[1] == 0 and r[2] == 0:
                    for k in range(3,11):
                        s[k][0] = 1
                if r[0] == 0 and r[2] == 0:
                    for k in range(5,13):
                        s[k][6] = 1
                m,n = pos(x,y,z)
'''
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
                for i in range(13):
                    for j in range(13):
                        if s[i][j]:
                            B[m+j][n+i] = 1
'''
im = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
for i in range(193):
    for j in range(193):
        if B[i][j]:
            im.putpixel((i,j),(255,255,255,255))

im.save(im_name)
im.show()
print(f"{im_name} 已保存.")
