from LLD2.Structural.Decorator.IceCream import IceCream


class ChocolateConeDecorator(IceCream):
    def __init__(self, ice_cream: IceCream | None = None): #icecream - normal cone
        self.ice_cream = ice_cream

    def get_price(self):
        if self.ice_cream is None:
            return 15
        return self.ice_cream.get_price() + 15

    def get_description(self):
        if self.ice_cream is None:
            return " Chocolate_Cone -->"
        return self.ice_cream.get_description() + " Chocolate_Cone -->"