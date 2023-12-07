from os.path import exists, isfile
from json import dumps

from .counters import count_containers


def _serialize_ships(ships: list) -> list:
    serialized_ships = []

    for ship in ships:
        serialized_ship = {
            "ship_id": str(ship.id),
            "port_id": str(ship.port.id),
        }

        serialized_ships.append(serialized_ship)

    return serialized_ships


def save(fp: str, ports: list) -> None:
    if not exists(fp) or not isfile(fp):
        raise Exception("Provided path is invalid or not exist.")

    with open(fp, "w") as file:
        prepared_data = []

        for port in ports:
            data = {"port_id": str(port.id)}

            data["ships"] = _serialize_ships(port.current_ships)
            data["containers"] = count_containers(port.containers)

            prepared_data.append(data)

        file.write(dumps(prepared_data))
