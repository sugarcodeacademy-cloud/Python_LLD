from LLD2.Structural.Decorator.IceCream import IceCream


class  VanillaScoopDecorator(IceCream):
    def __init__(self, ice_cream: IceCream):
        self.ice_cream = ice_cream

    def get_price(self):
        return self.ice_cream.get_price() + 20

    def get_description(self):
        return self.ice_cream.get_description() + " Vanilla_Scoop-->"