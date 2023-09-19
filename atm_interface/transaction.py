class Transaction:
    def __init__(self, transaction_type, amount, target_user=None):
        self.transaction_type = transaction_type
        self.amount = amount
        self.target_user = target_user

    def __str__(self):
        if self.transaction_type == 'DEPOSIT':
            return f'\nDeposited ${self.amount}\n'
        elif self.transaction_type == 'WITHDRAW':
            return f'\nWithdrew ${self.amount}\n'
        elif self.transaction_type == 'TRANSFER':
            return f'\nTransferred ${self.amount} to {self.target_user.user_id}\n'
