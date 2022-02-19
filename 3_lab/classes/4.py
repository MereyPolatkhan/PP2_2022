import math

class Point:
    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor
    
    def show(self):
        return f'x = {self.x}; y = {self.y}'
    
    def move(self, x_plus, y_plus):
        self.x = self.x + x_plus
        self.y = self.y + y_plus
        
    def distance(self, x1, y1):
        dist_x = x1 - self.x
        dist_y = y1 - self.y 
        dist = math.sqrt(dist_x ** 2 + dist_y ** 2)
        return dist 

var = Point(4, 6) 
print(var.show())
var.move(2, 0)
print(var.show())
print(var.distance(0, 0))
