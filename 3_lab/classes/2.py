class Shape:        
    def __init__(self):
        self.area1 = 0
    def area(self):
        print(self.area1)


class Square(Shape): 
    def __init__(self, _length):
        self.length = _length 
    def area(self):
        print(self.length ** 2)

var1 = Shape() 
var1.area()
var2 = Square(14)
var2.area()


    



