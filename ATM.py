class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self):
        attempts = 3
        while attempts > 0:
            user_pin = input("Enter your PIN: ")
            if user_pin == self.pin:
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("You have entered an incorrect PIN 3 times. Exiting.")
        return False

    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance}")

    def cash_withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Transaction successful! You withdrew ${amount}")
        else:
            print("Insufficient balance.")

    def cash_deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        print(f"Transaction successful! You deposited ${amount}")

    def change_pin(self):
        new_pin = input("Enter your new PIN: ")
        confirm_new_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_new_pin:
            self.pin = new_pin
            print("PIN change successful!")
        else:
            print("PINs do not match. Try again.")

    def print_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

def main():
    atm = ATM(balance=1000)  # Initial balance is $1000 for testing

    if not atm.check_pin():
        return

    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            atm.balance_inquiry()
        elif choice == "2":
            atm.cash_withdrawal()
        elif choice == "3":
            atm.cash_deposit()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.print_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
