from LLD1.Day10ExceptionsandDecorators.Exceptions.CustomExceptionWithLogic.WithdrawalException import WithdrawalError


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance or amount > 100000:
            raise WithdrawalError(self.balance, amount)
        self.balance -= amount
        print(f"Remaining balance : {self.balance}")


account = BankAccount(200000)
try:
    account.withdraw(150000)
except WithdrawalError as e:
    print(f"Withdrawal Error: {e}")