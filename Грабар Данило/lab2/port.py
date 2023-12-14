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
    """Implements port logic"""

    def __init__(self, latitude: float, longitude: float, containers=None) -> None:
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = containers
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True

    def outgoing_ship(self, ship: Ship) -> bool:
        # TODO: add checker
        if ship in self.ship_history:
            return False
        else:
            self.ship_history.append(ship)
            return True

    def serialize(self):
        port_data = {
            "port id": str(self.id),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "containers": self.containers,
        }
        return port_data

