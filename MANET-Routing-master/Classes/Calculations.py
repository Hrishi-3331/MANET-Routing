import math

TILE_SIZE = 256


def get_world_coordinates(lat, lon):
    sin_y = math.sin(lat * math.pi/180)
    sin_y = min(max(sin_y, -0.9999), 0.9999)
    x = TILE_SIZE * (0.5 + lon/360)
    y = TILE_SIZE * (0.5 - math.log((1 + sin_y) / (1 - sin_y), math.e)/(4 * math.pi))
    coordinates = [x, y]
    return coordinates


def inverse_mercator(x, y):
    lng = (x/256 * 360) - 180
    n = math.pi - (2 * math.pi) * (y / 256)
    lat = ((180 / math.pi) * math.atan(0.5 * (math.exp(n) - math.exp(-n))))
    loc = [lat, lng]
    return loc


def get_distance(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return distance


def calculate_distance(soldier1, soldier2):
    coordinates1 = get_world_coordinates(soldier1.get_latitude(), soldier1.get_longitude())
    coordinates2 = get_world_coordinates(soldier2.get_latitude(), soldier2.get_longitude())
    return get_distance(coordinates1[0], coordinates1[1], coordinates2[0], coordinates2[1])
