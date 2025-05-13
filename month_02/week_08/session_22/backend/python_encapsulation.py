class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balnce =balance
        self.__account_number = "123"


    def deposit(self, amount):
        if amount >0:
            self.balnce+=amount
            return True
        return False
    

    def witdhraw(self,amount):
        if 0< amount<= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance


account =BankAccount("John" ,1000)
print(account.owner)
print(account._balance)
print(account._BankAccount__account_number)