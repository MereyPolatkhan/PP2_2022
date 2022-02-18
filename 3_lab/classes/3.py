class Shape:        
    def __init__(self):
        pass



class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width   

var = Rectangle(6, 5) 
print(var.area())