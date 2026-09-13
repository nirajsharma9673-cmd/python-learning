import os  # it works on  underlying operating system
'''The os module in Python provides a way to interact with the
operating system, allowing you to perform system-level tasks such as
file and directory manipulation,
environment variable management,
and process handling.
It acts as an interface between your Python script and the
underlying operating system, providing functionality that is portable
across different operating systems like Windows, macOS, and Linux.'''

# print(dir(os)) it gives list function we can use or directory

print(os.getcwd()) # current working directory

# to chnage directory 
# os.chdir('C:\\') it will change the directory
os .rmdir("new project ")
os .mkdir("new project ")  # it will create new folder in cwd

#os.makedirs(one/two) # it will create 2 or more dirctorys

os.rmdir("new project ") # it will remove the folder
# os.removedirs("one/two")
# os.remove()
# os.rename 

os.listdir() # it will gives list of directories of path provided by user

os.listdrives() # it will gives list of drives

var =os.walk(os.getcwd()) # it lits out folder and inside of that folder
print (var)
for i in var :
    print(i)


 
s = os.stat("Module") # it gives the stats of that file : like chnages or something

print(s)
print(s.st_size)

# environment variable
#print(os.system('ls')) it will give error 
print(os.system('dir'))

print(os.environ)
# os.getenv()

print(os.name)