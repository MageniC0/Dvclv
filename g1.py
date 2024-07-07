import os
def f1():
    g1 = os.path.dirname(os.path.abspath(__file__))
    g2 = 0
    g3 = ''
    for g4, g5, g6 in os.walk(g1):
        g5.sort()
        g7 = g14.count(os.sep) - g11.count(os.sep)
        g3 = '_' * g7
        for g8 in g5:
            print(f"{g3}~{g8}")
        g9 = os.path.basename(__file__)
        for g0 in g6:
            if g0 != g9:
                print(f"{g3}_ {g0}")