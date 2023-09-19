from transaction import Transaction

class Transfer(Transaction):
    def __init__(self, amount, target_user):
        super().__init__('TRANSFER', amount, target_user)
