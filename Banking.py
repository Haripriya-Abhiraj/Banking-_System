class Bank:
    def __init__(self):
     self.balance = 0
     print("Welcome ! The account is created")


    def deposit(self):
        amount=float(input("Enter to be deposited: "))
        self.balance=self.balance+amount
        print("Deposit is successful and the balace in the account is %f" % self.balance)
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if(self.balance>=amount):
           self.balance=self.balance-amount
           print("The withdraw is successful and balance is %f" % self.balance)
        else  :
            print("Insuficient Balance: ")
    def enquiry(self):
        print("Balance in the account is %f" % self.balance)

acc=Bank()
acc.deposit()
acc.withdraw()
acc.enquiry()