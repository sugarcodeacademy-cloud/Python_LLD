from LLD2.Structural import ICICIBank
from LLD2.Structural.Adapter.PaymentProvider import PaymentProvider


class PaymentProcessor:
    def __init__(self, payment_provider: PaymentProvider): #payment_provider: ICICIBANK, PAYPAL
        self. payment_provider =  payment_provider;

    def proccess_payment(self, amount):
        self.payment_provider.make_payment(amount)
        self.payment_provider.get_status()



'''
Amazon --> My application


Payment Partners
1. ICICIBank --> We will recieve a document with API details and a link(API)
2.Paypal--> We will recieve a document with API details and a link(API)


Without Adapter Design:
I have to use if-elif- else conditions in each method for each payment partner because each bank has their own method names 

Problems:
1)Difficult to understand
2)Complex code



With Adapter Design:
We have creater an interface PaymentProvider(Interface / Abstract Class) --> Amazon method names for payment procssing 
make_payment_amazon/get_status_amazon

ICICIBank
ICICIBank has pay_icici/ get_status_icici_kotak as methods

Paypal
Paypal has payment_paypal/status_paypal as methods

You have to create an ICICIBankAdapter(PaymentProvider)
1.make_payment_amazon:
    pay_icici()
    
2.get_status_amazon:
    get_status_icici_kotak()
    
    
You have to create an PaypalAdapter(PaymentProvider)
1.make_payment_amazon:
    payemnt_paypal()
    
2.get_status_amazon:
    status_paypal()


In future I want to HDFC bank
HDFCBank has pay_hdfc/ status_hdfc as methods


You have to create an PaypalAdapter(PaymentProvider)
1.make_payment_amazon:
    pay_hdfc()
    
2.get_status_amazon:
    status_hdfc()


'''

