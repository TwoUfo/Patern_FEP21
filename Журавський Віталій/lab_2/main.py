from Container import initContainer
from Ship import Ship, DataShip
from Port import Port, DataPort
import json

with open('input.json') as file:
    data = json.load(file)

ships = []
ports = []
for item in data:
    temp = Port(item['latitude'], item['longitude'], DataPort(
        item['basic'],
        item['heavy'],
        item['refrigerated'],
        item['liquid']
    ))
    ports.append(temp)
    for inner_item in item['ships']:
        ships.append(Ship(
            temp,
            DataShip(
                inner_item['totalWeightCapacity'],
                inner_item['maxNumberOfAllContainers'],
                inner_item['maxNumberOfHeavyContainers'],
                inner_item['maxNumberOfRefrigeratedContainers'],
                inner_item['maxNumberOfLiquidContainers'],
                inner_item['fuelConsumptionPerKM']
            ),
            inner_item['fuel']
        ))

with open('containers.json') as file:
    data = json.load(file)

containers = []
for item in data['containers']:
    containers.append(initContainer.init_container(item[0], item[1]))


ships[0].sail_to(ports[1])
ships[1].sail_to(ports[1])







