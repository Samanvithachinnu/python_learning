import random
import string

# Get password length from the user
length = int(input("Enter password length: "))

# Define characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

# Generate random password
password = ''.join(random.choice(all_characters) for i in range(length))

# Display password
print("Generated Password:", password)

# ATM System in Python

balance = 5000
correct_pin = "1234"

pin = input("Enter your ATM PIN: ")

if pin == correct_pin:
    print("\nWelcome to ATM!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is Rs.", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: Rs. "))

            if amount > 0:
                balance += amount
                print("Money deposited successfully!")
                print("Updated balance: Rs.", balance)
            else:
                print("Enter a valid amount!")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: Rs. "))

            if amount <= 0:
                print("Enter a valid amount!")
            elif amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance: Rs.", balance)
            else:
                print("Insufficient balance!")

        elif choice == "4":
            old_pin = input("Enter your current PIN: ")

            if old_pin == correct_pin:
                new_pin = input("Enter your new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    correct_pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN!")

        elif choice == "5":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect ATM PIN!")