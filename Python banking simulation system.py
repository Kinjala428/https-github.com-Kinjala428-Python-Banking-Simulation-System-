"""1.data_store--------------
Defines the account data structure used across the application.
Uses only a dictionary (account details) and a list (transaction history)
as required — no external database or advanced data structures."""
def create_new_account(name, balance, pin):
 '''Create and return a new account record.Structure:
{"name": str,"balance": float,"pin": str,"transactions": []   # list of transaction description strings}'''
 return {"name": name,"balance": balance,"pin": pin,"transactions": []}
"""2.validations
----------------
Centralised input validation functions.
Keeping validation logic separate supports the project's
'Error Handling Strategy' non-functional requirement and
keeps other modules clean and focused on their own job.
"""
def is_valid_amount(value_str):
    """Return True if value_str is a valid positive number, else False."""
    cleaned = value_str.replace(".", "", 1)
    if cleaned.isdigit() and float(value_str) > 0:
        return True
    return False
def is_valid_pin(pin_str):
    """Return True if pin_str is a 4-digit numeric PIN."""
    return pin_str.isdigit() and len(pin_str) == 4
def is_valid_name(name_str):
    """Return True if the name is non-empty and contains no digits."""
    return len(name_str.strip()) > 0 and not any(ch.isdigit() for ch in name_str)
"""3.utils---------
Small display/UI helper functions kept separate from business logic
to support the project's modularity and maintainability goals."""
def display_menu():
#Display the main menu options.
    print("===== BANKING SIMULATION MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Mini Statement")
    print("5. Full Transaction History")
    print("6. Session Summary")
    print("7. Exit")
    print("====================================")
def print_welcome():
    print("=====================================================")
    print("   Welcome to the Python Banking Simulation System")
    print("=====================================================\n")
def print_goodbye(name):
    print("Thank you for banking with us, {name}!")
    print("Session ended.")
"""4.account_management.py
-----------------------
FUNCTIONAL MODULE 1: Account Management
Handles account creation, PIN-based authentication, and balance inquiry."""
from data_store import create_new_account
from validations import is_valid_amount, is_valid_pin, is_valid_name
def setup_account():
    """Interactively collect account details and create a new account."""
    print("----- Create New Account -----")

    while True:
        name = input("Enter account holder name: ")
        if is_valid_name(name):
            break
        print("Invalid name. Please do not leave it empty or use digits.")

    while True:
        balance_str = input("Enter initial deposit amount: ")
        if is_valid_amount(balance_str):
            balance = float(balance_str)
            break
        print("Invalid amount. Please enter a valid positive number.")

    while True:
        pin = input("Set a 4-digit PIN for your account: ")
        if is_valid_pin(pin):
            break
        print("Invalid PIN. Please enter exactly 4 digits.")

    account = create_new_account(name, balance, pin)
    print(f"\nAccount created successfully for {account['name']}!")
    print(f"Initial Balance: {account['balance']:.2f}\n")
    return account
def authenticate(account):
    """Ask the user for their PIN and confirm it matches the account's PIN."""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN to continue: ")
        if entered_pin == account["pin"]:
            print("Authentication successful.")
            return True
        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")
    print("Too many incorrect attempts. Session locked.")
    return False


def check_balance(account):
    """5.Display the current account balance."""
    print(f"\nCurrent Balance: {account['balance']:.2f}\n")
#transactions.py-----------------
#FUNCTIONAL MODULE 2: Transaction Processing
#Handles deposit and withdrawal operations, including validation
#and updating the accounts transaction history.
from validations import is_valid_amount
def deposit(account):
    #Deposit money into the account after validating the input.
    amount_str = input("Enter amount to deposit: ")

    if not is_valid_amount(amount_str):
        print("\nInvalid input. Please enter a valid positive number.")
        return
    amount = float(amount_str)
    account["balance"] += amount
    account["transactions"].append("Deposit: +{amount:.}")
    print("Deposit successful! New Balance: {account['balance']:}")
def withdraw(account):
    """Withdraw money from the account after validating input and balance."""
    amount_str = input("Enter amount to withdraw: ")
    if not is_valid_amount(amount_str):
        print("Invalid input. Please enter a valid positive number.")
        return
    amount = float(amount_str)
    if amount > account["balance"]:
        print("Insufficient funds! Withdrawal denied.")
        return
    account["balance"] -= amount
    account["transactions"].append(f"Withdraw: -{amount:.2f}")
    print("Withdrawal successful! New Balance: {account['balance']:}")
    """6.reports.py-----------
FUNCTIONAL MODULE 3: Reporting
Handles mini statements, full transaction history, and a session summary
(total deposited vs. total withdrawn) — demonstrating basic data processing
and analytics over the transaction list."""
def mini_statement(account):
    """Display the last 5 transactions."""
    print("----- Mini Statement -----")
    if len(account["transactions"]) == 0:
        print("No transactions yet.")
    else:
        recent = account["transactions"][-5:]
        for i in range(len(recent)):
            print(f"{i + 1}. {recent[i]}")
    print("---------------------------")
def full_statement(account):
    """Display the complete transaction history for the session."""
    print("----- Full Transaction History -----")
    if len(account["transactions"]) == 0:
        print("No transactions yet.")
    else:
        for i in range(len(account["transactions"])):
            print(f"{i + 1}. {account['transactions'][i]}")
    print("-------------------------------------\n")
def session_summary(account):
    """Calculate and display total deposited and total withdrawn this session."""
    total_deposited = 0.0
    total_withdrawn = 0.0
    for txn in account["transactions"]:
        amount_part = txn.split(":")[1].strip()
        amount_value = float(amount_part.replace("+", "").replace("-", ""))
        if txn.startswith("Deposit"):
            total_deposited += amount_value
        elif txn.startswith("Withdraw"):
            total_withdrawn += amount_value
    print("----- Session Summary -----")
    print("Total Deposited : {total_deposited:}")
    print("Total Withdrawn : {total_withdrawn:}")
    print("Net Change      : {total_deposited - total_withdrawn:}")
    print("Closing Balance : {account['balance']:.}")
    print("----------------------------")
    """main.py
--------
Entry point of the Banking Simulation application.
Ties together the three functional modules:
  1. Account Management (account_management.py)
  2. Transaction Processing (transactions.py)
  3. Reporting (reports.py)

Run this file to start the application:  python main.py
"""
from account_management import setup_account, authenticate, check_balance
from transactions import deposit, withdraw
from reports import mini_statement, full_statement, session_summary
from utils import display_menu, print_welcome, print_goodbye
def main():
    print_welcome()
    account = setup_account()

    if not authenticate(account):
        return  # end program if authentication fails

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        try:
            if choice == "1":
                check_balance(account)
            elif choice == "2":
                deposit(account)
            elif choice == "3":
                withdraw(account)
            elif choice == "4":
                mini_statement(account)
            elif choice == "5":
                full_statement(account)
            elif choice == "6":
                session_summary(account)
            elif choice == "7":
                print_goodbye(account["name"])
                break
            else:
                print("Invalid choice. Please select an option between 1 and 7.")
        except Exception as error:
 # Defensive catch-all so an unexpected error never crashes the session
            print("Something went wrong: {error}. Please try again.")
if __name__ == "__main__":
    main()








