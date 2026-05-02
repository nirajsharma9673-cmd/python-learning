# it is a __init__ function  which is also called as constructor if we dont create then python creates automatically
class Student : 
    def __init__(self) :# its a constructor , we have to give at least one parameter and we can give multiple parameter 
        print(self)
        name = "niraj"
        print("adding a new student ....")

s1 = Student() # if we dont create a constructor then it creates automatically like the () in student
print(s1)  # both are same slf and s1

class Car :
    cont = "japan" #class.attribute
    #default constructor
    def __init__(self) :
        print("it is default constructor")
    #parametarized consructor 
    def __init__(self, fullname , year , rating ) :
        self.name = fullname  # the variable or data in the  class is called as atrribute
        self.year = year #its a object/instance attribute
        self.rating = rating
        print("new car is adding ....")
# if you have two constructor then it choose which matches the parameters
    def greet(self) : #it a method 
        print("welcome at showroom of " , self.name)

    def rate(self) : #it is method
        print("ratings for your car" , self.rating)
    
    @staticmethod # it is decorator which is used show its static method
    def welcome() : # static method (it works at class level ) ,, its basically it input as function and chnge the behaviour then gives output as function
        print("welcome to  explore so many cars")
Car.welcome() # we can can out side the object or inside object because its work as class level
c1 = Car("toyota", 1997 ,9.5)
c1.greet()
print(c1.name)
print(c1.year)
print(Car.cont)
c1.rate()
c2 = Car("kawasaki ninja" , 1987 , 9.8)   
c2.greet()
print(c2.name )
print(c2.year)
print(Car.cont)
c2.rate()

# the pillar of oop we can say (4)
#1. abstraction : it like hiding implentation  and what is require that to show user , like whe we start a car it start but car doesnt show the process how it start
#2. enscapulation : its like wraping data and function in the single object (its basically what we have done on upper code)

