from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
import haversine as hs

from app.schemas.containers import Container
from app.schemas.items import Item

class IPort(BaseModel, ABC):
    id: int

    @abstractmethod
    def incoming_ship(self, ship_id: int) -> None:
        pass

    @abstractmethod
    def outgoing_ship(self, ship_id: int) -> None:
        pass

    @abstractmethod
    def load_item_to_container(self, item: Item, container: Container) -> None:
        pass

class Port(IPort):
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

    def incoming_ship(self, ship_id: int) -> None:
        if ship_id not in self.current_ships:
            self.current_ships.append(ship_id)

    def outgoing_ship(self, ship_id: int) -> None:
        if ship_id in self.current_ships:
            self.current_ships.remove(ship_id)
            self.ship_history.append(ship_id)

    def load_item_to_container(self, item: Item, container: Container) -> None:
        if container in self.containers and item in self.items:
            if container.weight + item.get_total_weight() <= container.get_max_weight():
                container.items.append(item)
                self.items.remove(item)
            else:
                pass  # <-This Item is too heavy to load in Container->
        else:
            pass  # <-Item and Container are in different Ports->
