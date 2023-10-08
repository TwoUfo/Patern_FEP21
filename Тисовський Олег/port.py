from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Ship

import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass


class Port(IPort):

    def __init__(self, latitude: float, longitude: float) -> None:
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship):
        if ship.__class__ == 'Ship':
            print('!-Given Object is Not Ship-!')
        elif ship not in self.current_ships:
            self.current_ships.append(ship)
            print('<-Ship had arrived to new Port->')
        else:
            print('!-Error-!')

    def outgoing_ship(self, ship: Ship):
        if ship.__class__ == 'Ship':
            print('!-Given Object is Not Ship-!')
        elif ship in self.current_ships:
            self.ship_history.append(ship)
            self.current_ships.remove(ship)
            print('<-Ship left current Port->')
        else:
            print('!-Error-!')
