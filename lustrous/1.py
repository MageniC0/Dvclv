import os

i = "input/"
if not os.path.exists(i):
    os.makedirs(i)
    print(f"创建文件夹\033[94m{i}\033[0m.")
else:
    print(f"文件夹\033[94m{i}\033[0m已存在.")  
a_=[]
a0=os.path.abspath(i)
for a1,_,a2 in os.walk(a0):
    a3 = a1.replace(a0,'').count(os.sep)
    a_.append("|   "*a3+f"[{os.path.basename(a1)}]\n")
    a_.extend("|   "*(a3+1)+f"{a6}\n" for a6 in a2)
print("\033[90m"+"".join(a_))

o = "output/"
if not os.path.exists(o):
    os.makedirs(o)
    print(f"创建文件夹\033[94m{s}\033[0m.")
else:
    print(f"文件夹\033[94m{s}\033[0m已存在.")
a_=[]
a0=os.path.abspath(o)
for a1,_,a2 in os.walk(a0):
    a3 = a1.replace(a0,'').count(os.sep)
    a_.append("|   "*a3+f"[{os.path.basename(a1)}]\n")
    a_.extend("|   "*(a3+1)+f"{a6}\n" for a6 in a2)
print("\033[90m"+"".join(a_))