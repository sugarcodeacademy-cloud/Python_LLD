from LLD2.Behavioural.Strategy.PathCalculator import PathCalculator


class BikePathCalculator(PathCalculator):
    def findPath(self, source, destination):
        print("  [Bike Strategy] Calculating bike route...")
        print("  → Using shortcuts and inner roads")
        print("  → Avoiding highways and high-speed zones")
        print("  → Factoring in lane-splitting opportunities")

        return (
            f"Bike path from {source} to {destination} "
            f"via Inner Road → Shortcut → Destination (ETA: 18 mins)"
        )