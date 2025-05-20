
class BankAccount:
    def __init__(self, acc_holder,balance=0):
        self.account_holder = acc_holder
        self.__balance = balance
    # Deposit mate
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid Amount!")
    #withdraw mate
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully!")
        else:
            print("Insufficient Balance!")  

    #Check bakance mate
    def check_balance(self):
        print(f"Available Balance: {self.__balance}")
    
def main():
    print("\n Banking System ")
    name = input("Enter Account Holder Name: ")
    account = BankAccount(name)

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
            print("\nExited!")
            break
        
        else:
            print("\nInvalid choice. try again.")

main()


