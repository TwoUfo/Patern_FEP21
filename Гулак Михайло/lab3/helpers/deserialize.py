from classes import (
    Port,
    Ship,
)

from .constants import CONTAINERS_MAPPING, ITEMS_MAPPING

from os.path import exists, isfile
from random import randint
from json import loads


def _deserialize_containers(serialized_port: map) -> list:
    containers = []

    for containers_type, containers_count in serialized_port["containers"].items():
        deserialized_containers = [
            CONTAINERS_MAPPING.get(containers_type)(randint(1000, 3000))
            for _ in range(0, containers_count)
        ]

        containers.extend(deserialized_containers)

    return containers


def _deserialize_ships(serialized_port: map) -> list:
    ships = []
    ship_types = ["light", "medium", "heavy"]

    for _ in serialized_port["ships"]:
        ship_type = ship_types[randint(0, 2)]
        ship = Ship.create(ship_type)
        ships.append(ship)

    return ships


def load(fp: str) -> list:
    if not exists(fp) or not isfile(fp):
        raise Exception("Provided path is invalid or not exist.")

    with open(fp, "r") as file:
        data = loads(file.read())

        ports = []
        item_types = ["small", "heavy", "refrigerated", "liquid"]

        for serialized_port in data:
            ships = _deserialize_ships(serialized_port)
            containers = _deserialize_containers(serialized_port)
            port = Port(randint(-90, 90), randint(-90, 90))
            for _ in range(5):
                item = ITEMS_MAPPING.get(item_types[randint(0, 3)])(
                    weight=randint(100, 1000), count=randint(1, 3)
                )

                port.items.append(item)

            for ship in ships:
                ship.port = port

            port.current_ships.extend(ships)
            port.containers.extend(containers)

            ports.append(port)

        return ports
