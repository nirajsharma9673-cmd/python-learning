#create a class called order which stores item & its price use dunder function
#__gt__() to coney that order1>order two

class Order :
    def __init__(self , item, price) :
        self.item = item
        self.price = price
    def __gt__(self , order_2) :
        return  self.price > order_2.price
    
order_1 = Order("apple" , 20.02)
order_2 = Order("orange", 25.23)

print(order_1 < order_2)