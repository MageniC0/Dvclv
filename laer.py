import d,d1,d2,d3,d4
def f(ch_,tr_,pl_):
    while True:
        lin = input("\n__________________________________\n[雨声]选择支线\033[94m_")
        if lin[0] == "0":break
        elif lin[0] == ".":d.f(lin)
        elif lin[0] == "1":d1.f(lin,ch_)
        elif lin[0] == "2":d2.f(lin,ch_,tr_)
        elif lin[0] == "3":d3.f(tr_,pl_)
        elif lin[0] == "4":d4.f(lin,ch_,tr_)
        else:
            with open("ref","r",encoding = 'utf-8') as file:print("\033[90m"+file.read())
