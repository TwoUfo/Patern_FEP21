from abc import ABC, abstractmethod
from uuid import uuid4
from dataclasses import dataclass
from ship import Ship
import haversine as hs

@dataclass
class PortConfig:
    BasicContainer: int
    HeavyContainer: int
    RefrigeratedContainer: int
    LiquidContainer: int

class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass

class Port(IPort):
    def __init__(self, latitude: float, longitude: float, containers=None):
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True

    def outgoing_ship(self, ship: Ship):
        if ship in self.ship_history:
            return False
        else:
            self.ship_history.append(ship)
            return True
        
    def serialize(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "containers": [container.serialize() for container in self.containers],
            "current_ships": [ship.serialize_ship() for ship in self.current_ships],
        }
        return data
    
    def serialize_input(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "containers": [container.serialize() for container in self.containers],
        }
        return data


