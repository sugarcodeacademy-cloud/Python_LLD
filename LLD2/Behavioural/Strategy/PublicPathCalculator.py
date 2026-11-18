from LLD2.Behavioural.Strategy.PathCalculator import PathCalculator


class PublicPathCalculator(PathCalculator):
    def findPath(self, source, destination):
        print("[Public Strategy] find nearest bustops and train stations")
        print(5/0)