import os
import json
from PIL import Image
#...
bl = [[0,0,0,0,0,1,1,1,0,0,0,0,0],
      [0,0,1,1,1,1,1,1,1,1,1,0,0],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,1,1,1,1,1,0,0],
      [0,0,0,0,0,1,1,1,0,0,0,0,0]]
up = [[0,0,0,1,1,1,0,0,0],
      [1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1],
      [0,0,0,1,1,1,0,0,0]]
lp = [[1,1,0,0,0,0,0],
      [0,0,1,1,1,0,0],
      [0,0,0,0,0,1,1]]
rp = [[0,0,0,0,0,1,1],
      [0,0,1,1,1,0,0],
      [1,1,0,0,0,0,0]]
fl = [[1,1,0,0,0,0],
      [1,1,1,1,1,0],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [0,0,1,1,1,1],
      [0,0,0,0,0,1]]
fr = [[0,0,0,0,1,1],
      [0,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,1,1],
      [1,1,1,1,0,0],
      [1,0,0,0,0,0]]
qi = [[1,1,0],
      [1,1,0],
      [0,1,1]]

def pos(x,y,z):
    m = 9 - 3 * x - 3 * y
    n = 12 + x + y - 4 * z
    return m * 2, n * 2
def e(c):
    r,g,b = c
    r = r * 75 // 100
    g = r * 75 // 100
    b = r * 75 // 100
    return (r,g,b)
def f(c):
    r,g,b = c
    r = r * 875 // 1000
    g = g * 875 // 1000
    b = b * 875 // 1000
    return (r,g,b)

def g_map(file_path,name):
    print("loading terrian...")
    tr_path = os.path.join("map", tr_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        tr = json.load(f)
    tr_n = tr.get('n', [])
    tr_c = tr.get('c', [])
    
    print("loading pixels...")
    for z in range(4):
        for y in range(4):
            for x in range(4):
                if tr_r[z][y][x]:
                    m,n = pos(x,y,z)
                    a,b = tr_c[z][y][x]
                    c = e(a)
                    r = tr_n[z][y][x]
                    for i in range(12):
                        for j in range(12):
                            if bl[i][j]:
                                B[m+i][n+j] = 0
                    if r[4]:
                        for i in range(9):
                            for j in range(4):
                                if up[i][j]:
                                    A[m+i+2][n+j] = a
                            if r[0]:
                                for i in range(7):
                                    for j in range(3):
                                        if lp[i][j]:
                                            A[m+i][n+j+2] = b
                            if r[1]:
                                for i in range(7):
                                    for j in range(3):
                                        if lp[i][j]:
                                            B[m+i+6][n+j] = 1
                            if r[2]:
                                for i in range(7):
                                    for j in range(3):
                                        if rp[i][j]:
                                            A[m+i+6][n+j+2] = b
                            if r[3]:
                                for i in range(7):
                                    for j in range(3):
                                        if rp[i][j]:
                                            B[m+i][n+j] = 1
                    if r[5]:
                        if r[1]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        B[m+i][n+j+10] = 1
                        if r[3]:
                            for i in range(7):
                                for j in range(3):
                                    if rp[i][j]:
                                        B[m+i+6][n+j+10] = 1
                    if r[0]:
                        for i in range(6):
                            for j in range(10):
                                if fl[i][j]:
                                    A[m+i][n+j+3] = c
                        if r[4] == 1 and r[6] == 1:
                            for k in range(8):
                                B[m][n+k+3] = 1
                    if r[2]:
                        for i in range(6):
                            for j in range(10):
                                if fr[i][j]:
                                    A[m+i+7][n+j+3] = c
                        if r[2] == 1 and r[7] == 1:
                            for k in range(8):
                                B[m+12][n+k+3] = 1
                    if r[0] == 1 and r[3] == 1:
                        for k in range(8):
                            A[m+6][n+k+5] == e(b)
                            B[m+6][n+k+5] == 1
                        if r[4]:
                            for i in range(3):
                                for j in range(3):
                                    if q[i][j]:
                                        B[m+i+3][n+j+4] = 1
                                          
    print("on rail...")
    map = Image.new("RGBA",(49,49))
    for i in range(49):
        for j in range(49):
            if r != 0 and g != 0 and b != 0:
                if B[i][j]:
                    r,g,b = f(A[i][j])
                    map.putpixel((i,j),(r,g,b,255))
                else:
                    map.putpixel((i,j),(0,0,0,0))
    map.save(name)
    print("saved as {name}.")
    