import json
import random
from Port import Port, ContainerDetails
from Ship import DataShip, Ship
from Container import Container
from uuid import uuid4

with open('Input_data.json') as ids:
    id_data = json.load(ids)

for cont_id in id_data['Containers_data']:
    cont_id["id"] = str(uuid4())

for port_id in id_data["Ports_data"]:
    port_id["id"] = str(uuid4())

for ship_id in id_data["Ships_data"]:
    ship_id["id"] = str(uuid4())

with open('Input_data.json', 'w') as ids:
    json.dump(id_data, ids, indent=2)

with open('Input_data.json') as file:
    project_data = json.load(file)

Ports = []
for port in project_data["Ports_data"]:
    Ports.append(Port(port["id"], port["latitude"], port["longitude"], ContainerDetails(
        port["basic_cont"],
        port["heavy_cont"],
        port["refrigerated_cont"],
        port["liquid_cont"])))
random_port = random.randint(0, len(Ports) - 1)

Ships = []
for ship in project_data["Ships_data"]:
    port_num = random.randint(0, len(Ports) - 1)
    Ships.append(Ship(ship["id"], ship["fuel"], Ports[port_num],
                      DataShip(ship["total_weight_capacity"],
                               ship["maxNumberOfAllContainers"],
                               ship["maxNumberOfBasicContainers"],
                               ship["maxNumberOfHeavyContainers"],
                               ship["maxNumberOfRefrigeratedContainers"],
                               ship["maxNumberOfLiquidContainers"],
                               ship["fuelConsumptionPerKM"])))
    Ports[port_num].ship_current.append(ship["id"])
Containers = []
for container in project_data['Containers_data']:
    if len(container) == 2:
        Containers.append(Container.check_category(container["id"], container['weight']))
    elif len(container) == 3:
        Containers.append(Container.check_category(container["id"], container['weight'], (container['value'])))
    Ports[random.randint(0, len(Ports) - 1)].containers.append(container["id"])


def main():
    """Sailing and refueling"""

    print("Current ships in this port: ", Ports[0].ship_current)
    print("Ship history for this port: ", Ports[0].ship_history)

    print(Ships[0].sail_to(Ports[0], Ports[1], Ports[2]))  # sailed without problems
    print(Ships[1].sail_to(Ports[0], Ports[1], Ports[2]))  # sailed after refueling in another port
    print(Ships[3].sail_to(Ports[0], Ports[1], Ports[2]))  # sailed after refueling at the starting port

    print("Current ships in this port: ", Ports[1].ship_current)
    print("Ship history for previous port: ", Ports[0].ship_history, '\n')

    """loading and unloading containers"""

    test_ship = Ships[1]
    print("Num of containers in a port before loading them on the ship: ", len(test_ship.current_port.containers))
    for cont in [Containers[0], Containers[3], Containers[6], Containers[7], Containers[8]]:
        result = test_ship.load(cont)
        if result is not False:
            print(result)
    print("Id of containers that are on the ship: ")
    test_ship.get_current_containers()
    print("Num of containers in a port after loading some on the ship: ", len(test_ship.current_port.containers), "\n")
    print("Unloading them back")
    for cont in [Containers[0], Containers[3], Containers[6], Containers[7], Containers[8]]:
        result = test_ship.unload(cont)
        if result is not False:
            print(result)
    print("Num of containers in a port after unloading some from the ship: ", len(test_ship.current_port.containers), "\n")


if __name__ == "__main__":
    main()
