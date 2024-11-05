class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

# Demonstrate encapsulation
account = BankAccount()
account.deposit(100)
account.withdraw(50)
