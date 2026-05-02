file = open(r"C:\Users\niraj\python learning\File i\o\problems\practise.txt", "r") 
data = file.read()
print (data)

new_data = data.replace("java", "pyhton")

file = open(r"C:\Users\niraj\python learning\File i\o\problems\practise.txt", "w") 
file.write(new_data)
