#it is used to make use the mthod as a property
class Student :
    def __init__(self , chem , phy , math) :
        self.chem = chem
        self.phy = phy
        self.math = math
        #self.percentage = str((self.chem + self.phy + self.math)/3) + "%" (we have to create prperty of these so its work like attribute)
    @property
    def percentage (self) :
        return str((self.chem + self.phy + self.math)/3)
rakesh =  Student(45,56,45)       
print(rakesh.percentage)

rakesh.phy = (98) #(in normal method)if we change the value in this it chnages the value but it doesnet affect on percentage it doesnt change 
print(rakesh.percentage) # after changing into property its chnage the percentage

