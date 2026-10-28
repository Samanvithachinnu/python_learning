#ATM
import getpass
Balance  = 0
pin = (int(input("Set your PIN: ")))
if len(str(pin)) != 4:
    print("PIN must be 4 digits.")
    exit()
pin = getpass.getpass("Enter your PIN: ")
confirm = getpass.getpass("Confirm your PIN: ")
if pin != confirm:
    print("PINs do not match. TRY AGAIN")
    exit()
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is: ", Balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        Balance += amount
        print("Amount deposited successfully.")
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= Balance:
            Balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        while True == False:
            print("Exiting...")
            exit()
    else:
        print("Invalid choice. Please try again.")