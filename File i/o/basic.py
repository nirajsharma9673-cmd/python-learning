file = openfile = open("C:/Users/niraj/python learning/File i/o/intorduction.txt", "r") #first for the file name with their type and the next one is mod  like read , write like this
data = file.read()# u can  pass the argument in thi if you put 5 then only 5 character will be printed 
print(data) 
print(type(data))
file.close()  # after open always remeber to close the file 


file2 = openfile = open(r"C:\Users\niraj\python learning\File i\o\mode.txt" , "r")
data2 = file2.readline() # if we want to write only onen line we have to write , then we can use readlin() function , in this we csn pass the argumnets to print multiple line 
print(data2) 
print(type(data2))
file2.close()  # after open always remeber to close the file 
