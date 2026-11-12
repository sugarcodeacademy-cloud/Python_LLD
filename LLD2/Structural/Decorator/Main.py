from LLD2.Structural.Decorator.NutsDecorator import NutsDecorator
from LLD2.Structural.Decorator.ChocoScoop import ChocoScoopDecorator
from LLD2.Structural.Decorator.ChocolateConeDecorator import ChocolateConeDecorator
from LLD2.Structural.Decorator.IceCream import IceCream
from LLD2.Structural.Decorator.NormalConeDecorator import NormalConeDecorator
from LLD2.Structural.Decorator.VanillaScoop import VanillaScoopDecorator

# ice_cream_1: IceCream= NutsDecorator(ChocoScoopDecorator(ChocolateConeDecorator(NormalConeDecorator())))
# print(ice_cream_1.get_price())
# print(ice_cream_1.get_description())

ice_cream_2: IceCream= NutsDecorator(ChocolateConeDecorator(VanillaScoopDecorator(NormalConeDecorator(ChocolateConeDecorator(NormalConeDecorator())))))
print(ice_cream_2.get_price())
print(ice_cream_2.get_description())

# ice_cream_3: IceCream = ChocoScoopDecorator()
# print(ice_cream_3.get_price())
# print(ice_cream_3.get_description())

# ice_cream_4: IceCream = ChocolateConeDecorator()
# print(ice_cream_4.get_price())
# print(ice_cream_4.get_description())

#TODO: Print a proper error message when there is no base like a cone "No base has been added.Please add any cone"