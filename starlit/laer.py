im_name = input("image_name:")+".png"
tr_name = input("terrian name:")+".json"
import json
from PIL import Image
def pos(x,y,z):
    m = 15 + x - y
    n = 60 + x + y - 4 * z
    return m * 6, n * 2
with open(tr_name) as file:
    tr = json.load(file)
tr_n = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
for z in range(16):
    for y in range(16):
        for x in range(16):
            if tr[z][y][x] == 1:
                tr_n[z+1][y+1][x+1] = 1
tr_r = [[[[0,0,0,0,0,0,0,0] for _ in range(16)] for _ in range(16)] for _ in range(16)]
for z in range(1,17):
    for y in range(1,17):
        for x in range(1,17):
            r0 = tr_n[z][y][x + 1]
            r1 = tr_n[z][y][x - 1]
            r2 = tr_n[z][y + 1][x]
            r3 = tr_n[z][y - 1][x]
            r4 = tr_n[z + 1][y][x]
            r5 = tr_n[z - 1][y][x]
            r6 = tr_n[z][y-1][x+1]
            r7 = tr_n[z][y+1][x-1]
            tr_r[z-1][y-1][x-1] = [r0,r1,r2,r3,r4,r5,r6,r7]
B = [[0 for _ in range(193)] for _ in range(193)]
for z in range(16):
    for y in range(16):
        for x in range(16):
            if tr[z][y][x] == 1:
                r = tr_r[z][y][x]
                s = [[0 for _ in range(13)] for _ in range(13)]
                if r[4] == 0 and r[3] == 0:
                    s[0][5] = 1
                    s[0][6] = 1
                    s[0][7] = 1
                    s[1][8] = 1
                    s[1][9] = 1
                    s[1][10] = 1
                if r[4] == 0 and r[1] == 0:
                    s[1][2] = 1
                    s[1][3] = 1
                    s[1][4] = 1
                    s[0][5] = 1
                    s[0][6] = 1
                    s[0][7] = 1
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
                if r[0] == 0 and r[3] == 0 and r[6] == 0:
                    for k in range(3,11):
                        s[k][12] = 1
                if r[1] == 0 and r[2] == 0 and r[7] == 0:
                    for k in range(3,11):
                        s[k][0] = 1
                if r[0] == 0 and r[2] == 0:
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
                for i in range(13):
                    for j in range(13):
                        if s[i][j]:
                            B[m+j][n+i] = 1
im = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
for i in range(193):
    for j in range(193):
        if B[i][j]:
            im.putpixel((i,j),(0,0,0,255))
im.save(im_name)
print(f"saved as {im_name}.")