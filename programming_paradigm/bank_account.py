class BankAccount:
    def __init__(self, account_balance=0):
        if not(account_balance, (int, float)) or account_balance < 0:
            raise ValueError("Initial balance should be a positive number")
        self.account_balance = account_balance

# e33ml ininstance w eno yb2a positive a kbr mn zero, b3den shof el withdraw wel deposit 
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount

    def withdraw(self, amount):
        if amount >= self.account_balance:
            self.account_balance = self.account_balance - amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
