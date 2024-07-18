class ysj:
    def __init__(self,theme):
        self.theme = theme
        self.ind = 1
        self.ash = '|   '
        self.dawn = '\033[0m'
        self.dawn2 = '\033[92m'
        self.dawn4 = '\033[94m'
    
    print(f'[{self.theme}]启动！')
    
    def adl(self):
        self.ind += 1

    def pur(self):
        print('_' * 199)

    def voidline(self):
        print(f'{self.dawn2}{self.ash * self.ind}')

    def printline(self, string):
        print(f'{self.dawn2}{self.ash * self.ind}{self.dawn}{string}')

    def inputline(self, string):
        inp = input(f'{self.dawn2}{self.ash * self.ind}{self.dawn}{string}{self.dawn4}_')
        return inp

pr = ysj("test")
pr.pur()
pr.voidline()
pr.adl()
pr.printline("别炸了！")
