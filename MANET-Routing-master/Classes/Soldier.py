
class Soldier:

    def __init__(self, id_number, longitude, latitude, power, signal_strength):
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.id_number = id_number
        self.power = power
        self.signal_strength = signal_strength
        self.cluster_id = None
        self.clustered = False

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_id(self):
        return self.id_number

    def get_power(self):
        return self.power

    def get_signal_strength(self):
        return self.signal_strength

    def set_cluster_id(self, id):
        self.cluster_id = id

    def get_cluster_id(self):
        return self.cluster_id

    def is_clustered(self):
        return self.clustered

    def set_clustered(self):
        self.clustered = True
