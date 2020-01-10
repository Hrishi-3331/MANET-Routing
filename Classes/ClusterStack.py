class ClusterSoldier:

    def __init__(self, soldier, distance):
        self.soldier = soldier
        self.distance = distance

    def get_distance(self):
        return self.distance

class ClusterStack:

    def __init__(self):
        self.soldier1 = None
        self.soldier2 = None
        self.soldier3 = None

    def check_feasibility(self, soldier):
        if self.soldier1 is None:
            self.soldier1 = soldier

        elif self.soldier1.get_distance() > soldier.get_distance()
