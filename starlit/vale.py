import json
print("mode list:\n0.save\n1.set one block\n2.set blocks\n3.build or delete")
name = input("name:") + ".json"
tr = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
bd = 1
i = 0
mod = None

def pu(tr, x1, y1, z1, x2, y2, z2, bd):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                tr[z][y][x] = bd

while True:
    t = input('mode_')
    if t.isdigit():
        mod = int(t)
    if mod == 0:
        break
    if mod == 1:
        x = int(input("x_"))
        y = int(input("y_"))
        z = int(input("z_"))
        tr[z][y][x] = 1
        print(f"set block {i} at tr[{z}][{y}][{x}]")
    elif mod == 2:
        x = int(input("x_"))
        y = int(input("y_"))
        z = int(input("z_"))
        x0 = int(input("x0_"))
        y0 = int(input("y0_"))
        z0 = int(input("z0_"))
        pu(tr, x, y, z, x0, y0, z0, bd)
        print(f"set block {i} from ({x},{y},{z}) to ({x0},{y0},{z0}).")
    elif mod == 3:
        bd = 1 - bd
        if bd:
            print("building.")
        else:
            print("deleting.")
    i = i + 1

with open(name, "w") as file:
    json.dump(tr, file, indent=1)
print("block saved")