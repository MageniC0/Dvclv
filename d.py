import pickle
def f(lin):
    if len(lin)==1:
        lin = ".."+input("[路径]路径设置\n..1:查看当前路径\n..2:修改路径\n..3:重置为默认路径\n[路径]选择模块\033[94m.._")
    if lin == "..1":
        with open("pl",'rb') as f:g = pickle.load(f)
        print("\033[90m[路径列表]")
        for d,e in g.items():print(f"\033[90m{d}____{e}")
    if lin == "..2":
        ch_ = input(f"[路径]新的chvjv路径\033[94m_")
        tr_ = input(f"[路径]新的terrain路径\033[94m_")
        pl_ = input(f"[路径]新的plot路径\033[94m_")
        with open("pl",'wb') as f: pickle.dump({"ch_":f"r/ch/{ch_}/","tr_":f"r/ch/{tr_}/","pl_":f"r/pl/{pl_}/"},f)
    if lin == "..3":
        with open("pl",'wb') as f:pickle.dump({"ch_":"r/ch/d/","tr_":"r/tr/d/","pl_":"r/pl/d/"},f)