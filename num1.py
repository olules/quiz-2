class BankAccount:

    def __init__(self, accountNumber, owner, balance, type):
        self.accountNumber = str(accountNumber)
        self.owner = str(owner)
        self.balance = float(balance)
        self.type = str(type)

    def __repr__(self):
        print(
            f'Bank Account Number:  {self.accountNumber}\n Account balance: {self.balance}\n Owner: {self.owner} \n Type: {self.type}')


class Bank:
    def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = accounts

    def add_account(self, account):
        self.account.append(account)


class Customers:
    def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = accounts

    def add_customer(self, account):
        self.account.append(account)


class Transactions:
    def __init__(self, accounts, amount, type):
        self.amount = str(amount)
        self.account = accounts
        self.type = type

    def Deposit(self, d):
        self.balance = self.balance + d

    def Withdrawal(self, w):
        if (self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
    # create bankFees() method

    def bankFees(self):
        self.balance = (95/100)*self.balance

    # create display() method
    def display(self):
        print("Account Number : ", self.accountNumber)
        print("Account Name : ", self.name)
        print("Account Balance : ", self.balance, " $")


bank = Bank('My Bank', [])
customer = Customers('Olule', [])
bankaccount = BankAccount(111, 1000, 'olul', 500, "savings")
customer.add_customer(bankaccount)
bank.add_account(bankaccount)

print(bank)
