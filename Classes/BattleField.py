from .Soldier import Soldier
import random


class BattleField:

    def __init__(self, soldier_count):
        self.lat = 21.129274
        self.lon = 79.056302
        self.soldier_count = soldier_count
        self.soldiers = []

    def create_soldiers(self):
        i = 0
        while i < self.soldier_count:
            random_latitude = self.lat + random.randint(1, 5)*0.0001 + random.randint(3, 6)*0.00001 + random.randint(1, 9)*0.000001
            random_longitude = self.lon + random.randint(1, 4)*0.0001 + random.randint(3, 9)*0.00001 + random.randint(1, 9)*0.000001
            random_battery = random.randint(1, 100)
            random_signal_strength = random.randint(1, 100)
            random_soldier = Soldier(i, random_longitude, random_latitude, random_battery, random_signal_strength)
            self.soldiers.append(random_soldier)
            i += 1

    def get_soldiers(self):
        return self.soldiers
