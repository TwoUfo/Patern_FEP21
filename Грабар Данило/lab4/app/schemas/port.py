from abc import ABC, abstractmethod
from typing import List
import haversine as hs
from pydantic import BaseModel

from app.schemas.items import Item
from app.schemas.containers import Container


class IPort(BaseModel, ABC):

    id: int

    @abstractmethod
    def incoming_ship(self, ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship):
        pass

    class Config:
        orm_mode = True


class Port(IPort):
    """Implements port logic"""
    latitude: float
    longitude: float
    title: str
    items: List[Item] = []
    containers: List[Container] = []
    ship_history: List[int] = []
    current_ships: List[int] = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship) -> None:
        if isinstance(ship) and ship not in self.current_ships:
            self.current_ships.append(ship.id)

    def outgoing_ship(self, ship) -> None:
        if isinstance(ship) and ship.id in self.current_ships:
            self.current_ships.remove(ship.id)
            self.ship_history.append(ship.id)

