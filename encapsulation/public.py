#example of using protected access specifier

class Parent:
    def __init__(self):
        self._protected_variable = "I am protected"

    def _protected_method(self):
        print("This is a protected method")

class Child(Parent):
    def access_protected(self):
        print(self._protected_variable)  # Accessing protected member in a subclass
        self._protected_method()

obj = Child()
obj.access_protected()  # Output: I am protected, This is a protected method

obj2 = Parent()
print(obj2._protected_variable) # Accessing protected member outside the class (Discouraged but possible)
obj2._protected_method() # Accessing protected method outside the class (Discouraged but possible)