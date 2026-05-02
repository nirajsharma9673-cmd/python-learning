"""hiii this is my second day of learning python frojm apna college 
and i have learned about sum , division ,multiplication , reminder and comment"""

#su of two number
num1 = 26
num2 = 56
print("the sum of two number is :", num1 +num2)

#substraction of two number
print("the substraction of two number is :", num1 -num2)
#division of two number
print("the divison of two number is :", num1 /num2)

# in reminder if denominator is negative then the result is negative 
print("the reminder of two number is :", num1 %num2)
print("the reminder of two number is :", num1 % -num2)

# integer division done by //
# the value ininteger divison is in integer then its convert in float \
# and it always take lesser value than the actual value
print("the integer division of two number is :", num1 //num2)
print("the integer division of two number is :", num1 // -num2)

# we can add string to sting with the help of + operator but we cannot add string to number
str1 = "hello"
str2 = "world"
num3 = 5
num4 = "7"
print((num4+str1 + str2)*num3)
# we can also multiply string with the number but we cannot multiply string with string
print(2*str1*7 )

# in put in python
name = input("enter your name:")
age = int (input("enter your age:"))
fee = float(input("enter your tution fess :"))
college = input ("enter your collage name :")
print("your name is :", name)
print("your age is :", age)
print("your tuition fee is :", fee)
print("your college name is :",college)
"""
#about operators :

#1. arithmetic operator : + , - , * , / , % , // , **

 #| Operator | Meaning             |
 # | -------- | ------------------- |
#|   `+`      | add                 |
#| `-`      | minus               |
#| `*`      | multiply            |
#| `/`      | divide              |
#| `%`      | remainder           |
#| `**`     | power               |
#| `//`     | whole part division |
 
 #2. assignment operator : = , += , -= , *= , /= , %= , //= , **=
| Operator | Meaning |
| -------- | ------- |
| `=` | assign |
| `+=` |add and assign |
| `-=` | subtract and assign |
| `*=` | multiply andassign | 
| `/=` | divide and assign |
| `%=` | remainder and assign |
| `//=` | whole part division and assign |
| `**=` | power and assign | 
 
 
#3. comparison operator : == , != , > , < , >= , <= 
 
1.  == (Equal to)

Matlab →
dono values same hain ya nahi

2. != (Not equal to)

Matlab →
dono values different hain ya nahi

3. > (Greater than)

Matlab →
left side wali value badi hai ya nahi

4.< (Less than)

Matlab →
left side wali value chhoti hai ya nahi

5. >= (Greater than or equal to)
 Matlab → left side wali value badi hai ya barabar hai ya nahi

6. <= (Less than or equal to) 
Matlab → left side wali value chhoti hai ya barabar hai ya nahi




#4. logical operator : and , or , not 
 
 1. and operator

👉 Matlab
dono condition True honi chahiye

a = 10

print(a > 5 and a < 20)


Output:

True

2. or operator
 👉 Matlab koi bhi ek condition True honi chahiye 
 a = 10 print(a > 5 or a < 20) 
 Output: True 
 
 3. not operator 
 👉 Matlab condition ka opposite hoga 
 a = 10 print(not(a > 5 and a < 20)) 
 Output: False


#5. bitwise operator : & , | , ^ , ~ , << , >> 
 
 1. & (Bitwise AND)

👉 Rule
dono bit 1 ho → result 1
warna → 0

Example:

a = 5
b = 3

print(a & b)


Binary:

5 → 101
3 → 011
---------
    001


Output:

1

2. | (Bitwise OR)
👉 Rule
dono bit me se koi bhi 1 ho → result 1
warna → 0

Example:

a = 5
b = 3

print(a | b)


Binary:

5 → 101
3 → 011
---------
    111


Output:

7
3. ^ (Bitwise XOR)

👉 Rule
dono different ho → 1
dono same ho → 0

Example:

a = 5
b = 3

print(a ^ b)


Binary:

101
011
---
110



Output:

6
~ (Bitwise NOT)

👉 Ye number ke bits ko ulta kar deta hai.

Example:

a = 5
print(~a)


Output:

-6


⚠️ Ye thoda confusing hota hai beginners ke liye,
kyunki Python internally negative numbers ko alag tarike se store karta hai.

📌 Yaad rakhne wali line:

~x = -(x+1)


So:

~5 = -(5+1) = -6

✅ 5. << (Left Shift)

👉 Bits ko left side shift karta hai.

Example:

a = 5
print(a << 1)


Binary:

5  → 101
<<1 → 1010


Output:

10


📌 Simple rule

x << 1  =  x * 2


Another:

print(5 << 2)


Output:

20


(5 × 4)

✅ 6. >> (Right Shift)

👉 Bits ko right side shift karta hai.

Example:

a = 5
print(a >> 1)


Binary:

101 → 10


Output:

2


📌 Simple rule

x >> 1 = x // 2


#6. identity operator : is , is not 
 
 1. is operator

👉 Matlab
dono same object hain kya?

Example:

a = [1, 2, 3]
b = a

print(a is b)


Output:

True


👉 kyunki

b = a

dono ek hi list object ko point kar rahe hain

2. is not operator
 👉 Matlab dono same object nahi hain kya?
  
    Example: a = [1, 2, 3] b = [1, 2, 3] 
    print(a is not b)
     
     Output: True 
     👉 kyunki a aur b alag alag list object hain jo same values rakhte hain lekin woh same object nahi hain.

     👉 is
= dono ka address same hai?

👉 ==
= dono ki value same hai?


 #7. membership operator : in , not in
 
 1. in operator

👉 Matlab
ye value andar present hai kya?

Example (list):

nums = [10, 20, 30, 40]

print(20 in nums)


Output:

True


👉 kyunki 20 list ke andar hai.

2. not in operator 
👉 Matlab ye value andar present nahi hai kya?

 Example (list): nums = [10, 20, 30, 40]
 print(50 not in nums) 

Output: True 

👉 kyunki 50 list ke andar nahi hai.
"""
