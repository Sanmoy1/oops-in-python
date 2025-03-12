class Complex:
    def __init__(self, real, imaginary):
        self.real= real
        self.imaginary= imaginary

    def __add__(self,other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)
    
    def __sub__(self,other):
        return Complex(self.real-other.real, self.imaginary-other.imaginary)
    
    def __eq__(self,other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __mul__(self,other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)
    
    # def __str__(self):
    #     if self.imaginary >= 0:
    #         return str(self.real) + " + " + str(self.imaginary) + "i"
    #     else:
    #         return str(self.real) + " - " + str(-self.imaginary) + "i"
        
    
c1 = Complex(1,2)
c2 = Complex(3,4)
c3 = c1+c2
c4 = c1-c2
print(c3)
print(c4)