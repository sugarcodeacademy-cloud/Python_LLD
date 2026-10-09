class WithdrawalError(Exception):
    def __init__(self,balance, amount):
        self.balance = balance
        self.amount = amount

        if amount > balance:
            self.message = "Insuffficient balance"

        elif amount > 100000:
            self.message = "Withdrwal limit exceeded"

        super().__init__(self.message)



