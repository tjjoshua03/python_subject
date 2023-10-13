import math
class Shape:
    def __init__(self, sides):
        self.sides = sides
    
    def getarea(self):
        self.area = 0
        
    def getperimeter(self):
        self.pertimeter = 0
        
class Rectange(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getarea(self):
        self.area = self.length * self.width
        return self.area
    
    def getperimeter(self):
        self.pertimeter = (self.width * 2) + (self.length * 2)
        return self.pertimeter
    
    def __str__(self):
        self.mystr = "I am a rectangle with" + str(self.length) + "and" +str(self.width)+ "as sides"
        return self.mystr
    
    