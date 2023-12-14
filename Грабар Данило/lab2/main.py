import jsonpickle
from uuid import uuid4
import random
from ship import Ship, ConfigShip, IShip
from port import Port, IPort
from containers import BasicContainer, RefrigeratedContainer, LiquidContainer, HeavyContainer, Container

ports_id = [str(uuid4()) for i in range(5)]

ships = []
for i in range(5):
    configship = ConfigShip(
        totalWeightCapacity=random.randint(100, 2000),
        maxNumberOfAllContainers=random.randint(5, 30),
        maxNumberOfHeavyContainers=3,
        maxNumberOfRefrigeratedContainers=5,
        maxNumberOfLiquidContainers=5,
        fuelConsumptionPerKM=5,
    )

    ship = Ship(
        port=random.choice(ports_id),
        ship_config=configship,
        fuel=100,
    )
    ships.append(ship)

ports = []
for i in range(5):
    port = Port(
        latitude=random.randint(-90, 90),
        longitude=random.randint(-180, 180),
        containers=[
            BasicContainer(random.randint(1500, 3000)),
            HeavyContainer(random.randint(3000, 5000)),
            RefrigeratedContainer(random.randint(3000, 5000)),
            LiquidContainer(random.randint(3000, 5000))
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

    containers.append(container)

for ship in ships:
    ship = port.incoming_ship(ship)
    random_port = random.choice(ports)
    destination_port = random.choice(ports)
    distance = random_port.get_distance(destination_port)
    amount_of_fuel = - (distance / configship.fuelConsumptionPerKM)

for ship in ships:
    for port in ports:
        if random_port.get_distance(destination_port) / amount_of_fuel != 0:

            for container in containers:
                ship.load(container)

            if port.incoming_ship(ship) and ship.sail_to(random_port) and port.outgoing_ship(ship):
                for container in containers:
                    ship.unload(container)

                ship.refuel(amount_of_fuel)
                ship.sail_to(destination_port)
                port.outgoing_ship(ship)
        else:
            break

json_string = jsonpickle.encode(port, indent=2)
with open('input.json', 'w') as outfile:
    outfile.write(json_string)

output_data = []
for port_index, port in enumerate(ports):
    port_data = Port(
        longitude=port.longitude,
        latitude=port.latitude,
    )

    port_data.basic = []
    port_data.heavy = []
    port_data.Refrigerated = []
    port_data.liquid = []
    port_data.current_ships = []
    port_data.ship_history = []

    for container in port.containers:
        if isinstance(container, BasicContainer):
            port_data.basic.append(container)
        elif isinstance(container, HeavyContainer):
            port_data.heavy.append(container)
        elif isinstance(container, RefrigeratedContainer):
            port_data.Refrigerated.append(container)
        elif isinstance(container, LiquidContainer):
            port_data.liquid.append(container)

    # Add the current ships to the port_data object.
    for ship in port.current_ships:
        port_data.current_ships.append(ship)

    # Add the ship history to the port_data object.
    for ship in port.ship_history:
        port_data.ship_history.append(ship.id)

    output_data.append(port_data)

for port in ports:
    port_data = port.serialize()
    output_data.append(port_data)

json_output = jsonpickle.encode(output_data, indent=2)

with open('output_data.json', 'w') as outfile:
    outfile.write(json_output)
