from LLD2.Structural.Decorator.IceCream import IceCream


class NormalConeDecorator(IceCream):
    def __init__(self, ice_cream: IceCream | None = None):
        self.ice_cream = ice_cream

    def get_price(self):
        if self.ice_cream is None:
            return 5
        return self.ice_cream.get_price() + 5

    def get_description(self):
        if self.ice_cream is None:
            return "Normal_Cone-->"
        return self.ice_cream.get_description() + " Normal Cone -->"