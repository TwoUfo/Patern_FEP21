from dataclasses import dataclass
from abc import ABC, abstractmethod
from uuid import uuid4

@dataclass
class DataShip:
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float

class IShip(ABC):
    @abstractmethod
    def sail_to(self, port):
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float):
        pass

    @abstractmethod
    def load(self, container):
        pass

    @abstractmethod
    def unload(self, container):
        pass

class Ship(IShip):
    def __init__(self, port, data_ship: DataShip, fuel: float = 0.0):
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.data = data_ship
        self.weight = 0
        self.containers = []

    def get_current_containers(self):
        return self.containers

    def sail_to(self, new_port):
        dist = self.port.got_distance(new_port)
        fuel_needed = self.data.fuelConsumptionPerKM * dist + self.weight

        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            self.port.outgoing_ship(self)
            self.port = new_port
            new_port.incoming_ship(self)
            return 'The ship docked at the new designated port'
        else:
            return 'The ship needs fuel!'

    def refuel(self, amount_of_fuel: float):
        if amount_of_fuel > 0:
            self.fuel += amount_of_fuel
            return f"Refueled | fuel: {self.fuel}"
        else:
            return 'Refuel error!'

    def load(self, container):
        if len(self.containers) < self.data.maxNumberOfAllContainers and self.weight+container.consumption() <= self.data.totalWeightCapacity:
            self.containers.append(container)
            self.weight += container.consumption()
            return f'Container loaded | count: {len(self.containers)} | weight of containers on the ship: {self.weight}'
        else:
            return f'Load error!'

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.weight -= container.consumption()
            return f'Container removed | count: {len(self.containers)} | weight of containers on the ship: {self.weight}'
        else:
            return f'Unload error!'
