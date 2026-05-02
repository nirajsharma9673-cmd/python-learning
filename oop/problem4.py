"""define a employee class with attribute
role, department & salary. this class also has the show detail method
create an engineer class that inherits propeties from employee & has 
additional attribute :name &age"""

class Employee :
    def __init__(self, role , department, salary) :
        self.role = role
        self.department = department
        self.salary = salary
    def showdetails(self) :
        print("role :", self.role)
        print("department :", self.department)
        print("salary :", self.salary)

class Engineer(Employee) :
    def __init__(self, name , age) :
        self.name = name 
        self.age = age
        super().__init__("engineer", "IT", 50000.652)
       
en1 = Engineer("rakesh", 29)
print(en1.name)
print(en1.age)
en1.showdetails()


