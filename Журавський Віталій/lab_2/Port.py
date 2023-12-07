from abc import ABC, abstractmethod
from dataclasses import dataclass
from Ship import Ship
from uuid import uuid4
from haversine import haversine

@dataclass
class DataPort:
    basic: int
    heavy: int
    refrigerated: int
    liquid: int


class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, s: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, s: Ship):
        pass


class Port(IPort):
    def __init__(self, latitude: float, longitude: float, data):
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.data = data
        self.containers = []
        self.ship_history = []
        self.current_ships = []

    def got_distance(self, port) -> float:
        dist = haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, s: Ship):
        self.current_ships.append(s)

    def outgoing_ship(self, s: Ship):
        self.ship_history.append(s)


