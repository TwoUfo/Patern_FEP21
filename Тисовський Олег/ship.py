from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class ConfigShip:
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float


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

    def __init__(self, port, ship_config: ConfigShip = None, fuel: float = 0.0) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        return self.containers

    def sail_to(self, port_to_go):
        sailing_fuel_cost = self.port.get_distance(port_to_go) * self.configs.fuel_consumption_per_km
        for container in self.containers:
            sailing_fuel_cost += container.consumption()
        if self.port is port_to_go:
            print('Ship already is in this port')
        else:
            if sailing_fuel_cost < self.fuel:
                print('<-Ship starts going to new Port->')
                self.port.outgoing_ship(self)
                port_to_go.incoming_ship(self)
                self.port = port_to_go
                self.fuel -= sailing_fuel_cost
            else:
                print('<-The Ship does\'nt have enough fuel to sail->')

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container):
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                print('<-Container is loaded on Ship->')
            else:
                print('<-Ship is full and can`t load anymore Containers->')
        else:
            print('<-This Container is in another port->')

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            print('<-Container is unloaded from Ship->')
        else:
            print('<-This Container is Not on this Ship->')
