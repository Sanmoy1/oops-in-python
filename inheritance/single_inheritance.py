#example of single level inheritance in python
class Parent:
    def __init__(self, name):
        print('Parent Init')
        self.name = name
    def display(self):
        print("this is the parent class")
class child(Parent):
    def __init__(self, name, age):
        print('Child Init')
        super().__init__(name)
        self.age = age
    def display(self):
        print("this is the child class")
        super().display()
        
obj = child('John', 25)
obj.display()
print(f"Name: {obj.name}, Age: {obj.age}")