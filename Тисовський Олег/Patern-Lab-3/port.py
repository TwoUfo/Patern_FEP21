from abc import ABC, abstractmethod
from uuid import uuid4
from ship import *
from containers import *
from item import *

import haversine as hs


class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass

    @abstractmethod
    def load_item_to_container(self, item: Item, container: Container) -> bool:
        pass


class Port(IPort):

    def __init__(self, latitude: float, longitude: float) -> None:
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.items = []
        self.ship_history = []
        self.current_ships = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship):
        if ship not in self.current_ships:
            self.current_ships.append(ship)
            return '<-Ship had arrived to new Port->'
        else:
            return '!-Error-!'

    def outgoing_ship(self, ship):
        if ship in self.current_ships:
            self.ship_history.append(ship)
            self.current_ships.remove(ship)
            return '<-Ship left current Port->'
        else:
            return '!-Error-!'

    def load_item_to_container(self, item, container):
        if container in self.containers and item in self.items:
            if container.weight + item.get_total_weight() <= container.get_max_weight():
                container.items.append(item)
                self.items.remove(item)
                return '<-This Item was loaded in Container->'
            else:
                return '<-This Item to heavy to load in Container->'
        else:
            return '<-Item and Container are in different Ports->'
