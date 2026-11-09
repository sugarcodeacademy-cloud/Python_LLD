from LLD2.Structural.Adapter.PaymentProvider import PaymentProvider
from LLD2.Structural.Adapter.Paypal.PaypalApi import PaypalApi


class PaypalAdapter(PaymentProvider):
    def __init__(self):
        self.paypalApi = PaypalApi()

    def make_payment(self, amount):
        self.paypalApi.pay(amount)


    def get_status(self):
        self.paypalApi.get_status()