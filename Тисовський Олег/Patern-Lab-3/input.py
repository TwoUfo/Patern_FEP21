from ship import *
from port import *
from containers import *
from item import *
import json

def get_data():
    """Function returns lists with all Objects"""
    with open('input.json') as file:
        data = json.load(file)

    ships = []
    ports = []
    containers = []
    items = []

    # Getting all data
    for port in data:
        #Getting Ports
        temp_port = Port(port['latitude'], port['longitude'])
        ports.append(temp_port)
        #Getting Ships
        for ship_item in port['ships']:
            config_ship = ConfigShip(
                ship_item['total_weight_capacity'],
                ship_item['max_number_of_all_containers'],
                ship_item['max_number_of_basic_containers'],
                ship_item['max_number_of_heavy_containers'],
                ship_item['max_number_of_refrigerated_containers'],
                ship_item['max_number_of_liquid_containers'],
                ship_item['fuel_consumption_per_km']
            )
            fuel = ship_item['fuel']
            ship = None
            if ship_item['ship_type'] == 'LightWeightShip':
                ship = LightWeightShip(temp_port, fuel, config_ship)
            elif ship_item['ship_type'] == 'MediumShip':
                ship = MediumShip(temp_port, fuel, config_ship)
            elif ship_item['ship_type'] == 'HeavyShip':
                ship = HeavyShip(temp_port, fuel, config_ship)
            temp_port.current_ships.append(ship)
            ships.append(ship)

        # Getting Containers
        for con in port['containers']:
            weight = con['weight']
            container = None
            if con['container_type'] == 'Basic':
                container = BasicContainer(weight)
            elif con['container_type'] == 'Heavy':
                container = HeavyContainer(weight)
            elif con['container_type'] == 'Refrigerated':
                container = RefrigeratedContainer(weight)
            elif con['container_type'] == 'Liquid':
                container = LiquidContainer(weight)
            else:
                print('!-You entered wrong value for Container type-!')
            temp_port.containers.append(container)
            containers.append(container)

        #Getting Items
        for item in port['items']:
            weight = item['weight']
            count = item['count']
            itm = None
            if item['item_type'] == 'Small':
                itm = SmallItem(weight, count)
            elif item['item_type'] == 'Heavy':
                itm = HeavyItem(weight,count)
            elif item['item_type'] == 'Refrigerated':
                itm = RefrigeratedItem(weight, count)
            elif item['item_type'] == 'Liquid':
                itm = LiquidItem(weight, count)
            else:
                print('!-You entered wrong value for Container type-!')
            temp_port.items.append(itm)
            items.append(itm)

    return ships, ports, containers, items
