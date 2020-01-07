
class Soldier:

    def __init__(self, id_number, longitude, latitude, power, signal_strength):
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.id_number = id_number
        self.power = power
        self.signal_strength = signal_strength

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
