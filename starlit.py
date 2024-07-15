import laer
print("\033[92m[星光]1.9.3")
while True:
    l = input("\n__________________________________\n[雨声]选择支线\033[94m_")
    if l == "0":break
    elif l[0] == "1":
        laer.f3()
        continue
    elif l[0] == "2":
        laer.f7(l)
    elif l == "3":
        laer.f8()
        continue
    elif l[0] == "4":
        if len(l) == 1:
            l = "4." + input(f"[检查]选择支线\n4.1 查看文件目录\n4.2 检查资源包\n4.3 检查地图册\n\033[94m4._")
        if l == "4.0":
            continue
        elif l == "4.1":laer.f9()
        elif l == "4.2":laer.fa()
        elif l == "4.3":laer.fb()
        else:
            print(f"[雨声]未知的支线{l}")
    elif l == "5":
        laer.fd()
    elif l == "6":
        laer.fe()
    else:
        print("\n\033[90m__________________________________\n[提示]\n1[编辑资源包]\n2[编辑地图册]\n|   2.1[放置单个方块]\n|   2.2[放置方块组]\n|   2.1[设置笔刷]\n3[生成例图]\n4[检查目录]\n|   4.1[检查文件目录]\n|   4.2[检查资源包]\n|   4.3[检查地图册]\n5[导入资源包]\n6[导出资源包]")