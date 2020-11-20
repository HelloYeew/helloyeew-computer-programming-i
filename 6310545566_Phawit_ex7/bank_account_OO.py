import random

# import random
# for i in range(10):
#     account_ID = str(random.randint(1000, 9999))
#     accout_name = 'account' + str(i)
#     balance = random.randint(20, 2000)
#     bank_account_DB[account_ID] = [accout_name, balance]

class Create:
    def __init__(self,account_name):
        self.account_ID = str(random.randint(1000, 9999))
        self.account_name = 'account' + str(account_name)
        self.balance = random.randint(20, 2000)

    def __str__(self):
        return self.bank_account

class Database:
    def __init__(self):
        self.bank_account = {}

    def add_account(self,account):
        self.bank_account[account.account_ID] = [account.account_name,account.balance]

    # search for a given bank account with ID
    def search(self,account_ID):
        if account_ID in self.bank_account.keys():
            return True
        else:
            return False

    # deposit an amount to a given bank account ID
    def deposit(self,account_ID, amount):
        if self.search(account_ID) == True:
            self.bank_account[account_ID][1] += amount
        else:
            print('Record not found.')

    # withdraw an amount from a given bank account ID
    def withdraw(self,account_ID, amount):
        if self.search(account_ID) == False:
            print('Record not found.')
        else:
            if self.bank_account[account_ID][1] < amount:
                print('Insufficient funds. Transacion aborted.')
            else:
                self.bank_account[account_ID][1] -= amount

    def __str__(self):
        return "\n".join([i + ':' + str(self.bank_account[i]) for i in self.bank_account])

bank_database = Database()
for i in range(10):
    bank_database.add_account(Create(i))


# main loop to run our banking system
while True:
    print('Banking System Menu:')
    print('Press 1 to display all records.')
    print('Press 2 to search for a record')
    print('Press 3 to deposit amount')
    print('Press 4 to withdraw amount')
    print('Press 0 to exit')
    choice = input('Enter a choice (0-4): ')
    if choice == '0':
        break
    elif choice == '1':
        print(bank_database)
    elif choice == '2':
        search_account = input('Enter an account number to search: ')
        if bank_database.search(search_account):
            print(search_account + ':' + str(bank_database.bank_account[search_account]))
        else:
            print('Record not found.')
    elif choice == '3':
        deposit_account = input('Enter an account number to deposit: ')
        deposit_amount = float(input('Enter an amount to deposit: '))
        bank_database.deposit(deposit_account, deposit_amount)
    elif choice == '4':
        withdraw_account = input('Enter an account number to withdraw: ')
        withdraw_amount = float(input('Enter an amount to withdraw: '))