import laer
import pickle,os
with open("pl", 'rb') as f:pl = pickle.load(f)
ch_ = pl["ch_"]
tr_ = pl["tr_"]
pl_ = pl["pl_"]
if not os.path.exists(ch_):os.makedirs(ch_)
if not os.path.exists(tr_):os.makedirs(tr_)
if not os.path.exists(pl_):os.makedirs(pl_)
print("\033[92m[星光]1.7.0")
laer.f(ch_,tr_,pl_)