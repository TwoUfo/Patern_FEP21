from abc import ABC, abstractmethod
from pydantic import BaseModel

from app.schemas.containers import Container
from app.db.repositories.ports import PortRepository


class IShip(BaseModel, ABC):
    id: int
    port_id: int
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    @abstractmethod
    def sail_to(self, port_id) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container: Container) -> bool:
        pass

    @abstractmethod
    def unload(self, container: Container) -> bool:
        pass

    class Config:
        orm_mode = True


class Ship(IShip):
    title: str
    fuel: float

    def sail_to(self, port_id) -> bool:
        if self.port_id != port_id:
            self.port_id = port_id
            # if self.port.outgoing_ship(self):
            # return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: Container) -> bool:
        if isinstance(container, Container):
            if len(self.containers) < self.max_number_of_all_containers:
                self.containers.append(container)
                return True
        return False

    def unload(self, container: Container) -> bool:
        if isinstance(container, Container) and container in self.containers:
            self.containers.remove(container)
            return True
        return False

    def get_total_weight(self):
        return self.total_weight_capacity


