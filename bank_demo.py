'''
banking application
this version is done in the CLI for simplicity
and to focus on the functionality of the app
'''

import os

balance = 100
running = True

def cls():
    os.system('cls||clear')

def login():
    input("enter ")

def show_balance():  
    cls()

    print(f"Current Balance: ${balance}")
    user_input = input("""Options:
1) withdraw
2) deposit
3) back to home
""")
    
    if user_input == '1':
        withdraw()
    elif user_input == '2':
        deposit()
    elif user_input == '3':
        home_menu()

def deposit():
    cls()

    global balance

    deposit_amount = int(input("enter amount to deposit: "))
    balance += deposit_amount
    print(f"Deposit succesful, new balance: ${balance}")
    home_menu()

def withdraw():
    cls()

    global balance
    withdrawal_amount = int(input("enter amount to withdraw: "))
    if withdrawal_amount > balance:
        print("insufficient funds")
        home_menu()
    elif withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"Successful withdrawal, new balance: ${balance}")
    home_menu()

def home_menu():

    global running

    options_prompt = """## Sample Bank Demo ## 
enter one of the following options:
1) show balance
2) withdraw
3) deposit
4) exit
"""

    user_input = input(options_prompt)

    if user_input == '1':
        show_balance()
        print(options_prompt)
    elif user_input == '2':
        withdraw()
    elif user_input == '3':
        deposit()
    elif user_input == '4':
        print("program ended, goodbye")
        running = False
    else:
        os.system('cls||clear')
        print("invalid option, try again")
        home_menu()   

while running == True: 
    cls()
    home_menu()