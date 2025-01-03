#This is an example of compile time polyorphism

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math_op = MathOperations()
print(math_op.add(1, 2))  
print(math_op.add(1, 2, 3)) 
