from LLD2.Behavioural.Strategy.PathCalculator import PathCalculator


class CarPathCalculator(PathCalculator):
    def findPath(self, source, destination):
        #In real world you have to implement using graph algorithms
        print("  [Car Strategy] Calculating car route...")
        print("  → Preferring highways and main roads")
        print("  → Avoiding narrow lanes and pedestrian zones")
        print("  → Factoring in real-time traffic")
        return f"Car path from {source} to {destination}  via Highway → Main Road → Destination (ETA: 25 mins)"