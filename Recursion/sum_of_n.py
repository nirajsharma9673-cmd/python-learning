# craete a recusive function to calculate the sum of n numbers
def sum(num) :
    if(num == 0 ) :
        return 0
    return sum(num-1) + num

print(sum(5))