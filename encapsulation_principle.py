class BankAccount:
    def __init__(self, account_number, balance):
        self.__acount_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise('Insufficent funds')
    
    def get_balance(self):
        return self.__balance

account = BankAccount("1245", 8000)

try:
    print(account.__acount_number)
except AttributeError as e:
    print("Attribute Error", e)

account.deposit(500)
print("Balance after deposit:", account.get_balance())