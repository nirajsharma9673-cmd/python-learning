def print_list(list, ind =0) :
     if ind == len(list) :
        return
     print (list[ind])
     print_list(list, ind+1)
fruit = [4,5,6,5,4,5,5]
print_list(fruit)