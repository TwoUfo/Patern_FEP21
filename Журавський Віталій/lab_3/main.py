from Container import Container
from Ship import Ship, DataShip
from Port import Port
from Item import IItem
import json

with open('input.json') as file:
    data = json.load(file)


ports = []
for index, item in enumerate(data):

    def get_id(obj):
        return obj.id

    ''' --------< containers >-------- '''
    curr_containers = []
    for inner_item in item['containers']:
        curr_container = Container.init_container(inner_item[0], inner_item[1], inner_item[2])
        curr_containers.append(curr_container)

    curr_containers = sorted(curr_containers, key=get_id)

    # for inner_index, i in enumerate(curr_containers):
    #     i.id = inner_index

    ''' --------<    ports    >-------- '''
    curr_port = Port(item['id'], item['latitude'], item['longitude'])
    curr_port.containers = curr_containers
    ports.append(curr_port)

    ''' --------<    ships    >-------- '''
    curr_ships = []
    for inner_item in item['ships']:
        curr_ships.append(Ship.init_ship(
            inner_item['totalWeightCapacity'],
            curr_port,
            inner_item['id'],
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

    curr_ships = sorted(curr_ships, key=get_id)
    curr_port.current_ships = curr_ships


# for item in data:
#     temp = Port(item['id'], item['latitude'], item['longitude'])
#     ports.append(temp)
#     for inner_item in item['ships']:
#         ships.append(Ship(
#             temp,
#             inner_item['id'],
#             DataShip(
#                 inner_item['totalWeightCapacity'],
#                 inner_item['maxNumberOfAllContainers'],
#                 inner_item['maxNumberOfHeavyContainers'],
#                 inner_item['maxNumberOfRefrigeratedContainers'],
#                 inner_item['maxNumberOfLiquidContainers'],
#                 inner_item['fuelConsumptionPerKM']
#             ),
#             inner_item['fuel']
#         ))
#
# with open('containers.json') as file:
#     data = json.load(file)
#
# containers = []
# for item in data['containers']:
#     containers.append(initContainer.init_container(item[0], item[1], item[2]))
#
#

def load_item_to_container(port_index, containers_index, item_weight, item_count):
    curr_item = IItem.init_item(ports[port_index].containers[containers_index], item_weight, item_count, ports[port_index].containers[containers_index].id)
    ports[port_index].containers[containers_index].load_item(curr_item)


load_item_to_container(0, 2, 200, 3)
print(ports[0].current_ships[0].load(ports[0].containers[2]), type(ports[0].containers[2]), ports[0].containers[2].id)

# print(ports[0].current_ships)
# print(ports[1].current_ships)
# print()
#
# print(ports[1].current_ships[0].id)
# print(ports[1].current_ships[0].sail_to(ports[0]))
# print()
# print(ports[0].current_ships)
# print(ports[0].current_ships[2].id)




