#print he value of tuple
t =(1,1,2,4,1,14,4,5,1,45,1,4,45)
i = 0
x=45
while i<(len(t)) :
    if x == t[i] :
        print("found", i)
    i += 1
    
print("loop ended")