nd = 1
sh = '|   '

d = '\033[0m'
d0 = '\033[90m'
d1 = '\033[91m'
d2 = '\033[92m'
d3 = '\033[93m'
d4 = '\033[94m'
d5 = '\033[95m'

def l1():
    print('_'*68)
def l2():
    print(f'{d2}{sh*nd}')
def l3(s):
    print(f'{d2}{sh*nd}{d}{s}')
def l4(s):
    return input(f'{d2}{sh*nd}{d}{s}{d4}_')
def l5():
    inp = input(f'{d2}{sh*nd}{d4}_')
    if len(inp) == 0:
        return "0"
    return inp
def l6(s,o):
    print(f'{d2}{sh*nd}{d}{s}{d4}{o}')

#

def l1():
    ...
def l2():
    ...
#功能方法
def g11():
    ...
def g12():
    ...
#二级分支
def f1(ch_):
    nd += 1
    l3("[编辑预设]")
def f2(ch_,tr_):
    nd += 1
    l3("[编辑地图册]")
def f3(tr_,pl_):
    nd +=1
    l3("[生成例图]")
    while True:
        l2()
        mu = l5()
def f4():
    nd += 1
    l3("[检查]")
    while True:
        mu = l5()
def f5():
    nd += 1
    l3("[文件转换]")
    while True:
        mu = l5()

print('laer v2.0.0-alpha')
l1()
#'©2024 Dustormn.All rights reserved.'

while True:
    ln = l5()
    if ln == "0":
        print('退出.')
        break
    elif ln == "1":
        ch_ = l4('指定预设')
        f1(ch_)
    elif ln == "2":
        ch_ = l4('指定预设')
        tr_ = l4('指定地图册')
        f2(ch_,tr_)
    elif ln == "3":
        tr_ = l4('指定地图册')
        pl_ = l4('指定图形')
        f3(tr_,pl_)
    elif ln == "4":
        f4()
    elif ln == "5":
        f5()
    else:
        l1()
        print("""\033[90m[提示]
|
1[编辑预设]
|_输入预设名
|   |_索引[0~255]
|   |_名称
|   |_主色
|   |_副色
|
2[编辑地图册]
|_预设名
|_地图册名
|   2.1[放置单个方块]
|   |_坐标x
|   |_坐标y
|   |_坐标z
|   2.2[放置方块组]
|   |_起点坐标x
|   |_起点坐标y
|   |_起点坐标z
|   |_终点坐标x
|   |_终点坐标y
|   |_终点坐标z
|   2.3[设置笔刷]
|   |_索引[0~255]
|
3[生成例图]
|   |3.1[生成]
|   |_地图册名
|   |_文件名
|
|   |3.2[生成并预览]
|   |_地图册名
|   |_文件名
|
|   |3.3[预览]
|   |_文件名
|
4[检查]
|   4.1[检查文件]
|   4.2[检查预设]
|   |_预设名
|   4.3[检查地图册]
|   |_地图册名
|
5[文件转换]
|   5.1[导入数据]
|   |_数据路径
|   |_文本路径
|
|   5.2[导出数据]
|   |_文本路径
|   |_数据路径
""")
        l1()
