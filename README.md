# Banking System - Mini Project

A Python-based, menu-driven application that simulates basic banking operations. Users can create an account, log in securely with an account number and PIN, and perform common banking activities such as deposits, withdrawals and transfers.

## Features

- **Create account**: enter name, phone number and set a 4-digit PIN; a unique 10-digit account number is generated automatically
- **Login**: authenticate with account number and PIN
- **Check balance**: view the current account balance
- **Deposit**: add money to the account
- **Withdraw**: withdraw money after a balance check
- **Transfer**: send money to another account using the receiver's account number
- **Transaction history**: view deposits, withdrawals and transfers with date and time
- **Change PIN**: verify the old PIN, then set and confirm a new one
- **Logout**: end the session and return to the main menu

## Input Validation

- Name may contain only letters, spaces, hyphens and apostrophes
- Phone number must be exactly 10 digits
- PIN must be exactly 4 digits and is confirmed twice
- Amounts must be valid numbers greater than zero
- Withdrawals and transfers are blocked if the balance is insufficient
- Transfers to your own account or to a non-existent account are rejected
- Login shows a single generic error message so it does not reveal which part was wrong

## Python Concepts Used

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- String operations
- Modules: `random` (account number generation) and `datetime` (transaction timestamps)

## Program Flow

```
MAIN MENU (Create Account / Login / Exit)
        |
      LOGIN
        |
ACCOUNT MENU
  1. Check Balance
  2. Deposit
  3. Withdraw
  4. Transfer
  5. Transaction History
  6. Change PIN
  7. Logout
        |
   back to MAIN MENU
```

## How to Run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Download or clone this repository.
3. Run the program from the project folder:
   ```
   python banking_system.py
   ```

## Sample Output

```
---Create Account---
Enter your name: Aditya Modanwal
Enter your phone number: 9876543210
Create a 4-digit PIN: 2311
Confirm your PIN: 2311
Account created successfully!
Your account number  1809659100
```

```
Enter Choice: 2
Enter the amount to deposit: 500
Amount  500.0 Rs deposited successfully. Total balance  500.0 Rs
```

## Notes

- Account data is stored in memory only, so all accounts are reset when the program exits. Create accounts and test everything within a single run.
- Data persistence (for example saving to a file) can be added as a future improvement.

## Author

Aditya Modanwal
