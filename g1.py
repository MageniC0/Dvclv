import os
def f():
    h1 = os.path.dirname(os.path.abspath(__file__))
    h2 = 0
    h3 = ''
    for h4, h5, h6 in os.walk(h1):
        h5.sort()
        h2 = h4.count(os.sep) - h1.count(os.sep)
        h3 = '_' * h2
        for h8 in h5:
            print(f"{h3}~{h8}")
        for h0 in h6:
            print(f"{h3}_{h0}")