#define a circle class with a radius r using constructor 
#define an Area(method) of the class which calculates the area of the circle
#perimeter() method of the class which allows which allows to calculate the perimeter of the circle

class Circle :
    def __init__(self, radius) :
        self.radius = radius
    
    def area(self) :
        return ((22/7) * (self.radius **2))
    
    def perimeter(self) :
        return   (2 * (22/7) * self.radius)
    
c = Circle(1.56)
print("the area of the circle : ", c.area() )
print("the perimeter of circle", c.perimeter())
