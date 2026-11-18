from LLD2.Behavioural.Strategy.GoogleMaps import GoogleMaps
from LLD2.Behavioural.Strategy.ModeTypes import ModeTypes

maps = GoogleMaps()
# print(maps.findPath("Manikonda", "Madhapur", "car"))
print(maps.findPath("Manikonda", "Madhapur", ModeTypes.BIKE))

