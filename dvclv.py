#©2024 Dustormn.All rights reserved.
print("[dvclv]v2.2.0")
import pickle,os,re
from PIL import Image,ImageDraw
def dian():
    a_=[]
    a0=os.path.abspath('.')
    for a1,_,a2 in os.walk(a0):
        a3 = a1.replace(a0,'').count(os.sep)
        a_.append("|   "*a3+f"[{os.path.basename(a1)}]\n")
        a_.extend("|   "*(a3+1)+f"{a6}\n" for a6 in a2)
    print("\033[90m"+"".join(a_))

class pt:
    def __init__(self):
        with open("pt",'rb') as f:self.ch_,self.tr_=pickle.load(f)
    def c(self):return self.ch_
    def r(self):return self.tr_
    def sh(self):print(f"ch_[{self.ch_}]\ntr_[{self.tr_}]")
    def sv(self):
        with open("pt",'wb') as f:pickle.dump((self.ch_,self.tr_),f)
    def li(self):
        self.sv()
        self.sh()
    def ch(self,su):
        self.ch_=f"ch/{su}/"
        self.li()
    def tr(self,su):
        self.tr_=f"tr/{su}/"
        self.li()
    def ro(self):
        self.ch_="ch/a/"
        self.tr_="tr/a/"
        print("release")
        self.li()
p_=pt()
def p():
    while True:
        ip=input("\033[94m_")
        if len(ip) == 0:return
        elif ip=="sh":p_.sh()
        elif ip=="ro":p_.ro()
        elif me:=re.match(r"ch (\w+)",ip):p_.ch(me.group(1))
        elif me:=re.match(r"tr (\w+)",ip):p_.tr(me.group(1))
        else:print("\033[93m_")

class ch:
    def __init__(self,ch_):
        self.ch_=ch_
        self.ca_ = os.path.join(self.ch_,"a")
        self.cb_ = os.path.join(self.ch_,"b")
        if os.path.exists(self.ch_):
            with open(self.ca_,'rb') as f:self.ca=pickle.load(f)
            with open(self.cb_,'rb') as f:self.cb=pickle.load(f)
        else:
            os.makedirs(self.ch_)
            self.ca=[[(0,0,0),(0,0,0),(0,0,0),(0,0,0)] for _ in range(256)]
            self.cb=["dvst" for _ in range(256)]
            with open(self.ca_,'wb') as f:pickle.dump(self.ca,f)
            with open(self.cb_,'wb') as f:pickle.dump(self.cb,f)
    def lr(self,di,c_1,c_2):
        c0,c1,c2=[int(c_1[i:i+2],16) for i in (0,2,4)]
        c3,c4,c5=[int(c_2[i:i+2],16) for i in (0,2,4)]
        c6,c7,c8,c9,c10,c11=[round(c*0.8) for c in (c0,c1,c2,c3,c4,c5)]
        self.ca[di]=[(c0,c1,c2),(c3,c4,c5),(c6,c7,c8),(c9,c10,c11)]
        with open(self.ca_,'wb') as f:pickle.dump(self.ca,f)
    def am(self,di,nm):
        self.cb[di]=nm
        with open(self.cb_,'wb') as f:pickle.dump(self.cb,f)
    def st(self,di,nm,c_1,c_2):
        self.lr(di,c_1,c_2)
        self.am(di,nm)
    def vw(self,di):
        print(f"\033[90m[{di}] {self.ca[di]}_{self.cb[di]}")
def c():
    c_=ch(p_.c())
    while True:
        ip = input("\033[94m_")
        if len(ip) == 0:return
        elif me:=re.match(r"st (\d+) (\w+) ([a-f0-9]{6}) ([a-f0-9]{6})",ip):c_.st(int(me.group(1)),me.group(2),me.group(3),me.group(4))
        elif me:=re.match(r"vw (\d+)",ip):c_.vw(int(me.group(1)))
        elif me:=re.match(r"am (\d+) (\w+)",ip):c_.am(int(me.group(1)),me.group(2))
        elif me:=re.match(r"lr (\d+) ([a-f0-9]{6}) ([a-f0-9]{6})",ip):c_.lr(int(me.group(1)),me.group(2),me.group(3))
        else:print("\033[93m_")

class tr:
    def __init__(self,ch_,tr_):
        self.ch_=ch_
        self.ca_ = os.path.join(self.ch_,"a")
        self.cb_ = os.path.join(self.ch_,"b")
        if os.path.exists(self.ch_):
            with open(self.ca_,'rb') as f:self.ca=pickle.load(f)
            with open(self.cb_,'rb') as f:self.cb=pickle.load(f)
        else:
            print("\033[93m_")
        self.tr_=tr_
        self.ta_=os.path.join(self.tr_,"a")
        self.tb_=os.path.join(self.tr_,"b")
        if os.path.exists(self.tr_):
            with open(self.ta_,'rb') as f:self.ta=pickle.load(f)
            with open(self.tb_,'rb') as f:self.tb=pickle.load(f)
        else:
            os.makedirs(self.tr_)
            self.ta=[[[[0 for _ in range(12)] for _ in range(16)] for _ in range(16)] for _ in range(16)]
            self.tb=[[[0 for _ in range(16)] for _ in range(16)] for _ in range(16)]
            self.sv()
        self.ma=self.ca[1]
        self.mb=1
        self.mc=self.cb[1]
    def sv(self):
        with open(self.ta_,'wb') as f:pickle.dump(self.ta,f)
        with open(self.tb_,'wb') as f:pickle.dump(self.tb,f)
    def ut(self,x,y,z):
        self.ta[x][y][z] = self.ma
        self.tb[x][y][z] = self.mb
        self.sv()
    def fl(self,x1,y1,z1,x2,y2,z2):
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                for z in range(z1,z2+1):
                    self.ta[x][y][z] = ma
                    self.tb[x][y][z] = mb
        self.sv()
    def br(self,mw):
        self.ma=self.ca[mw]
        self.mc=self.cb[mw]
        if mw==0:
            b=0
            print("deleting")
        else:
            b = 1
            print(f"set \033[94m{self.mc}")
    def oa(self,nm):
        al=[[(0,0,0) for _ in range(193)] for _ in range(193)]
        bl=[[0 for _ in range(193)] for _ in range(193)]
        nl=[[[0 for _ in range(18)] for _ in range(18)] for _ in range(18)]
        for x in range(16):
            for y in range(16):
                for z in range(16):
                    if self.tb[x][y][z]!=0:nl[x+1][y+1][z+1]=1
        for x in range(16):
            for y in range(16):
                for z in range(16):
                    if self.tb[x][y][z]==1:
                        m,n=6*(15-x+y),2*(60+x+y-4*z)
                        for i in range(13):
                            for j in range(2,11):bl[m+i][n+j]=0 
                        for i in range(2,11):bl[m+i][n+1]=0
                        for i in range(2,11):bl[m+i][n+11]=0
                        bl[m+5][n]=bl[m+6][n]=bl[m+7][n]=bl[m+5][n+12]=bl[m+6][n+12]=bl[m+7][n+12]=0
                        h=[nl[x+2][y+1][z+1],nl[x][y+1][z+1],nl[x+1][y+2][z+1],nl[x+1][y][z+1],nl[x+1][y+1][z+2],nl[x+1][y+1][z]]
                        e0,e1,e2,e3=(self.ta[x][y][z][i] for i in range(4))
                        if h[4]==0:
                            al[m+5][n]=al[m+6][n]=al[m+7][n]=al[m+5][n+3]=al[m+6][n+3]=al[m+7][n+3]=e0
                            for i in range(2,11):al[m+i][n+1]=e0
                            for i in range(2,11):al[m+i][n+2]=e0
                            if h[0]==0:al[m][n+2]=al[m+1][n+2]=al[m+2][n+3]=al[m+3][n+3]=al[m+4][n+3]=al[m+5][n+4]=al[m+6][n+4]=e1
                            if h[1]==0:bl[m+5][n]=bl[m+6][n]=bl[m+7][n]=bl[m+8][n+1]=bl[m+9][n+1]=bl[m+10][n+1]=2
                            if h[2]==0:al[m+6][n+4]=al[m+7][n+4]=al[m+8][n+3]=al[m+9][n+3]=al[m+10][n+3]=al[m+11][n+2]=al[m+12][n+2]=e1
                            if h[3]==0:bl[m+2][n+1]=bl[m+3][n+1]=bl[m+4][n+1]=bl[m+5][n]=bl[m+6][n]=bl[m+7][n]=2
                        if h[5]==0:
                            if h[0]==0:bl[m][n+10]=bl[m+1][n+10]=bl[m+2][n+11]=bl[m+3][n+11]=bl[m+4][n+11]=bl[m+5][n+12]=1 
                            if h[2]==0:bl[m+7][n+12]=bl[m+8][n+11]=bl[m+9][n+11]=bl[m+10][n+11]=bl[m+11][n+10]=bl[m+12][n+10]=1
                        if h[0]==0:
                            if h[3]==0:
                                for j in range(3,11):bl[m][n+j]=3
                            for j in range(3,11):al[m][n+j]=e2
                            for j in range(3,11):al[m+1][n+j]=e2
                            for j in range(4,12):al[m+2][n+j]=e2
                            for j in range(4,12):al[m+3][n+j]=e2
                            for j in range(4,12):al[m+4][n+j]=e2
                            for j in range(5,13):al[m+5][n+j]=e2
                        if h[2]==0:
                            if h[1]==0:
                                for j in range(3,11):bl[m+12][n+j]=3
                            for j in range(5,13):al[m+7][n+j]=e2
                            for j in range(4,12):al[m+8][n+j]=e2
                            for j in range(4,12):al[m+9][n+j]=e2
                            for j in range(4,12):al[m+10][n+j]=e2
                            for j in range(3,11):al[m+11][n+j]=e2
                            for j in range(3,11):al[m+12][n+j]=e2
                        if h[0] == 0 and h[2]==0:
                            for j in range(5,13):al[m+6][n+j]=e3
        p=[]
        for j in range(193):
            w=[]
            for i in range(193):
                r,g,b = al[i][j]
                if bl[i][j] == 1:r,g,b=int(r*0.9),int(g*0.9),int(b*0.9)
                elif bl[i][j]==2:r,g,b=int(r*0.7)+63,int(g*0.7)+63,int(b*0.7)+63
                elif bl[i][j]==3:r,g,b=int(r*0.8),int(g*0.8),int(b*0.8)
                w.append((r,g,b))
            p.append(w)
        u=Image.new('RGB',(193,193),color=(0,0,0))
        u.putdata([l for w in p for l in w])
        u.save(nm+".png")
def r():
    r_=tr(p_.c(),p_.r())
    while True:
        ip = input("\033[94m_")
        if len(ip) == 0:return
        elif me:=re.match(r"ut (\d+) (\d+) (\d+)",ip):r_.ut(int(me.group(1)),int(me.group(2)),int(me.group(3)))
        elif me:=re.match(r"fl (\d+) (\d+) (\d+) (\d+) (\d+) (\d+)",ip):r_.fl(int(me.group(1)),int(me.group(2)),int(me.group(3)),int(me.group(4)),int(me.group(5)),int(me.group(6)))
        elif me:=re.match(r"br (\d+)",ip):r_.br(int(me.group(1)))
        elif me:=re.match(r"oa (\w+)",ip):r_.oa(me.group(1))
        else:print("\033[93m_")

def dc(n):
    with open(f"ch/{n}/b","rb") as f:cv=pickle.load(f)
    p=[]
    for i in range(64):
        for j in range(4):
            k=i+j*64
            p.append(f"[{k}]_{cv[k]}".ljust(20))
        p.append("\n")
    print("\033[90m"+"".join(p))
def dr(n):
    with open(f"tr/{n}/a","rb") as f:rv=pickle.load(f)
    iy = Image.open("lab.png")
    ly = ImageDraw.Draw(iy)
    for z in range(16):
        for y in range(16):
            for x in range(16):
                cu=rv[x][y][z][0]
                if cu!=(0,0,0):
                    ly.rectangle([16*x+2,16*y+288*z+2,16*x+17,16*y+288*z+17],fill=cu)
    iy.show()
def w(ip,n):
    if ip=="ch":dc(n)
    elif ip=="tr":dr(n)
    else:print("\033[93m_")

def main():
    while True:
        print()
        ln = input("\033[92m_")
        if len(ln) == 0:break
        elif ln==".":dian()
        elif ln == "pt":p()
        elif ln == "ch":c()
        elif ln == "tr":r()
        elif lm:=re.match(r"cr (\w+) (\w+)",ln):w(lm.group(1),lm.group(2))
        else:print("\033[93m_")
try:
    main()
except Exception as e:
    print(e)
    print("\033[93m_")