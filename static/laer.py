from PIL import Image
import json
cube_name = input("cube name:")+".png"
tr_name = input("terrian name:")+".json"
png_name = input("save as:")+".png"

with open(tr_name) as file:
    trr = json.load(file)
def pos(x, y, z):
    m = 15+ x - y
    n = 60 + x + y - 4 * z
    return m * 6, n * 2
mapt = Image.new("RGBA", (193, 193),(255,255,255,0))
cube = Image.open(cube_name)
    
for z in range(16):
    for y in range(16):
        for x in range(16):
            if trr[z][y][x]:
                m,n = pos(x,y,z)
                for i in range(13):
                    for j in range(13):
                        s = cube.getpixel((i,j))
                        r,g,b,a = s
                        if a:
                            mapt.putpixel((m+i,n+j), (r, g, b, 255))

mapt.save(png_name)
print("saved as png.")