from math import *

# here we are going to see basic function of math  module

print(sqrt(4585)) # this shows the squre root of number

print(ceil(10.8)) # it returns the integer of next number like round off

print(fabs(-45)) # it returns absolute value

print(factorial(56)) # it gives factorial of number

print(floor(10.5)) # it gives integer value but it gives back value

print(pow(2,6)) # it gives power of any number

l =[5,6,8,6,9,8,4]

print(fsum(l)) # it sums list and tuple value

print(sin(30)) # it gives in degree 

print(cos(30))

print(log(25))

# for radian value 

print(sin(radians(30))) # 0.5 

print(cos(radians(60)))

print(trunc(-48.659)) # it reomves decimal parts

print(trunc(458.265))

print(gcd(10,20)) # it gives common divisor
# we can use multiple numbers 
print(gcd(5,65,625,95,85))
'''
   Factors of 12 = 1, 2, 3, 4, 6, 12
   Factors of 18 = 1, 2, 3, 6, 9, 18

   Greatest common divisor = 6
'''

# The least common multiple (LCM) is the smallest positive integer
#  that is divisible by two or more given numbers without a remainder

print(lcm(5,8)) # we can use multiple integer 

print(pi) # it gives pi value and also use in arthmetic operations

area = pi*5**2
print(area)


print(e) # euler's number

print(tau) # 2*pi

print(inf) # it represents infinity and can't use in comparison

print(nan) # it means not number 

print(log(5)) # natural log

print(log(5,2)) #log(x,base)

print(log10(585)) # you can change the base like log2()

# covert radians into degree
print(degrees(pi/2))

# degrees() → radians to degrees
# radians() → degrees to radians

print(tan(radians(45))) # tangent 

# inverse trignomatic
print(degrees(asin(0.5)))
print(degrees(acos(0.5)))
print(degrees(atan(1)))

print(isclose(0.2*0.2,0.25)) # it uses to compare floating point
# answers in True/False

#it checks number is finite or not
print(isfinite(100))
print(isfinite(float('inf')))

# it checks number is infinity or not
print(isinf(float('inf')))
print(isinf(100))

x = float('nan') # it checks nan value 
print(isnan(x))

# calculates combination
print(comb(3,6)) #3C6 , 3 choose 6

print(perm(5,6)) # for permuantation

print(prod(l)) # it gives product of list and tuple

# to find hypotenuse √(a² + b²)

print(hypot(3,4))