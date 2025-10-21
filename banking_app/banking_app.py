# ========================== Bank App Exercise ===============================================================

# Build a simple console-based banking system that allows users to 
# 1. create accounts, 
# 2. deposit money, 
# 3. withdraw money, and 
# 4. check balances 
# using functions, loops, if/else, lists, and dictionaries.

'''
    Bank account structure
    {
        'user': {'first_name': '', 'last_name': ''},
        'account': {'account_name': '', 'account_number': '', 'account_balance': ''}
    }
'''

import random

# Sample data to test withdraw/deposit flows
accounts = [
    {
        'user': {
            'first_name': 'Ada',
            'last_name': 'Lovelace',
        },
        'account': {
            'account_name': 'Checking',
            'account_number': '1001',
            'account_balance': 750,   # int
        }
    },
    {
        'user': {
            'first_name': 'Alan',
            'last_name': 'Turing',
        },
        'account': {
            'account_name': 'Savings',
            'account_number': '1002',
            'account_balance': 1200,  # int
        }
    },
    {
        'user': {
            'first_name': 'Grace',
            'last_name': 'Hopper',
        },
        'account': {
            'account_name': 'Checking',
            'account_number': '1003',
            'account_balance': 0,     # edge case: zero balance
        }
    },
    {
        'user': {
            'first_name': 'Linus',
            'last_name': 'Torvalds',
        },
        'account': {
            'account_name': 'Savings',
            'account_number': '1004',
            'account_balance': 0,
        }
    },
]

user_options = ["1. Create Account", "2. Deposit Money", "3. Withdraw Money", "4. Check Balance", "5. Quit"]


print(
    "Welcome To ST Bank.\n"   
)

def greet():
    print("What would you like to do\n" + "\n".join(user_options))

    user_selection = input("Select an option: ")

    if user_selection == '1':
        create_account()
    elif user_selection == '2':
        deposit_money()
    elif user_selection == '3':
        withdraw_money()
    elif user_selection == '4':
        check_balance()
    elif user_selection == '5':
        print("Nice doing business with you.")
        return
    else:
        print("Invalid Input, Please select")
        return greet()


def create_account():
    print("Creating Account...")
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")

    user = {
        'first_name': first_name,
        'last_name': last_name
    }
    account = {
        'account_name': f"{first_name} {last_name}",
        'account_number': f"12345{len(accounts) + 1}"
    }
    accounts.append({
        'user': user,
        'account': account
    })

    print("Your account has been created successfully\n")
    print(
        f'''
            Account Name: {account['account_name']}
            Account Number: {account['account_number']}
        '''
    )

    return greet()
    


def deposit_money():
    print("depositing money")

    account_number = input("Enter account number: ")

    # accounts = [ {'user': {'first_name: '', }, 'account: {'account_number': ""} },  ]
    user_account = None
    user_account_idx = None

    for idx,account in enumerate(accounts):
        if account['account']['account_number'] == account_number:
            user_account = account
            user_account_idx = idx
            break

    if not user_account:
        print("You do not have an account")
        return greet()
    
    acct = accounts[user_account_idx]['account']

    try:
        deposit_amount = int(input("How much do you want to deposit? ").strip())
        if deposit_amount <= 0:
                print("Input a valid amount")
                return greet()
        else:
            acct['account_balance'] += deposit_amount
            print(f"Deposited {deposit_amount}. New balance: {acct['account_balance']}")
            return greet()
    except ValueError:
        print("Input a Valid amount")
            
  
        
# 'account': {'account_name': '', 'account_number': '', 'account_balance': ''}

def withdraw_money():
    print("withdrawing money")
    user_balance = None
    user_account_id = None
    user_account = input("Enter account number: ")

    for idx,account in enumerate(accounts):

        if account['account']['account_number'] == user_account:
            user_account_id = idx
            user_balance = account['account']['account_balance']
            break

    if user_account_id is None:
        print("You do not have an account")
        return greet()
    
    try:
         amount = int(input("How much would you like to withdraw: "))
         if amount < 0:
             print("Input a valid amount")
             greet()
    except ValueError:
         print("Please enter a valid amount")
         return greet()

    balance = int(user_balance)

    if  balance < amount:
         print(f"Insufficent funds.Current Balance: {balance}")
         greet()

    balance -= amount
    print(f"Withdrew {amount}\n Current Balance: {balance}")
    greet()



def check_balance():
    print("checking balance")

    user_balance = None

    user_account = input("Enter account number: ")

    for account in accounts:
        if account['account']['account_number'] == user_account:
            user_balance = account['account'].get('account_balance',0)

            try:
                user_balance = int(user_balance)
            except(TypeError,ValueError):
                print("Account balance is invalid. Please contact support.")
                return greet()
            print(f"User account balance is {user_balance}")
            greet()
            break

    if user_balance is None:
        print("You do not have an account")
        return greet()



greet()