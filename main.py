class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print('Deposit successful.')

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print('Withdrawal successful.')
        else:
            print('Insufficient balance.')

    def get_balance(self):
        return self.__balance


# Creating an instance of BankAccount.
account = BankAccount('123456789', 5000)

# Accessing and modifying balance using methods.
print('Initial balance:', account.get_balance())
account.deposit(50000)
account.withdraw(1000)
print('Current balance:', account.get_balance())
