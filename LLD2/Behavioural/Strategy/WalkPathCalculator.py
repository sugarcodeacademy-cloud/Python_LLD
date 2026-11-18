from LLD2.Behavioural.Strategy.PathCalculator import PathCalculator


class WalkPathCalculator(PathCalculator):
    def findPath(self, source, destination):
        print("  [Walk Strategy] Calculating walking route...")
        print("  → Using footpaths and narrow alleys")
        print("  → Including staircases and pedestrian bridges")
        print("  → Taking the most direct route possible")

        return (
            f"Walking path from {source} to {destination} "
            f"via Footpath → Alley → Pedestrian Bridge → Destination "
            f"(ETA: 45 mins)"
        )