from transaction import Transaction

class Deposit(Transaction):
    def __init__(self, amount):
        super().__init__('DEPOSIT', amount)
