class Person :
    name = "unknown"

    def changename(self, name) :
        self.name = name  # but we use like Person.name / self.__class__.name then it changes directly into class
# a static method does not change the value of class or it doesnt effect to the class and it genrally use for utility
#thats why we class method it is bound to the class & recievs the class as an inplicit first argument . 
p1 = Person()
p1.changename("rakesh")
print(p1.name)
print(Person.name) # you will see it does not change the name of the class 

class Car : 
    name = "unknown"

    @classmethod
    def changename(cls, name) :
        cls.name = name 

Car1 = Car()
Car1.changename("toyota")
print(Car.name)     # after doing with class method it directly changes in class and changed the name 