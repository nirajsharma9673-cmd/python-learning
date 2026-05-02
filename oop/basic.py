class Student :  #creating a class it name always started with capital letter
    name = " niraj sharma"
    division = "c"

s1 = Student() # it creating a object (instance)
print(s1)
print(s1.name)

del s1 # deliting object etc .

s2 = Student()
s2.name = input( "enter your name :")
s2.division = "c"
del s2.name
print(Student())
print(s2.name)
print(s2.division)
