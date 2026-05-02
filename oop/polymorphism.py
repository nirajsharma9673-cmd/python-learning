#polymorphism : operator overloading (it is a 4th pillar of oops)
#poly(many)-morphism(forms)
# when the same oprator has deffrent meaning as per context like
#print(1+2) # it normally add 
#print("niraj" + "sharma") # its a string it cant br add so basically its context change and "concatenate"
#print([1,2,3] + [4,5,6]) # it merge 

#in plymorphism we do the exact thing for class
class Complex :
    def __init__(self , real, img) :
        self.real = real
        self.img = img
    
    def shownumber(self) :
        print(self.real, "i +" , self.img ,"j" )
    
    def __add__(self, num2) : #dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal ,newImg)
    def __sub__(self, num2) :#dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal ,newImg)
    def __mul__(self, num2) :#dunder function
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return Complex(newReal ,newImg)
    def __truediv__(self, num2) :#dunder function
        newReal = self.real / num2.real
        newImg = self.img / num2.img
        return Complex(newReal ,newImg)  
    def __mod__(self, num2) :#dunder function
        newReal = self.real % num2.real
        newImg = self.img % num2.img
        return Complex(newReal ,newImg)  
num1 = Complex(1,5)
num1.shownumber()

num2 = Complex(8,5)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()

num5 = num1 * num2
num5.shownumber()

num6 = num1 / num2
num6.shownumber()

num7 = num1 % num2
num7.shownumber()