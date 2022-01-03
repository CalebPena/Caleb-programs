class Shape():
    def what_am_i(self):
        print('I am a shape')
class Rectangle(Shape):
    def __init__(self,l,w):
        self.len=l
        self.width=w
    def area(self):
        return self.len*self.width
class Square(Rectangle):
    def __init__(self,l):
        self.len=l
        self.width=l
    def change_size(self,size_change):
        self.len=self.len+size_change
        self.width=self.width+size_change
