'''
Write a complex number class with a constructor that takes two arguments, the real and imaginary parts of the number. Implement the following overloaded operations for the class:
add - add two complex numbers
subtract - subtract two complex numbers
multiply - multiply two complex numbers
divide - divide two complex numbers
'''
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return Complex(self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2), (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)

    def __str__(self):
        return f'{self.real} + {self.imag}i'
def main():
    c1=Complex(2,3)
    c2=Complex(4,5)
    print(c1+c2)
    
if __name__ == '__main__':
    main()
    
    