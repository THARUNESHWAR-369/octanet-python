from transaction import Transaction

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(Transaction("DEPOSIT", amount))

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(Transaction("WITHDRAW", amount))

    def transfer(self, target_user, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            target_user.balance += amount
            self.transaction_history.append(Transaction("TRANSFER", amount, target_user))

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def get_balance(self):
        return self.balance
