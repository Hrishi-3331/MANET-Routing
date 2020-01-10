class ClusterSoldier:

    def __init__(self, soldier, distance):
        self.soldier = soldier
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_clustered(self):
        self.soldier.set_clustered()

    def get_id(self):
        return self.soldier.get_id()

    def get_latitude(self):
        return self.soldier.get_latitude()

    def get_longitude(self):
        return self.soldier.get_longitude()


class ClusterStack:

    def __init__(self):
        self.soldier1 = None
        self.soldier2 = None
        self.soldier3 = None

    def check_feasibility(self, soldier):
        if self.soldier1 is None:
            self.soldier1 = soldier

        elif self.soldier2 is None:
            self.soldier2 = soldier

        elif self.soldier3 is None:
            self.soldier3 = soldier

        elif self.soldier1.get_distance() > soldier.get_distance():
            self.soldier3 = self.soldier2
            self.soldier2 = self.soldier1
            self.soldier1 = soldier

        elif self.soldier2.get_distance() > soldier.get_distance():
            self.soldier3 = self.soldier2
            self.soldier2 = soldier

        elif self.soldier3.get_distance() > soldier.get_distance():
            self.soldier3 = soldier

    def set_cluster(self):
        self.soldier1.set_clustered()
        self.soldier2.set_clustered()
        self.soldier3.set_clustered()

    def print_cluster(self):
        id1 = self.soldier1.get_id()
        id2 = self.soldier2.get_id()
        id3 = self.soldier3.get_id()
        print(str(id1) + "," + str(id2) + "," + str(id3) + "\n")

    def get_coordinates(self):
        coor1 = [self.soldier1.get_latitude(), self.soldier1.get_longitude()]
        coor2 = [self.soldier2.get_latitude(), self.soldier2.get_longitude()]
        coor3 = [self.soldier3.get_latitude(), self.soldier3.get_longitude()]

        return [coor1, coor2, coor3]