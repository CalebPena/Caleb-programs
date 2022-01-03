class Horse():
    def __init__(self,rider,hieght):
        self.rider=rider
        self.hieght=hieght
class Rider():
    def __init__(self,rider):
        self.rider=rider
rider=Rider('Josh')
horse=Horse(rider,10)
print(horse.rider.rider)
