from abc import ABC, abstractmethod
from pydantic import BaseModel

from app.schemas.containers import Container
from app.db.repositories.ports import PortRepository


class IShip(BaseModel, ABC):
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    port_id: int
    id: int

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
        next_port = PortRepository.get_by_id(port_id)
        if self.port_id != port_id:
            if self.port.outgoing_ship(self):
                self.port_id = port_id
            return True
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


class MediumWeightShip(Ship):
    pass


class LightWeightShip(Ship):
    pass


class HeavyWeightShip(Ship):
    pass



