from LLD2.Structural.Decorator.IceCream import IceCream


class NutsDecorator(IceCream):
    def __init__(self, ice_cream: IceCream):
        self.ice_cream = ice_cream

    def get_price(self):
        return self.ice_cream.get_price() + 50

    def get_description(self):
        return self.ice_cream.get_description() + " Nuts-->"