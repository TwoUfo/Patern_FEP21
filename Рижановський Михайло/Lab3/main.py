import json
from uuid import uuid4
import random
from items import Item, SmallItems, HeavyItems, RefrigeratedItem, LiquidItems, ItemFactory
from ship import Ship, ConfigShip, ShipFactory, LightWeightShip, HeavyShip, MediumShip
from port import Port, PortConfig
from containers import BasicContainer, RefrigeratedContainer, LiquidContainer, HeavyContainer, Container
with open("input.json") as input_file:
    data = json.load(input_file)

ports = []

ports_id = [str(uuid4()) for _ in range(5)]

ships_data = []
for _ in range(2):
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

    for _ in range(5):
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

        ships_data.append(ship_data)

    port_data["ships"] = ships_data
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
        port_deliver=ship_data['ports_deliver'],
        ship_config=configship,
        fuel=ship_data['fuel']
    )

    ships = []
    ports = []

    for i in range(2):
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

    items = []
    item_builder = ItemFactory()
    containers = []

    basic = port_data["containers"]["BasicContainer"]
    heavy = port_data["containers"]["HeavyContainer"]
    refrigerated = port_data["containers"]["RefrigeratedContainer"]
    liquid = port_data["containers"]["LiquidContainer"]


    def Create_container(weight):
        item_count = random.randint(2, 50)


        real_basic = BasicContainer(random.uniform(10.0, 5.0))
        real_heavy = HeavyContainer(random.uniform(10.0, 5.0))
        real_refrigerated = RefrigeratedContainer(random.uniform(10.0, 5.0))
        real_liquid = LiquidContainer(random.uniform(10.0, 5.0))

        if weight < 25:
            item = item_builder.create_item('Small item', item_weight, item_count, str(real_basic.id), 'very tiny')
            container = real_basic
        elif weight > 40:
            item = item_builder.create_item('Heavy item', item_weight, item_count, str(real_heavy.id), 'huge box')
            container = real_heavy
        elif weight > 30:
            item = item_builder.create_item('Refrigerated item', item_weight, item_count, str(real_refrigerated.id),
                                            'frezeee')
            container = real_refrigerated
        elif weight > 20:
            item = item_builder.create_item('Liquid item', item_weight, item_count, str(real_liquid.id),
                                            'thats water..?')
            container = real_liquid
        container.add_item(item)

        return container


    for cont_number in range(len(ports)):
        for i in range(configship.maxNumberOfAllContainers):
            item_weight = random.randint(20, 60)
            cont = Create_container(item_weight)

            ports[cont_number].containers.append(cont)

    for port in ports:
        ship_factory = ShipFactory()
        r_fuel = random.randint(1, 5)
        cont = Create_container(20)

        lightship = (ship_factory.create_ship('LightWeightShip', ship_data['ship_id'], ship_data['port_id'],
                                              ship_data['ports_deliver'], configship, ships_data[r_fuel]['fuel']))
        lightship.containers.append(cont)
        ships.append(lightship)
        r_fuel = random.randint(1, 5)
        cont = Create_container(45)

        mediumship = (ship_factory.create_ship('MediumShip', ship_data['ship_id'], ship_data['port_id'],
                                               ship_data['ports_deliver'], configship, ships_data[r_fuel]['fuel']))
        mediumship.containers.append(cont)
        ships.append(mediumship)
        r_fuel = random.randint(1, 5)
        cont = Create_container(random.randint(26, 39))

        heavyship = (ship_factory.create_ship('HeavyShip', ship_data['ship_id'], ship_data['port_id'],
                                              ship_data['ports_deliver'], configship, ships_data[r_fuel]['fuel']))
        heavyship.containers.append(cont)
        ships.append(heavyship)

        for ship in ships:
            ship2 = port.incoming_ship(ship)
            random_port = random.choice(ports)
            destination_port = random.choice(ports)
            distance = random_port.get_distance(destination_port)
            # ship_data['fuel'] = (distance / configship.fuelConsumptionPerKM)

        ships = []

for port in ports:
    for ship in port.current_ships:
        if isinstance(ship, Ship):
            port.incoming_ship(ship)
            ship.refuel(100)
            for container in containers:
                ship.unload(container)

            if port.incoming_ship(ship) and ship.sail_to(destination_port) and port.outgoing_ship(ship):
                for container in containers:
                    ship.load(container)

                ship.sail_to(destination_port)
                port.outgoing_ship(ship)

ship_json = []

for ship in ships:
    if isinstance(ship, Ship):
        ship_json.append(ship.serialize_ship())

ports_json = [port.serialize() for port in ports]
containers_json = [container.serialize() for container in containers]

for port_json in ports_json:
    port_json['id'] = str(port_json['id'])

for container_json in containers_json:
    container_json['id'] = str(container_json['id'])
    for item in container_json['items']:
        item['id'] = str(item['id'])
        item['containerID'] = str(item['containerID'])

port_output_data = []
for port_index, port in enumerate(ports):
    p_data = {
        "Port": {
            "id": port_json['id'],
            "longitude": port.longitude,
            "latitude": port.latitude,
            "basic": [container.serialize() for container in port.containers if isinstance(container, BasicContainer)],
            "heavy": [container.serialize() for container in port.containers if isinstance(container, HeavyContainer)],
            "Refrigerated": [container.serialize() for container in port.containers if
                             isinstance(container, RefrigeratedContainer)],
            "liquid": [container.serialize() for container in port.containers if
                       isinstance(container, LiquidContainer)],
            "current_ships": [ship.serialize_ship() for ship in port.current_ships],
        }
    }

    port_output_data.append(p_data)

with open('output_data.json', 'w') as outfile:
    json.dump(port_output_data, outfile, indent=4)