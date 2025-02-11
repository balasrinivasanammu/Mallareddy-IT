class ATM:
    def __init__(self):
        self.balance = 0
        self.free_transactions = 3  # Maximum free transactions per month
        self.transaction_count = 0  # Count of transactions for the month
        self.transaction_fee_percentage = 2  # Fee percentage for extra transactions

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_count += 1
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.transaction_count < self.free_transactions:
                if amount <= self.balance:
                    self.balance -= amount
                    self.transaction_count += 1
                    print(f"Withdrawn: ${amount:.2f}")
                else:
                    print("Insufficient funds!")
            else:
                fee = (self.transaction_fee_percentage / 100) * amount
                total_deduction = amount + fee
                if total_deduction <= self.balance:
                    self.balance -= total_deduction
                    self.transaction_count += 1
                    print(f"Withdrawn: ${amount:.2f} with a fee of ${fee:.2f}")
                else:
                    print("Insufficient funds to cover transaction and fee!")
        else:
            print("Please enter a valid amount.")
    
    def remaining_free_transactions(self):
        return self.free_transactions - self.transaction_count

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        # After each transaction, show the number of free transactions left for the month
        print(f"Free transactions left this month: {atm.remaining_free_transactions()}")

if __name__ == "__main__":
    main()
