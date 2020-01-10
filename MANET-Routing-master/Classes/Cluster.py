import random


def generate_cluster_center():
    random_latitude = 21.128935 + random.randint(1, 9) * 0.0001 + random.randint(1, 9) * 0.00001 + random.randint(1,9) * 0.000001
    random_longitude = 79.055891 + random.randint(1, 9) * 0.0001 + random.randint(1, 9) * 0.00001 + random.randint(1, 9) * 0.000001
    return [random_latitude, random_longitude]

