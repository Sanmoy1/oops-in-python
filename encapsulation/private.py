#this is an example of private encapsulation (access specifier)

class MyClass:
    def __init__(self):
        self.__private_variable = "I am private"

    def __private_method(self):
        print("This is a private method")
    
    def access_private(self):
        print(self.__private_variable)
        self.__private_method()

obj = MyClass()
obj.access_private() # Output: I am private, This is a private method

# Attempting to access private members directly (Will raise an AttributeError)
# print(obj.__private_variable)  # AttributeError: 'MyClass' object has no attribute '__private_variable'
# obj.__private_method()        # AttributeError: 'MyClass' object has no attribute '__private_method'

# Accessing private members using name mangling (Possible but generally not recommended)
print(obj._MyClass__private_variable)  # Output: I am private
obj._MyClass__private_method()        # Output: This is a private method