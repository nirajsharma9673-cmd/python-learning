#create aaccount class with 2 attribute - blance & account no. create method for a debit , credit, & printing the balance 
class Account :
    def __init__(self, bal, acc) :
        self.balance = bal
        self.account = acc
    def debit(self, amount) :
        self.balance -= amount
        print(amount , "rs debited")
    def credit(self, amount) :
        self.balance += amount
        print(amount , "rs credited")
    def show(self) :
        print("your total balance :", self.balance)

trans1 = Account(10000.50 , 1800321)
print("your account number :" ,trans1.account)
print("total balance :", trans1.balance)
trans1.debit(2000.50)
trans1.show()

trans2 = Account(45002.50 , 456852)
print("your account number :" ,trans2.account)
print("total balance :", trans2.balance)
trans2.credit(4585.50)
trans2.show()


