class Point:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary= imaginary

    def __add__(self,other):
        return Point(self.real+ other.real, self.imaginary+other.imaginary)
    
    def __eq__(self,other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __str__(self):
        return "Point({},{})".format(self.real, self.imaginary) 
    
p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1+p2
print(p3)
print(p1==p2)
