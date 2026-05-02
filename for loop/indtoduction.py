# itn is used for sequential iteration 
num = [5,6,6,9,5,4,5,5]
for value in num :
    print(value) #we can use as well as in tuple 
index = 0
for value in num :
    print(value, index)
    index +=1

# one more thing in for loop it called as else , it is run after completing a looop , it used in if break is applicable , if you want to run after the looop completely ends

for el in num :
    print(el)
else : 
    print("the loop ended")

for ele in num :
    print(ele)
    if (ele ==9):
        print("the 9 is find")
        break
else : 
    print ("the loop ended")
