from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class ConfigShip:
    total_weight_capacity: int
    max_number_of_all_containers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float


class IShip(ABC):

    @abstractmethod
    def sail_to(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass


class Ship(IShip):
    """Ship implementation"""

    def __init__(self, port, ship_config: ConfigShip, fuel: float = 0.0) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        # TODO: refactor
        self.containers = sorted(self.containers, key=lambda container: container.getID())
        return self.containers

    def sail_to(self, port) -> bool:
        if self.configs in port:
            return True 

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel = self.fuel + amount_of_fuel

    def load(self, container) -> bool:
        if container in self.configs:
            return True

    def unload(self, container) -> bool:
        if container not in self.configs:
            return True
