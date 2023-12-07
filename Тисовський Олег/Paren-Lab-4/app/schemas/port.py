from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
import haversine as hs

from app.schemas.containers import *
from app.schemas.items import *


class IPort(BaseModel, ABC):
    """Basic abstraction"""

    id: int

    @abstractmethod
    def incoming_ship(self, ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship):
        pass

    @abstractmethod
    def load_item_to_container(self, item: Item, container: Container):
        pass

    class Config:
        from_attributes = True


class Port(IPort):
    """Implements port logic"""
    latitude: float
    longitude: float
    title: str
    items: List[Item] = []
    containers: List[Container] = []
    ship_history: List[int] = []
    current_ships: List[int] = []

    def get_distance(self, port_to_go) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port_to_go.latitude, port_to_go.longitude))
        return dist

    def incoming_ship(self, ship_id) -> None:
        if ship_id not in self.current_ships:
            self.current_ships.append(ship_id)

    def outgoing_ship(self, ship_id) -> None:
        if ship_id in self.current_ships:
            self.current_ships.remove(ship_id)
            self.ship_history.append(ship_id)

    def load_item_to_container(self, item: Item, container: Container) -> None:
        if container in self.containers and item in self.items:
            if container.weight + item.get_total_weight() <= container.get_max_weight():
                container.items.append(item)
                self.items.remove(item)
                # return '<-This Item was loaded in Container->'
            else:
                pass
                # return '<-This Item to heavy to load in Container->'
        else:
            pass
            # return '<-Item and Container are in different Ports->'
