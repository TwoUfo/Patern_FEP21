from abc import ABC, abstractmethod
from typing import List

import haversine as hs
from app.schemas.ship import IShip
from pydantic import BaseModel


class IPort(ABC, BaseModel):
    id: int

    @abstractmethod
    def incoming_ship(self, ship: IShip) -> bool:
        pass

    @abstractmethod
    def outgoing_ship(self, ship: IShip) -> bool:
        pass




class Port(IPort):
    latitude: float
    longitude: float
    basic: int
    heavy: int
    refrigerated: int
    liquid: int
    basic_items: int
    heavy_items: int
    refrigerated_items: int
    liquid_items: int
    title: str
    current_ships: List[int] = []

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: IShip) -> None:
        if isinstance(ship, IShip) and ship not in self.current_ships:
            self.current_ships.append(ship.id)

    def outgoing_ship(self, ship: IShip) -> None:
        if isinstance(ship, IShip) and ship.id in self.current_ships:
            self.ship_history.append(ship.id)

    class Config:
        orm_mode = True
        from_attributes = True