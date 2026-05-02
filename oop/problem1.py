class Student :
    def __init__ (self , name ,marks ) :
        self.name = name 
        self.marks = marks
    def avg(self) :
        sum =0
        for values in self.marks :
            sum += values
        avg = sum / len(self.marks)
        print("the avrage mark of student",avg)

s1 = Student("karan",[10,20,30])
print(s1.name)
s1.avg()

s2 = Student("rahul",[40,20,30])
print(s2.name)
s2.avg()

s3 = Student("dev",[80,20,30])
print(s3.name)
s3.avg()