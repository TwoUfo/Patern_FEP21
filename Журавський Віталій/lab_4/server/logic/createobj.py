import sqlite3
from mainapi.schemas.Port import Port
from mainapi.schemas.Ship import Ship, DataShip


class CreateObj:
    @staticmethod
    def port(ID):
        conn = sqlite3.connect('mainapi/db/data.db')
        port_row = conn.cursor().execute('''SELECT * from port WHERE id = ?''', (ID,)).fetchone()
        if port_row is not None:
            curr_port = Port(port_row[0], port_row[1], port_row[2])
            curr_ships = conn.cursor().execute('''SELECT * from ship''').fetchall()
            curr_containers = conn.cursor().execute('''SELECT * from container''').fetchall()

            for ship in curr_ships:
                if curr_port.id == ship[8]:
                    curr_port.current_ships.append(ship[0])

            for container in curr_containers:
                if curr_port.id == container[3]:
                    curr_port.containers.append(container[0])

            return curr_port

    @staticmethod
    def ship(ID, port):
        conn = sqlite3.connect('mainapi/db/data.db')
        ship_row = conn.cursor().execute('''SELECT * from ship WHERE id = ?''', (ID,)).fetchone()
        if ship_row is not None:
            data_ship = DataShip(ship_row[1], ship_row[2], ship_row[3], ship_row[4], ship_row[5], ship_row[6])
            return Ship.init_ship(ship_row[1], port, ship_row[0], data_ship, ship_row[7])
