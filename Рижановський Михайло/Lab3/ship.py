from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
from containers import Container, BasicContainer

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
    """Ship implementation"""

    def __init__(self, port, port_deliver, ship_config: ConfigShip, fuel: float = 0.0) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        return self.containers

    def sail_to(self, port) -> bool:
        if self.port and port != self.port:
            if self.port.outgoing_ship(self):
                self.port = port
            return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: Container) -> bool:
        if isinstance(container, Container):
            if len(self.containers) < self.configs.maxNumberOfAllContainers:
                self.containers.append(container)
                return True
        return False

    def unload(self, container: Container) -> bool:
        if isinstance(container, Container) and container in self.containers:
            self.containers.remove(container)
            return True
        return False


    def serialize_ship(self):
        data = {
            "type": self.__class__.__name__,
            "id": str(self.id),
            "fuel": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data

class LightWeightShip(Ship):

    def sail_to(self, port) -> bool:
        if self.port and port != self.port:
            if self.port.outgoing_ship(self):
                self.port = port
            return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container) -> bool:
        self.containers.append(container)
        return True

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        else:
            return False
        
    def serialize_ship(self):
        data = {
            "type": "LightWeightShip",
            "id": str(self.id),
            "fuel": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data

class MediumShip(Ship):

    def sail_to(self, port) -> bool:
        if self.port and port != self.port:
            if self.port.outgoing_ship(self):
                self.port = port
            return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container) -> bool:
        self.containers.append(container)
        return True

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        else:
            return False
        
    def serialize_ship(self):
        data = {
            "type": "MediumShip",
            "id": str(self.id),
            "fuel": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data

class HeavyShip(Ship):

    def sail_to(self, port) -> bool:
        if self.port and port != self.port:
            if self.port.outgoing_ship(self):
                self.port = port
            return True
        return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container) -> bool:
        self.containers.append(container)
        return True

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        else:
            return False

    def serialize_ship(self):
        data = {
            "type": "HeavyShip",
            "id": str(self.id),
            "fuel": self.fuel,
            "port": self.port,
            "containers": [container.serialize() for container in self.containers],
        }
        return data

class ShipFactory:
    @staticmethod
    def create_ship(ship_type, ship_id, port, port_deliver, ship_config: ConfigShip, fuel: float):
        if ship_type == 'LightWeightShip':
            return LightWeightShip(port, port_deliver, ship_config, fuel)
        elif ship_type == 'MediumShip':
            return MediumShip(port, port_deliver, ship_config, fuel)
        elif ship_type == 'HeavyShip':
            return HeavyShip(port, port_deliver, ship_config, fuel)
        else:
            raise ValueError(f"Invalid item type: {ship_type}")
