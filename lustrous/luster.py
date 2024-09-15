from PIL import Image

up_ = [[0,0,1,1,1,0,0],
       [1,1,1,1,1,1,1],
       [0,0,1,1,1,0,0]]
left_ = [[1,1,0],
         [1,1,1],
         [1,1,1],
         [1,1,1],
         [0,0,1]]
right_ = [[0,1,1],
          [1,1,1],
          [1,1,1],
          [1,1,1],
          [1,0,0]]

def graph(l):
    return [[(0, 0, 0, 0) for _ in range(l)] for _ in range(l)]

print("loading...")

up = graph(16)
left = graph(16)
right = graph(16)
raster = Image.open("input/test.png")
for j in range(16):
    for i in range(16):
        up[j][i] = raster.getpixel((i, j))
        left[j][i] = raster.getpixel((i+16, j))
        right[j][i] = raster.getpixel((i+32, j))

chcw = Image.new("RGBA", (97, 97), (0, 0, 0, 0))
chcl = graph(97)

for j in range(16):
    for i in range(16):
        m, n = 49 +3*i, 32 - i + 4*j
        c = right[j][i]
        for y in range(5):
            for x in range(3):
                if right_[y][x]:
                    chcl[n+y][m+x] = c
for j in range(16):
    for i in range(16):
        m, n = 3*i, 17 + i + 4*j
        c = left[j][i]
        for y in range(5):
            for x in range(3):
                if left_[y][x]:
                    chcl[n+y][m+x] = c
for j in range(16):
    for i in range(16):
        m, n = 45 + 3*i - 3*j, i + j
        c = up[j][i]
        for y in range(3):
            for x in range(7):
                if up_[y][x]:
                    chcl[n+y][m+x] = c

for k in range(16):
    _up = up[15][15-k]
    _left = left[k][15]
    _right = up[k][15]
    chcl[33-k][48-3*k]=_up
    chcl[33-k][47-3*k]=_up
    chcl[32-k][46-3*k]=_up
    chcl[32-k][45-3*k]=_up
    chcl[33+4*k][48]=_left
    chcl[34+4*k][48]=_left
    chcl[35+4*k][48]=_left
    chcl[36+4*k][48]=_left
    chcl[33-k][48+3*k]=_right
    chcl[33-k][49+3*k]=_right
    chcl[32-k][50+3*k]=_right
    chcl[32-k][51+3*k]=_right
chcw.putdata([i for j in chcl for i in j])
chcw.save("output/test.png")
chcw.show()