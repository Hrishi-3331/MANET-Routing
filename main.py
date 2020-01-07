from Classes.BattleField import BattleField
import json as json

x = input('Enter number of soldiers')
WarField = BattleField(int(x))

WarField.create_soldiers()
soldier_list = WarField.get_soldiers()

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