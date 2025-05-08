class BankAccount:
    def __init__(self, owner, balnce=0):
        self.owner = owner
        self.balance = balnce
        self._account_number="12345"


account = BankAccount("John")
print(account.owner)
print(account.balance)
print(account._BankAccount__account_number)
        