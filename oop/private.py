class greet :
    function = "greet people "
    def __init__(self , name ) :
        self.name = name 
        self.__secret = "This is a private attribute"  # Private attribute
    def __name(self) : #  __ it is use to create private method or attribute , it can only accesable under class , but we cant call this outside

        print("what's your name ?:")
    def welcome(self , name ) : # but you can call private method to another method under class
        self.__name()
        print("welcome to the shop ", name )

costmer = greet("Niraj")
costmer.welcome("niraj")
print(costmer._greet__secret)  # Accessing private attribute outside the class
