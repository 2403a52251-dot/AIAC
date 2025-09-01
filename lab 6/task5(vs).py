class bank_account:
    def __init__(self, account_number, account_holder, balance=0):
        # Initialize account number, account holder's name, and starting balance
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Add the deposit amount to the balance if it is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Subtract the withdrawal amount from the balance if sufficient funds exist
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Print and return the current balance
        print(f"Current balance: {self.balance}")
        return self.balance

# Example usage:
if __name__ == "__main__":
    acc = bank_account("123456", "Alice", 1000)
    acc.check_balance()      # Show initial balance
    acc.deposit(500)         # Deposit money
    acc.withdraw(200)        # Withdraw money
    acc.withdraw(2000)       # Try to withdraw more than balance
    acc.check_balance()