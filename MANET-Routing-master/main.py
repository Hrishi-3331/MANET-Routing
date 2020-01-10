from Classes.BattleField import BattleField
import json as json
from Classes import Calculations
import math
from Classes import Cluster
from Classes.ClusterStack import ClusterStack
from Classes.ClusterStack import ClusterSoldier
from matplotlib import pyplot

x = input('Enter number of soldiers: ')
WarField = BattleField(int(x))

WarField.create_soldiers()
soldier_list = WarField.get_soldiers()
available_soldier_list = soldier_list[:]

N = len(soldier_list)
i = 0
cluster_points = []

for p in range(0, int(N/3)):
    cluster_points.append(Cluster.generate_cluster_center())

for point in cluster_points:
    stack = ClusterStack()
    lat1 = point[0]
    lon1 = point[1]
    [x1, y1] = Calculations.get_world_coordinates(lat1, lon1)
    for soldier in available_soldier_list:
        [x2, y2] = Calculations.get_world_coordinates(soldier.get_latitude(), soldier.get_longitude())
        dist = Calculations.get_distance(x1, y1, x2, y2)
        stack.check_feasibility(ClusterSoldier(soldier, dist))
    stack.set_cluster()
    WarField.add_cluster(stack)
    for soldier in available_soldier_list:
        if soldier.is_clustered():
            available_soldier_list.remove(soldier)

for stack in WarField.get_clusters():
    stack.get_coordinates()
features = []
i = 0
for soldier in soldier_list:
    temp = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                soldier.get_longitude(),
                soldier.get_latitude()
            ]
        },
        "properties": {
            "title": 'Soldier' + str(i),
            "icon": "monument"
        }
    }
    features.append(temp)
    i = i + 1

soldier_data = {
    "type": "FeatureCollection",
    "features": features
}

with open('./plots/soldiers.geojson', 'w') as outfile:
    json.dump(soldier_data, outfile)