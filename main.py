print("[星光]1.6.0")
print("")
print("输入0返回")
print("输入数字继续")
print("[主页面]")
print("1_ 检查文件")
print("2_ 生成图形")
print("3_ 设计资源包")
print("4_ 设计地图")
print("5_ 参考文档")

i = input("")

import g1
import g2
import g3
import g4

if i == "0":
    print("告辞。")

if i == "1":
    g1.f()

if i == "2":
    g2.f()

if i == "3":
    g3.f()

if i == "4":
    g4.f()

if i == "5":
    file = open("laer.txt","r")
    print(file)
    file.close