import os
def f(h1 = os.path.dirname(os.path.abspath(__file__)), h2=0):
    h3 = '•   ' * h2
    for h4, h5, h6 in os.walk(h1):
        print(f"{h3}____[{os.path.basename(h4)}]")
        for h7 in h6:
            print(f"•   {h3}{h7}")
        if h5:
            for h8 in h5:
                f(os.path.join(h4, h8), h2 + 1)