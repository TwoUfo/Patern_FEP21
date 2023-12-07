from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
import random

@dataclass
class ConfigShip:
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
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
    def __init__(self, port, ship_config: ConfigShip, fuel: float = 0.0) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        return self.containers

    def sail_to(self, port) -> bool:
        if self.port and port != port:
            if self.port.outgoing_ship(self):
                self.port = port
            return True
        return False

    def refuel(self, amount_of_fuel: float) -> float:
        self.fuel += amount_of_fuel
        return self.fuel

    def load(self, container) -> bool:
        if len(self.containers) < self.configs.maxNumberOfAllContainers:
            self.containers.append(container)
            return True
        return False

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False
    
    
    def serialize_input(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "fuel": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data
    
    def serialize(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "fuel left:": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data
    
