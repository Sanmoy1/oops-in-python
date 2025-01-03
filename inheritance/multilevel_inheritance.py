class GrandParent:
    def __init__(self, name):
        # print('GrandParent Init')
        self.name = name
    def display(self):
        print("this is the GrandParent class")

class Parent(GrandParent):
    def __init__(self, Parent_name, name):
        # print('Parent Init')
        GrandParent.__init__(self,name)
        self.Parent_name = Parent_name
    def display(self):
        print("this is the Parent class")
        GrandParent.display(self)


class Child(Parent):
    def __init__(self, age, Parent_name,name):
        # print('Child Init')
        Parent.__init__(self,Parent_name,name)  #either we can use super (self parmeter not required) or the name (self parameter required) of the class
        self.age = age
    def display(self):
        print("this is the Child class")
        Parent.display(self)

obj = Child(25, 'Parent Name', 'GrandParent Name')
obj.display()
