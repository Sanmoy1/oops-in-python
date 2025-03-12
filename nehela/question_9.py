class BankAccount:
    def __init__(self, account_holder, account_number, account_type, balance):
        # Initializing the attributes of the bank account
        self.account_holder = account_holder
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        # Deposit money into the account, ensure amount is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance:{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money, ensuring there is enough balance and minimum balance condition
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.balance - amount < 1000:
            print("Cannot withdraw. Balance should remain above 1000.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_account_info(self):
        # Display all the details of the account
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print("="*40)

# Creating 3 Bank Account objects and testing functionalities

account1 = BankAccount("Mahesh", "M12345", "Savings", 5000)
account1.deposit(1500)  # Depositing money
account1.withdraw(3000)  # Withdrawing money
account1.display_account_info()  # Display account info

account2 = BankAccount("Sanmoy", "A12345", "Current", 2000)
account2.deposit(2000)  # Depositing money
account2.withdraw(7500)  # Withdrawing money
account2.display_account_info()  # Display account info

account3 = BankAccount("Subham", "S12345", "Savings", 3000)
account3.deposit(500)  # Depositing money
account3.withdraw(000)  # Withdrawing money
account3.display_account_info()  # Display account info
