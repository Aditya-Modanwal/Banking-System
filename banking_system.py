import random
import math
from datetime import datetime

accounts = {}

def generate_account_number():
    while True:
        acc_number = str(random.randint(1000000000,9999999999))
        if acc_number not in accounts:
            return acc_number

def create_account():
    print("\n---Create Account---")

    name = input("Enter your name: ").strip().title()
    clean = name.replace(" ","").replace("-","").replace("'","")
    if not clean.isalpha():
        print("Name can only contain letters, spaces, hyphens (-) and apostrophes (').")
        return
    
    phone = input("Enter your phone number: ").strip()
    if len(phone) != 10 or not phone.isdigit():
        print("Invalid phone number. It must be exactly 10 digits")
        return 
    
    pin = input("Create a 4-digit PIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid pin number. It must be exactly 4 digits")
        return 
    
    confirm_pin = input("Confirm your PIN: ").strip()
    if pin != confirm_pin:
        print("PINs do not match. Account not created")
        return 

    acc_number = generate_account_number()
    accounts[acc_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "history": [] }

    print("Account created successfully!")
    print("Your account number ", acc_number)

def login():
    acc_no = input("Enter your account number: ").strip()
    
    pin = input("Enter your PIN: ").strip()
    if acc_no in accounts and pin == accounts[acc_no]['pin']:
        print('Welcome',accounts[acc_no]["name"])
        return acc_no
    else:
        print("Invalid account number or PIN")
        return

def check_balance(acc_no):
    print("Your balance is ",accounts[acc_no]['balance'],"Rs.")



def read_amount(prompt):
    while True:
        text  =  input(prompt).strip()
        try:
            amount = float(text) 
            amount = round(amount,2)
            if not math.isfinite(amount):
                print("Invalid amount.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        if amount<=0:
            print("Amount must be greater than zero")
            continue

        return amount

def withdraw(acc_no):
    amount = read_amount("Enter the amount to withdraw: ")
    if accounts[acc_no]['balance'] >= amount:
        accounts[acc_no]['balance']  = round(accounts[acc_no]['balance'] - amount , 2)
        print("Amount ",amount,"Rs withdrawn successfully. Remaining balance ", accounts[acc_no]['balance'],"Rs")
        add_transaction(acc_no, "Withdrawal", amount)
    else:
        print("Insufficient Balance!")
        

def deposit(acc_no):
    amount = read_amount("Enter the amount to deposit: ")

    accounts[acc_no]["balance"] = round(accounts[acc_no]['balance'] + amount , 2)
    print("Amount ",amount,"Rs deposited successfully. Total balance ", accounts[acc_no]['balance'],"Rs")

    add_transaction(acc_no, "Deposit", amount)


def transfer(acc_no):
    receiver = input("Enter the account number of receiver: ").strip()

    #checking receiver is exist or not same
    if receiver not in accounts :
        print("Invalid Account Number!")
        return

    elif receiver == acc_no:
        print("You cannot transfer to your own account.")
        return
    
    print("receiver's name is ",accounts[receiver]['name'])

    #taking amt to transfer
    amount = read_amount('Enter amount to transfer: ')

    #checking balance of sender
    if amount>accounts[acc_no]["balance"]:
        print("Insufficient Balance!")
        return
    
    #taking money from sender
    accounts[acc_no]["balance"] = round(accounts[acc_no]['balance'] - amount , 2)

    #giving to receiver
    accounts[receiver]["balance"] = round(accounts[receiver]['balance'] + amount , 2)

    add_transaction(acc_no, "Transfer Sent", amount, "To " + receiver)
    add_transaction(receiver, "Transfer Received", amount, "From " + acc_no)

    print(" Successfully transferred.")


def add_transaction(acc_no, kind, amount, note=""):
    accounts[acc_no]["history"].append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "type": kind,
        "amount": amount,
        "balance_after": accounts[acc_no]["balance"],
        "note": note
    })

def transaction_history(acc_no):
    history = accounts[acc_no]["history"]
    print("\n--- TRANSACTION HISTORY ---")

    if not history:
        print("No transactions yet.")
        return

    print(f"{'Date & Time':<20} {'Type':<18} {'Amount':>10} {'Balance':>12}  Note")
    print("-" * 75)
    for t in history:
        print(f"{t['time']:<20} {t['type']:<18} {t['amount']:>10.2f} {t['balance_after']:>12.2f}  {t['note']}")


def change_pin(acc_no):
    old_pin = input("Enter your old PIN: ").strip()

    if old_pin != accounts[acc_no]['pin']:
        print("Incorrect old PIN!")
        return
    
    new_pin = input("Enter new 4-digit PIN: ").strip()

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Invalid pin number. It must be exactly 4 digits")
        return 
        
    confirm_pin = input("Confirm your PIN: ").strip()
    if new_pin != confirm_pin:
            print("New PINs do not match. PIN not changed.")
            return
    accounts[acc_no]['pin'] = new_pin
    print("PIN changed successfully.")

def account_menu(acc_no):
    while True:
        print('''
                 -----------------------------------
                 |        ACCOUNT MENU             |
                 -----------------------------------
                 | 1. Check Balance                |
                 | 2. Deposit                      | 
                 | 3. Withdraw                     |
                 | 4. Transfer                     |
                 | 5. Transaction History          |
                 | 6. Change PIN                   |
                 | 7. Logout                       |
                 -----------------------------------
                 ''')
        choice = input("Enter Choice: ").strip()

        if choice == '1':
            check_balance(acc_no)

        elif choice == "2":
            deposit(acc_no)
        elif choice == "3":
            withdraw(acc_no)
        elif choice == "4":
            transfer(acc_no)
        elif choice == "5":
            transaction_history(acc_no)  
        elif choice == "6":
            change_pin(acc_no)            
        elif choice == "7":
            print("Logged out successfully!")
            break
        else:
            print("Invalid Choice!")


def main():
    while True:
        print('''
                ____________________________
                |        MAIN MENU         |
                |--------------------------|
                | 1. Create Account        |
                | 2. Login                 |
                | 3. Exit                  |
                |__________________________|
                ''')
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_account()
        elif choice == '2':
            acc = login()
            if acc:
                account_menu(acc)
        
        elif choice == '3':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()