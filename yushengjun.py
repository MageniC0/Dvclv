class ysj:
    def __init__(self,theme):
        print('_'*39)
        print(theme)
        self.ind = 1
        self.ash = '|   '
        self.dawn = '\033[0m'
        self.dawn = '\033[90m'
        self.dawn1 = '\033[91m'
        self.dawn2 = '\033[92m'
        self.dawn3 = '\033[93m'
        self.dawn4 = '\033[94m'
        self.dawn5 = '\033[95m'
    
    def lad(self):
        self.ind += 1
    def lsi(self):
        if self.ind != 0:
            self.ind -= 1
        else:
            raise ValueError("unexpected value 0.")
    def purline(self):
        print('_' * 39)
    def voidline(self):
        print(f'{self.dawn2}{self.ash*self.ind}')
    def printline(self,string):
        print(f'{self.dawn2}{self.ash*self.ind}{self.dawn}{string}')
    def inputline(self,string):
        return input(f'{self.dawn2}{self.ash*self.ind}{self.dawn}{string}{self.dawn4}_')
    def callline(self,string,object):
        print(f'{self.dawn2}{self.ash*self.ind}{string}{self.dawn4}{object}')
