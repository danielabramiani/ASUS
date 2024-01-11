class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

def main():
    # Example usage
    account1 = BankAccount(account_number=1, account_holder="John Doe")
    account2 = BankAccount(account_number=2, account_holder="Jane Doe", balance=1000)

    print("Initial balances:")
    print(f"Account {account1.account_number}: ${account1.get_balance()}")
    print(f"Account {account2.account_number}: ${account2.get_balance()}")

    account1.deposit(500)
    account2.withdraw(200)

    print("\nFinal balances:")
    print(f"Account {account1.account_number}: ${account1.get_balance()}")
    print(f"Account {account2.account_number}: ${account2.get_balance()}")

if __name__ == "__main__":
    main()