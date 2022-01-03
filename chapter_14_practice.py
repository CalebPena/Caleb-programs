class Square():
    squares=[]
    def __init__(self,s):
        self.side=s
        self.squares.append(s)
    def __repr__(self):
        return str(self.side)+' by '+str(self.side)
def check(a,b):
    if a is b:
        return True
    else:
        return False
sq1=Square(10)
sq2=sq1
sq3=Square(10)
print(check(sq1,sq2))
print(check(sq1,sq3))
print(check(sq2,sq3))
