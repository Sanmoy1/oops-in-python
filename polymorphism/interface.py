#this is the example of interface polymorphism

from abc import abstractmethod


class interface:
    @abstractmethod
    def method(self):
        pass

class implementInterface(interface):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def method(self):
        area=self.length*self.breadth
        print("Area of rectangle is: ",area)

def cal_area(interface):#this is the function which is taking interface as argument (interface polymorphism)
    interface.method()
    

obj1=implementInterface(10,20)
cal_area(obj1)