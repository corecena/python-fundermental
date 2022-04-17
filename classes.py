class Point:
    # magical methods are methods that start with __ and end __ they are called automatically by the compiler
    #  the __init__(self) function  is the main constructor executed when creatng an object
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #self is a reference to the current object 
    #defining a class method 
    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"Point  ({self.x} , {self.y})")
# creating an object of type Point
point = Point.zero()
point.draw()
print(type(point))