from LLD2.Structural.Adapter.ICICIBank.ICICIApi import ICICIBankApi
from LLD2.Structural.Adapter.PaymentProvider import PaymentProvider


class ICICIBankAdapter(PaymentProvider):
    def __init__(self):
        self.ICICIApi = ICICIBankApi()

    def make_payment(self, amount):
        ICICIBankApi.payment(amount)

    def get_status(self):
        ICICIBankApi.status()
