import random as r

x = r.random() # it genrates random number between 0 to 1
print(x)    

print(r.randint(1,100)) # itn gives one random numbers between value1,value2
# rnadint - random + integer 
# it can also gives values as output , becuase it consider them 

print(r.randrange(1,5)) 
#it generates a random integer from 1 to 9. 
# the last number is not included 
# you can also give steps (start , stop(excluded), step)

fruits = ["Apple", "Mango", "Banana", "Orange"]
print(r.choice(fruits))
# it used to select randomly from a collection 
# we can also choose from string

print(r.choices(fruits)) # it select multiple elemnets in collection
# here k =1 (default) , it choose 3 three element , we can change the number of selection
print(r.choices(fruits, k=3)) # also repetition is allowed

print(r.sample(fruits,k =4)) # it simillar to choices 
# in this repitition is not allowed 
# we can avoid writing k

r.shuffle(fruits)
print("before shuffle : ",fruits )
print("after shuffle : ",fruits)
# it just shuffles the elements of the collection
# and it chnges the original list
# we can't stores the shuffle because it returns None

#uniform() is used to generate a random decimal (float) number between two values.
print(r.uniform(1,56))

#problem when we genrate random numbers it changes every time after run
# but seed with the help of seed we solve that
r.seed(10)
#why does this happen
#Think of seed() as setting the starting point for the random number generator.
'''seed(10)
   ↓
Starting point is fixed
   ↓
Random sequence is generated
   ↓
Same starting point
   ↓
Same sequence

Why is seed() useful?

It's especially useful for:

Testing programs
Debugging
Machine learning
Data analysis
Experiments

For example, 
if you're testing a program that uses random numbers,
 you may want the same random data every time so you can compare results.'''





