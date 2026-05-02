#theory of string 
str1 =  'hello world'
str2 = "hello world "
str3 = """hello world """

str4 = "hello world's "
str5 = 'hello world"s'

print(str1+str2)
print (str1+""+str2) # we also calculated the space 

print(len(str1)) # for lenth of the string
#slicing 
n = "i am unable to speak "
print(n[0])
print (n[0:4])  # it deosnt print the element , and indexing always start from 0

print (n[0:len(n)])
print (n[0 : -1]) # - indexing start from last , form -1 to - 85 it is useful in machine learning 

# function 

m = "i am unable to speak"
print(m.capitalize()) # it doesnt change the mane value 

#m = m.capatilize()  # it affect one main valu , and chanmged

print (m.endswith("eak")) # to check the string ending , if it is then print true or false 

print(m.replace("a","o"))
print(m.find("a")) # it shows the first index of world or letter 
print(m.count("n")) # it count how many times a word or charcter is present in the string 

#escape sequence character 
a= "your unable to speak .\nand also i am ." # for printing next line 
b= "it's a wonderfull night\tand it is the one of the best moon of night's" # for tab spacing 


