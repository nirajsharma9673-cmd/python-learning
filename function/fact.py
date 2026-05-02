def fact(a) :
    factorial = 1
    for items in range (1,a+1) :
        factorial *= items
    print("the factorial of ", num , "is :", factorial )        

num = int(input("enter the number for factorial "))
fact(num)


