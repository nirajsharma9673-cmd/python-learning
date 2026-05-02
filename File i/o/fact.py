# if you open that file for write and append if this fle is not exist then they will create a new file for you
file = openfile = open("new_append", "w")
data = file.write("\nthis is created by write function") 
print(data) 
print(type(data))
file.close()  # it is also same happen if you do with append function
