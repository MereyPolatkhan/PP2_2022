class First:
    def __init__(self):
        self.string = "_"
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper()) 

var = First()
var.getString()
var.printString()
