import pickle
from PIL import Image
def f(tr_,pl_):
    nm = pl_ + input("[制图]文件名\033[94m_") + ".png"
    try:
        with open(tr_+'a','rb') as file:tra = pickle.load(file)
        with open(tr_+'b','rb') as file:trb = pickle.load(file)
    except Expection:
        print(f"[制图]未找到\033[94m{tr_}")
        return
    print("[制图]传送数据...")
    trn = [[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if trb[x][y][z] != 0:
                    trn[x+1][y+1][z+1] = 1
    pix = [[(0,0,0) for _ in range(193)] for _ in range(193)]
    daw = [[0 for _ in range(193)] for _ in range(193)]
    for x in range(16):
        for y in range(16):
            for z in range(16):
                if trb[x][y][z] == 1:
                    pi = [[(0,0,0) for _ in range(13)] for _ in range(13)]
                    da = [[0 for _ in range(13)] for _ in range(13)]
                    t = tra[x][y][z]
                    rn = [
                        trn[x+2][y+1][z+1],
                        trn[ x ][y+1][z+1],
                        trn[x+1][y+2][z+1],
                        trn[x+1][ y ][z+1],
                        trn[x+1][y+1][z+2],
                        trn[x+1][y+1][ z ]]
                    a = (t[0],t[1],t[2])
                    b = (t[3],t[4],t[5])
                    az = (t[6],t[7],t[8])
                    bz = (t[9],t[10],t[11])
                    if rn[4] == 0:
                        for i in range(2,11):pi[i][1] = a
                        for i in range(2,11):pi[i][2] = a
                        pi[5][0] = a
                        pi[6][0] = a
                        pi[7][0] = a
                        pi[5][3] = a
                        pi[6][3] = a
                        pi[7][3] = a
                        if rn[0] == 0:
                            pi[0][2] = b
                            pi[1][2] = b
                            pi[2][3] = b
                            pi[3][3] = b
                            pi[4][3] = b
                            pi[5][4] = b
                            pi[6][4] = b
                        if rn[1] == 0:
                            da[5][0] = 2
                            da[6][0] = 2
                            da[7][0] = 2
                            da[8][1] = 2
                            da[9][1] = 2
                            da[10][1] = 2
                        if rn[2] == 0:
                            pi[6][4] = b
                            pi[7][4] = b
                            pi[8][3] = b
                            pi[9][3] = b
                            pi[10][3] = b
                            pi[11][2] = b
                            pi[12][2] = b
                        if rn[3] == 0:
                            da[2][1] = 2
                            da[3][1] = 2
                            da[4][1] = 2
                            da[5][0] = 2
                            da[6][0] = 2
                            da[7][0] = 2
                    if rn[5] == 0:
                        if rn[0] == 0:
                            da[0][10] = 1
                            da[1][10] = 1
                            da[2][11] = 1
                            da[3][11] = 1
                            da[4][11] = 1
                            da[5][12] = 1 
                        if rn[2] == 0:
                            da[7][12] = 1
                            da[8][11] = 1
                            da[9][11] = 1
                            da[10][11] = 1
                            da[11][10] = 1
                            da[12][10] = 1
                    if rn[0] == 0:
                        if rn[3] == 0:
                            for j in range(3,11):da[0][j] = 3
                        for j in range(3,11):pi[0][j] = az
                        for j in range(3,11):pi[1][j] = az
                        for j in range(4,12):pi[2][j] = az
                        for j in range(4,12):pi[3][j] = az
                        for j in range(4,12):pi[4][j] = az
                        for j in range(5,13):pi[5][j] = az
                    if rn[2] == 0:
                        if rn[1] == 0:
                            for j in range(3,11):da[12][j] = 3
                        for j in range(5,13):pi[7][j] = az
                        for j in range(4,12):pi[8][j] = az
                        for j in range(4,12):pi[9][j] = az
                        for j in range(4,12):pi[10][j] = az
                        for j in range(3,11):pi[11][j] = az
                        for j in range(3,11):pi[12][j] = az
                    if rn[0] == 0 and rn[2] == 0:
                        for j in range(5,13):pi[6][j] = bz
                    m = 6 * (15 - x + y)
                    n = 2 * (60 + x + y - 4 * z)
                    for i in range(13):
                        for j in range(2,11):
                            daw[m+i][n+j] = 0 
                    for i in range(2,11):daw[m+i][n+1] = 0
                    for i in range(2,11):daw[m+i][n+11] = 0
                    daw[m+5][n] = 0
                    daw[m+6][n] = 0
                    daw[m+7][n] = 0
                    daw[m+5][n+12] = 0
                    daw[m+6][n+12] = 0
                    daw[m+7][n+12] = 0
                    for i in range(13):
                        for j in range(13):
                            if pi[i][j] != (0,0,0):
                                daw[m+i][n+j] = da[i][j]
                                pix[m+i][n+j] = pi[i][j]
    img = Image.new('RGBA',(193,193), color=(255, 255, 255, 0))
    for i in range(193):
        for j in range(193):
            r,g,b = pix[i][j]
            if daw[i][j] == 1:
                r = int(r*0.9)
                g = int(g*0.9)
                b = int(b*0.9) 
            if daw[i][j] == 2:
                r = int(r*0.7)+63
                g = int(g*0.7)+63
                b = int(b*0.7)+63
            if daw[i][j] == 3:
                r = int(r*0.85)
                g = int(g*0.85)
                b = int(b*0.85)
            img.putpixel((i,j),(r,g,b,255))
    img.save(nm)
    print(f"\n[制图]生成图像\033[94m{nm}.\n")
    img.show()