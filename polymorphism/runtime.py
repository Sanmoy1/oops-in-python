#this is the example of runtime polymorphism

class a:
    def sound(self):
        print("sound of a")
class b(a):
    def sound(self):
        print("sound of b")
class c(a):
    def sound(self):
        print("sound of c")

d=c()
d.sound()

        