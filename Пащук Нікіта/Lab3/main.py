import json
from random import randint, choice
from Port import Port, ContainerDetails
from Ship import DataShip, MakeShip
from Container import Container, get_type
from Item import IItem
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
port_num = randint(0, len(Ports) - 1)

Ships = []
port_count = len(Ports)
for i, ship in enumerate(project_data["Ships_data"]):
    port = Ports[i % port_count]
    ship_data = DataShip(
        ship["total_weight_capacity"],
        ship["maxNumberOfAllContainers"],
        ship["maxNumberOfBasicContainers"],
        ship["maxNumberOfHeavyContainers"],
        ship["maxNumberOfRefrigeratedContainers"],
        ship["maxNumberOfLiquidContainers"],
        ship["fuelConsumptionPerKM"]
    )
    new_ship = MakeShip.check_type(ship["id"], ship["fuel"], port, ship_data)
    Ships.append(new_ship)
    port.ship_current.append(new_ship)

Containers = []
for i, container in enumerate(project_data['Containers_data']):
    port = Ports[i % port_count]
    if len(container) == 2:
        new_container = Container.check_category(container["id"], container['weight'])
        Containers.append(new_container)
        port.containers.append(new_container)
    elif len(container) == 3:
        new_container = Container.check_category(container["id"], container['weight'], (container['type']))
        Containers.append(new_container)
        port.containers.append(new_container)

Items = []
for i in range(36):
    item = IItem.check_type(
        str(uuid4()), randint(1, 30)*20, randint(1, 6), choice(["R", "L", None, None])
        )
    Items.append(item)

for item in Items:
    for cont in Containers:
        if ((item.item_type == cont.type or (cont.type == "Basic" and item.item_type == "Small"))
                and len(cont.items) < cont.max_items):
            cont.items.append(item)
            cont.weight += item.getTotalWeight()
            item.containerID = get_type(cont)


def main():

    def port_data(port):
        container_types = ['Basic', 'Heavy', 'Refrigerated', 'Liquid']
        container_counts = {
            container_type: [cont.id for cont in port.containers if cont.type == container_type]
            for container_type in container_types}

        ship_data = {ship.id: f'{ship.fuel}' for ship in port.ship_current}
        ship_containers = {ship.id: [cont.id for cont in ship.containers] for ship in port.ship_current}
        container_items = {}
        for container in port.containers:
            container_items[container.id] = [item.id for item in container.items]

        return {
            f'Port ID: {port.id} and coords: ({port.latitude}, {port.longitude})': {
                'Containers': container_counts,
                'Ships': ship_data,
                'Ship Containers': ship_containers,
                'Container Items': container_items
            }
        }
    output_data = {}

    for port in Ports:
        output_data.update(port_data(port))

    with open('output_data.json', 'w') as output_file:
        json.dump(output_data, output_file, indent=2)

    """TEST FUNCTIONS"""

    """loading containers"""
    test_ship = Ships[1]
    print(f"We will test {test_ship.ship_type} ship\n")
    print("Num of containers in a port before loading them on the ship: ", len(test_ship.current_port.containers))
    temp_copy = list(test_ship.current_port.containers)
    for cont in temp_copy:
        result = test_ship.load(cont)
        print(result)
    print("Id of containers that are on the ship: ")
    test_ship.get_current_containers()
    print("Num of containers in a port after loading some on the ship: ", len(test_ship.current_port.containers), "\n")

    """Sailing and refueling"""

    print("\nCurrent ships in first port: ")
    for k in range(len(Ports[1].ship_current)):
        print(Ports[1].ship_current[k].id)
    print(f"Ship history in first port: {Ports[1].ship_history}")
    for j in range(0, len(Ports[1].ship_current)):
        print(Ports[1].ship_current[0].sail_to(Ports[1], Ports[0], Ports[2]))

    print(f"Current ships in new port: ")
    for k in range(len(Ports[0].ship_current)):
        print(Ports[0].ship_current[k].id)
    print("Ship history for previous port: ")
    for j in range(len(Ports[1].ship_history)):
        print(Ports[1].ship_history[j].id)

    """Unloading containers"""

    print("\n\nUnloading containers back")
    while test_ship.containers:
        result = test_ship.unload(test_ship.containers[0])
        print(result)
    print(f"Num of containers in a port after unloading some from the ship: {len(test_ship.current_port.containers)}\n")


if __name__ == "__main__":
    main()
