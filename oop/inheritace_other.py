# INHERITANCE IS THRID PILLAR OF OOPS 
# which is one class give/pass the properties and method to another class

class Car :
    def __init__(self, colour) :
        self.colour = colour
        print(self.colour)

    @staticmethod
    def start() :
        print("the car is started")

    @staticmethod 
    def stop() :
        print("the car has stopped ")


# 1. single inheritance (it is that what we have done it above) like one parent and one child
class Toyotacar(Car) : # we passed the proprties or method to toyota car
    def __init__(self, name , colour ) :
        self.name = name 
        super().__init__(colour)   # super method (it is use to acsess the method of parent class )


car1 = Toyotacar("fortuner","blue")

car2 = Toyotacar("supra","black") 

print(car1.name)
car1.start() # due to inheritance we can acses the method of Car
car1.stop()


# 2. multi level inheritance
class Suzukicar(Car) : # we passed the proprties or method to toyota car
    def __init__(self, brand , colour ) :
        self.brand = brand
        super().__init__(colour)

class Wagoner(Suzukicar) : # its like car --> suzukicar --> wagnoer (we can acses all of them)
    def __init__(self , type , brand , colour):
        self.type = type
        super().__init__(brand , colour)

scar1 = Suzukicar("maruti","white")
scar2 = Wagoner("petrol","suzuki","red")

print(scar1.brand)
print(scar2.type)

scar1.start()
scar2.stop() # it is called as multilevel inheritence


# 3.multiple inheritance (its like passinsg two three parent into child)
class multi(Car,Suzukicar) :
    def __init__(self, colour , brand):
        Car.__init__(self, colour)
        Suzukicar.__init__(self, brand , colour)
        print("hii its multiple inheritence")

m = multi("black","bmw")
m1 = Suzukicar("bmw","grey")

print(m1.brand)

m.start()
m.stop()