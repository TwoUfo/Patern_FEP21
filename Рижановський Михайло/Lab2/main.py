import json
import uuid 
from uuid import uuid4
import random
from ship import Ship, ConfigShip, IShip
from port import Port, PortConfig
from containers import BasicContainer, RefrigeratedContainer, LiquidContainer, HeavyContainer, Container

with open("input.json") as input_file:
    data = json.load(input_file)

ports = []

ports_id = [str(uuid4()) for _ in range(5)]

for _ in range(5):
    port_id = str(uuid4())
    port_data = {
        "port_id": port_id,
        "latitude": round(random.uniform(-90, 90), 2),
        "longitude": round(random.uniform(-180, 180), 2),
        "ships": [],
        "containers": {
            "BasicContainer": random.randint(1, 10),
            "HeavyContainer": random.randint(1, 15),
            "RefrigeratedContainer": random.randint(1, 20),
            "LiquidContainer": random.randint(1, 16),
        },
    }

    ships = []
    for _ in range(10):
        ship_id = str(uuid4())
        fuel_consumption = round(random.uniform(0.1, 1.0), 2)

        ship_data = {
            "ship_id": ship_id,
            "port_id": port_id,
            "ports_deliver": random.choice([p for p in ports_id if p != port_id]),
            "totalWeightCapacity": random.randint(3000, 12000),
            "maxNumberOfAllContainers": random.randint(10, 30),
            "maxNumberOfHeavyContainers": random.randint(10, 15),
            "maxNumberOfRefrigeratedContainers": random.randint(10, 12),
            "maxNumberOfLiquidContainers": random.randint(10, 13),
            "fuelConsumptionPerKM": round(random.uniform(0.1, 1.0), 2),
            "fuel": random.randint(50, 1000),
        }

        ships.append(ship_data)

    port_data["ships"] = ships
    ports.append(port_data)

input_data = {"ports": ports}

with open("input.json", "w") as outfile:
    json.dump(input_data, outfile, indent=2)
    
    port = Port(
            port_data["latitude"],
            port_data['longitude'],
            PortConfig(port_data["containers"]["BasicContainer"],
                       port_data["containers"]['HeavyContainer'],
                       port_data["containers"]['RefrigeratedContainer'],
                       port_data["containers"]['LiquidContainer'])
        )
    configship = ConfigShip(
        totalWeightCapacity=random.randint(100, 2000),
        maxNumberOfAllContainers=random.randint(5, 10),
        maxNumberOfHeavyContainers=3,
        maxNumberOfRefrigeratedContainers=5,
        maxNumberOfLiquidContainers=5,
        fuelConsumptionPerKM=5,
    )

    ship = Ship(
        port=str(random.choice(ports_id)),
        ship_config=configship,
        fuel = ship_data['fuel']
    )
    ships.append(ship)

ports = []
for i in range(5):
    port = Port(
        latitude=random.randint(-90, 90),
        longitude=random.randint(-180, 180),
        containers=[
            BasicContainer(random.randint(5, 10)),
            HeavyContainer(random.randint(2, 10)),
            RefrigeratedContainer(random.randint(5, 15)),
            LiquidContainer(random.randint(1, 10))
        ],
    )
    ports.append(port)

containers = []
for i in range(configship.maxNumberOfAllContainers):
    weight = random.randint(1500, 6000)
    if weight <= 3000:
        container = BasicContainer(weight)
    elif 3000 < weight <= 4000:
        container = HeavyContainer(weight)
    else:
        container = RefrigeratedContainer(weight)
    
    ship.containers.append(container)
    port.containers.append(container)

    basic = port_data["containers"]["BasicContainer"]
    heavy = port_data["containers"]["HeavyContainer"]
    refrigerated = port_data["containers"]["RefrigeratedContainer"]
    liquid = port_data["containers"]["LiquidContainer"]

    for count in range(0, basic):
        real_basic = BasicContainer(random.uniform(10.0, 5.0))

    for count in range(0, heavy):
        real_heavy = HeavyContainer(random.uniform(10.0, 5.0))

    for count in range(0, refrigerated):
        real_refrigerated = RefrigeratedContainer(random.uniform(10.0, 5.0))

    for count in range(0, liquid):
        real_liquid = LiquidContainer(random.uniform(10.0, 5.0))

for ship in ships:
    for port in ports:
        ship = port.incoming_ship(ship)
        random_port = random.choice(ports)
        destination_port = random.choice(ports)
        distance = random_port.get_distance(destination_port)
        print(f"dist {distance}")
        fuel = (distance / configship.fuelConsumptionPerKM)
        print(f"fuel {fuel}")

for ship in ships:
    for port in ports:
        if isinstance(ship, Ship):
            ship.refuel(100)
            for container in containers:
                ship.unload(container)
                port.append(container)

            if port.incoming_ship(ship) and ship.sail_to(destination_port) and port.outgoing_ship(ship):
                for container in containers:
                    ship.unload(container)

                ship.sail_to(destination_port)
                port.outgoing_ship(ship)

ship_json = []

for ship in ships:
    if isinstance(ship, Ship):
        ship_json.append(ship.serialize())

port_json = [port.serialize() for port in ports]
container_json = [container.serialize() for container in containers]

port_output_data = []

for port_index, port in enumerate(ports):
    p_data = {
        "Port": {
        "longitude": port.longitude,
        "latitude": port.latitude,
        "basic": [container.serialize() for container in port.containers if isinstance(container, BasicContainer)],
        "heavy": [container.serialize() for container in port.containers if isinstance(container, HeavyContainer)],
        "Refrigerated": [container.serialize() for container in port.containers if isinstance(container, RefrigeratedContainer)],
        "liquid": [container.serialize() for container in port.containers if isinstance(container, LiquidContainer)],
        "current_ships": [ship.serialize() for ship in port.current_ships],
        }
    }

    for ship in port.current_ships:
        p_data["Port"]["current_ships"].append(ship_json)

    port_output_data.append(p_data)

with open('output_data.json', 'w') as outfile:
    json.dump(port_output_data, outfile, indent=4)
