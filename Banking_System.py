class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_user_info(self):
        print(f"The account info are: \nName: {self.name}\nAge: {self.age}")



class Py_Bank(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"Your deposit was successfull. Your new balance is {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient fund. Your balance is {self.balance}")
        else:
            self.balance -= self.amount
            print(f"Your withdraw was successfull. Your new balance is {self.balance}")

    def print_account(self):
        self.print_user_info()
        print(f"Balance: {self.balance}")