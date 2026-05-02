#sum
def add(*num1) :
    total = 0
    for i in num1 :
        total += i
    print("the sum of nunmber :",total)

#SUBSTRACT
def sub (a,b) :
    sub = a-b
    print("the substraction of number :" ,sub)
    

#product
def mult (*num3) :
    product = 1
    for j in num3 :
        product *= j
    print("the product of number :",product)

def div(a,b) :
    division = a/b
    print("the divison of number :", division )

creator = {"name" : "niraj sharma",
           "age" : 18,
            }