class Person:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


class Account:

    def __init__(self, number, type, owner, balance=0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance
    
class Bank:

    def __init__(self):
        self.customers = {}
        self.accounts = {}


    # Adding a customer to the bank:

    def add_customer(self, customer):
        if customer.id in self.customers:
            print("Cstomer Already Exists!")
        else:
            self.customers[customer.id] = customer
            print(f"Customer Added: {customer.firstName} {customer.lastName}(ID: {customer.id})")


    # Adding an account to the bank:

    def account_add(self, account):
        if account.number in self.accounts:
            print("customer already exist!")
        elif account.owner.id  not in self.customers:
            print("customer id is not found")
        else:
            self.accounts[account.number] = account
            print(f"Account Added: Account Number: {account.number}, Type: {account.type}, Balance: ${account.balance}")



    # Removing an account from the bank:

    def account_remove(self, account):
        if account.number in self.accounts:
            self.accounts.pop(account.number)
            print("Account Removed")
        else:
            print("This Account Does Not Exist")


    # Depositing money into an account:

    def money_deposit(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount > 0:
                account.balance += amount
                print(f"Successfully Deposited ${amount}")
            else:
                print("Have To Be Greater Than Zero")
        else:
            print("This Account Does Not Exist")



    # Withdrawing money from an account:

    def money_withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount > 0 and amount <= account.balance:
                account.balance -= amount
                print(f"Successfully Withdrewed ${amount}")
            elif amount <= 0:
                print("Have To Be Greater Than Zero.")
            else:
                print("You Have Insufficient Funds.")
        else:
            print("This Account Does N0t Exist")


    # Balance inquiry for a particular account:

    def inquiry_balance(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Current Balance: ${account.balance:.2f}")
        else:
            print("Account Does Not Exist")