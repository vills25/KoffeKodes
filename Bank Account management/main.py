
class BankAccount:
    def __init__(self, account_holder, account_type, balance=0):
        self.account_holder = account_holder
        self.account_type = account_type
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully!")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Available Balance: {self.__balance}")

    def display_details(self):
        return f"Account Holder: {self.account_holder}, Type: {self.account_type}, Balance: {self.__balance}"

def main():
    print("\n= Banking System =")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Savings/Current): ")
    
    account = BankAccount(name, acc_type)

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("\nChoose an option (1/2/3/4): ")
        
        if choice == '1':
            amount = float(input("Enter Amount to Deposit: "))
            account.deposit(amount)
        
        elif choice == '2':
            amount = float(input("Enter Amount to Withdraw: "))
            account.withdraw(amount)
            account.check_balance()

        elif choice == '3':
            account.check_balance()
        
        elif choice == '4':
            print("\nExiting...!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

# Run the application
main()


