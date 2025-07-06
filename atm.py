class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully! New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully! Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


def main():
    print("Welcome to the Bank Account Management System!")
    name = input("Enter your name to create an account: ")
    account = BankAccount(name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter the amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            print("Thank you for using the Bank Account Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()