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
        self.pertimeter = (self.width + self.length) * 2
        return self.pertimeter
    
    def __str__(self):
        self.mystr = "I am a rectangle with" + str(self.length) + "and" +str(self.width)+ "as sides"
        return self.mystr
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def getarea(self):
        s = (self.a + self.b + self.c) / 2
        self.area = (s * (s - self.a) * (s - self.b) * (s - self.c))** 0.5
        return self.area
    
    def getperimeter(self):
        self.pertimeter = self.a + self.b + self.c
        return self.pertimeter
    
    def __str__(self):
        self.mystr = "I am a triangle with" + str(self.a) + "," + str(self.b) + "," + str(self.c) + "as sides"
        return self.mystr
    
    
class Circle(Shape):
    pi = 3.14
    
    def __init__(self, r):
        self.r = r
        
    def getarea(self):
        self.area = Circle.pi * self.r * self.r
        return self.area
    
    def getperimeter(self):
        self.pertimeter = 2 * Circle.pi * self.r
        return self.pertimeter
    
    def __str__(self):
        self.mystr = "I am a circle with" + str(self.r) + "as radius and" + self.area + "as area and" + self.pertimeter + "as perimeter"
        return self.mystr
    
class Square(Rectange):
    def __init__(self, length):
        self.length = length
        
    def getarea(self):
        self.area = self.length * self.length
        return self.area
    
    def getperimeter(self):
        self.pertimeter = self.length * 4
        return self.pertimeter
    
    def __str__(self):
        self.mystr = "I am a square with " + str(self.length) + " as a side"
        return self.mystr
    
    
#test code    
square_instance = Square(4)
result = square_instance.__str__()
print(result)