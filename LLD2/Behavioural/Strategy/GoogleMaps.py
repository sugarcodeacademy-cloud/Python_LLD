from LLD2.Behavioural.Strategy.BikePathCalculator import BikePathCalculator
from LLD2.Behavioural.Strategy.CarPathCalculator import CarPathCalculator
from LLD2.Behavioural.Strategy.ModeTypes import ModeTypes
from LLD2.Behavioural.Strategy.PublicPathCalculator import PublicPathCalculator
from LLD2.Behavioural.Strategy.WalkPathCalculator import WalkPathCalculator


class GoogleMaps():
    # def findPath(self, source, destination, mode):
    #     if mode == "car":
    #         return "Consider Highways and toll roads"
    #     elif mode == "bike":
    #         return "Consider narrow lanes and shortcuts"
    #     elif mode == "public":
    #         return "bustops and train stations" 2
    #     else:
    #         return "Consider walkways, alleys, foot over bridges"

    def findPath(self, source, destionation ,mode):
        path_calculator = None
        if mode == ModeTypes.CAR:
           path_calculator = CarPathCalculator()
        elif mode == ModeTypes.BIKE:
           path_calculator = BikePathCalculator()
        elif mode == ModeTypes.WALK:
           path_calculator = WalkPathCalculator()
        elif mode == ModeTypes.PUBLIC:
            path_calculator = PublicPathCalculator()
        else:
            raise ValueError("Invalid mode ")
        return path_calculator.findPath(source, destionation)