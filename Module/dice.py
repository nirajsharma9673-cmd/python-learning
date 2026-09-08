import random as r 
print("Spin the dice")
print("for spin enter y , if don't then enter n")
n = input("enter :")
if n =='y':
    print(r.randint(1,6))
elif n=='n':
    print("-----")
else :
    print("invalid")
