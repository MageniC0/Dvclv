import laer
print("\033[92m[星光]1.9.2")
while True:
    line = input("\n__________________________________\n[雨声]选择支线\033[94m_")
    if line == "0":break
    elif line[0] == "1":
        laer.f3()
        continue
    elif line[0] == "2":
        laer.f7(line)
    elif line == "3":
        laer.f8()
        continue
    elif line[0] == "4":
        if len(line) == 1:
            line = "4." + input(f"[检查]选择支线\n4.1 查看文件目录\n4.2 检查资源包\n4.3 检查地图册\n\033[94m4._")
        if line == "4.0":
            continue
        elif line == "4.1":laer.f9()
        elif line == "4.2":laer.fa()
        elif line == "4.3":laer.fb()
        else:
            print(f"[雨声]未知的支线{line}")
    else:
        print("\n\033[90m__________________________________\n[提示]\n1[编辑资源包]\n2[编辑地图册]\n|   2.1[放置单个方块]\n|   2.2[放置方块组]\n|   2.1[设置笔刷]\n3[生成例图]\n4[检查目录]\n|   4.1[检查文件目录]\n|   4.2[检查资源包]\n|   4.3[检查地图册]")