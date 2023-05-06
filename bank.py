

class Account:
    account ="branch"

    def __init__(self,account_number,account_name,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        print (f"{self.account_name} whose account number is {self.account_number} has a balance of {self.balance}")


    def withdraw(self):
        print(f"{self.account_name} has withdrawn 2000 ")    


    def freezed(self) :
        print(f"{self.account_number} under {self.account_name} has been freezed no transactions can be made")


bank=Account("1223edEBF","Michael Jane",200000)  

bank.deposit()
bank.withdraw()
bank.freezed()


      
