print("[星光]1.6.0")
print("")
print("[主页面]")
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
    laer = open("laer.txt","r")
    print(laer.read())
    laer.close