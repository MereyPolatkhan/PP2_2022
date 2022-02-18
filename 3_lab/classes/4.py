class Point:
    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor
    
    def show(self):
        return f'x = {self.x}; y = {self.y}'
    
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
        
    def distance(self, pt):
        dx = pt.x 
