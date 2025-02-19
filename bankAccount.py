class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print ("Deposited", amount, "pesos, current balance is", self.balance)
        else:
            print ("Account is inactive")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print ("Withdrew", amount, "pesos, current balance is", self.balance)
            else:
                print ("Insufficient funds")
        else:
            print ("Account is inactive")

    def deactivate_account(self):
        self.is_active = False
        print ("Account deactivated")
    
    def activate_account(self):
        self.is_active = True
        print ("Account activated")

account1 = BankAccount("John", 1000)
account2 = BankAccount("Alice", 2000)

#llamada de metodos
account1.deposit(500)
account2.deposit(1000)
account1.withdraw(200)
account2.withdraw(500)
account1.deactivate_account()
account1.deposit(500)
account1.activate_account()
account1.deposit(500)