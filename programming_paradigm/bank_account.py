# bank_account.py

class BankAccount:
    """
    A simple BankAccount class to encapsulate banking operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance with an optional initial balance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.
        """
        # Ensure initial_balance is a non-negative number
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.account_balance += amount
        # No print statements here, as main-0.py handles the output based on its requirements

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
