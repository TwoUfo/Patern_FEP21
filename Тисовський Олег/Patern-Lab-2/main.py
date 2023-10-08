from ship import *
from port import *
from containers import *
import json

with open('input.json') as file:
    data = json.load(file)

ships = []
ports = []
containers = []

# Getting all data
for item in data:
    temp_port = Port(item['latitude'], item['longitude'])
    ports.append(temp_port)
    # Getting ships
    for ship_item in item['ships']:
        ship = Ship(
            temp_port,
            ConfigShip(
                ship_item['total_weight_capacity'],
                ship_item['max_number_of_all_containers'],
                ship_item['max_number_of_basic_containers'],
                ship_item['max_number_of_heavy_containers'],
                ship_item['max_number_of_refrigerated_containers'],
                ship_item['max_number_of_liquid_containers'],
                ship_item['fuel_consumption_per_km']
            ),
            ship_item['fuel']
        )
        temp_port.current_ships.append(ship)
        ships.append(ship)
    # Getting containers
    for con_item in item['containers']:
        con = None
        if con_item['container_type'] == 'Basic':
            con = BasicContainer(con_item['weight'])
        elif con_item['container_type'] == 'Heavy':
            con = HeavyContainer(con_item['weight'])
        elif con_item['container_type'] == 'Refrigerated':
            con = RefrigeratedContainer(con_item['weight'])
        elif con_item['container_type'] == 'Liquid':
            con = LiquidContainer(con_item['weight'])
        else:
            print('!-You entered wrong value for Container type-!')
        temp_port.containers.append(con)
        containers.append(con)

ships[0].sail_to(ports[1])
print()
ships[0].sail_to(ports[0])
ships[0].refuel(100000)
print()
ships[0].sail_to(ports[0])
print()


print('Container to load: ', containers[0])
print('Containers in Port: ', len(ports[0].containers))
print('Containers on ship: ', ships[0].containers, '\n')

ships[0].load(containers[0])
print('Containers in Port: ', len(ports[0].containers))
print('Containers on ship: ', ships[0].containers, '\n')

ships[0].unload(containers[0])
print('Containers in Port: ', len(ports[0].containers))
print('Containers on ship: ', ships[0].containers, '\n')






# 1. load data from JSON
# 2. Generate Ships based on JSON
# 3. Generate ports based on JSON
# 4. Generate containers
# Loop operations
# 4. Ships can load(), unload() containers
# 5. Ships sail to ports()
# 6. Ships can refuel in the ports;
# 7. Ships must check if they can reach the port
# end loop
# 8. Output to JSON
# 9* (optional). Unit tests all classes.
