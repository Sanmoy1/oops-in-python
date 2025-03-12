class Complex_Number:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self,other):
        return Complex_Number(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self,other):
        return Complex_Number(self.real-other.real, self.imaginary-other.imaginary)


    def __eq__(self,other):
        return self.real ==other.real and self.imaginary==other.imaginary
    
    def __mul__(self,other):
        real_part =  self.real*other.real - self.imaginary*other.imaginary
        imaginary_part = self.real*other.real+ self.imaginary*other.imaginary
        return Complex_Number (real_part, imaginary_part)
    
    def __gt__(self,other):
        self_magnitude = self.real**2 + self.imaginary**2
        other_magnitude = other.real**2 + other.imaginary**2
        return self_magnitude> other_magnitude
    
c1 = Complex_Number(1,2)
c2 = Complex_Number(3,4)

c3=c1+c2
c4=c1-c2

