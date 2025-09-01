# --- Analysis and Explanation ---

# The BankAccount class models a simple bank account.
# - The constructor (__init__) allows setting an initial balance, defaulting to 0.
# - The deposit method adds a positive amount to the balance and prints a confirmation.
#   It checks that the deposit amount is positive.
# - The withdraw method subtracts a positive amount from the balance if there are sufficient funds.
#   It checks for both positive input and sufficient balance, printing appropriate messages.
# - The balance method returns the current balance.
# The class uses a private attribute (_balance) to store the account balance, following Python's naming convention for "protected" members.
# This class can be extended with more features such as transaction history, interest calculation, etc.

# Example usage:
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# print("Current balance:", account.balance())
class BankAccount:
    def __init__(self, name, balance=0):
        """
        Initialize the BankAccount with account holder's name and initial balance.
        :param name: The name of the account holder.
        :param balance: The initial balance (default is 0).
        """
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        :param amount: The amount to deposit (must be positive).
        :return: None
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a positive amount from the account if sufficient funds exist.
        :param amount: The amount to withdraw (must be positive and <= balance).
        :return: None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            print(f"Withdrew: {amount}")

    def balance(self):
        """
        Return the current balance of the account.
        :return: The account balance.
        """
        return self._balance

# Example usage:
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"{account.name}'s Current balance:", account.balance())
