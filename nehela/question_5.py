class Room:
    def __init__(self,height,width,breath):
        self.height=height
        self.width=width
        self.breath=breath
        
    def volume(self):
        return self.height * self.width * self.breath
    
    
r1=Room(10,5,7)
print(r1.volume())