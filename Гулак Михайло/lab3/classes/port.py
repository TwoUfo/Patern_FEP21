from abc import ABC, abstractmethod
from uuid import uuid4

import haversine as hs

from .ship import Ship


class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, ship: Ship):
        # * Should add ship to current
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        # * Should add ship to history if it is not already appended
        pass


class Port(IPort):
    def __init__(self, latitude: float = 0, longitude: float = 0) -> None:
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.items = []
        # Both contain unique instances of ships
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine(
            (self.latitude, self.longitude), (port.latitude, port.longitude)
        )

        return dist

    def incoming_ship(self, ship: Ship) -> None:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)

    def outgoing_ship(self, ship: Ship) -> None:
        if isinstance(ship, Ship) and ship not in self.ship_history:
            self.ship_history.append(ship)

    def __repr__(self):
        return (
            f"Port(id={self.id}, latitude={self.latitude}, longitude={self.longitude})"
        )
