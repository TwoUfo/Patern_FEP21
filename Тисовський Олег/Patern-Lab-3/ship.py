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

    def __init__(self, port, fuel: float = 0.0, ship_config: ConfigShip = None) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        return self.containers


class LightWeightShip(Ship):

    def __init__(self, port, fuel, ship_config):
        super().__init__(port, fuel, ship_config)

    def sail_to(self, port_to_go):
        sailing_fuel_cost = self.port.get_distance(port_to_go) * self.configs.fuel_consumption_per_km
        for container in self.containers:
            sailing_fuel_cost += container.consumption()
        if self.port is port_to_go:
            return 'Ship already is in this port'
        else:
            if sailing_fuel_cost < self.fuel:
                self.port.outgoing_ship(self)
                port_to_go.incoming_ship(self)
                self.port = port_to_go
                self.fuel -= sailing_fuel_cost
                return '<-Ship starts going to new Port->'
            else:
                return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container):
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                return '<-Container is loaded on Ship->'
            else:
                return '<-Ship is full and can`t load anymore Containers->'
        else:
            return '<-This Container is in another port->'

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            return '<-Container is unloaded from Ship->'
        else:
            return '<-This Container is Not on this Ship->'


class MediumShip(Ship):

    def __init__(self, port, fuel, ship_config):
        super().__init__(port, fuel, ship_config)

    def sail_to(self, port_to_go):
        sailing_fuel_cost = self.port.get_distance(port_to_go) * self.configs.fuel_consumption_per_km
        for container in self.containers:
            sailing_fuel_cost += container.consumption()
        if self.port is port_to_go:
            return 'Ship already is in this port'
        else:
            if sailing_fuel_cost < self.fuel:
                self.port.outgoing_ship(self)
                port_to_go.incoming_ship(self)
                self.port = port_to_go
                self.fuel -= sailing_fuel_cost
                return '<-Ship starts going to new Port->'
            else:
                return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container):
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                return '<-Container is loaded on Ship->'
            else:
                return '<-Ship is full and can`t load anymore Containers->'
        else:
            return '<-This Container is in another port->'

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            return '<-Container is unloaded from Ship->'
        else:
            return '<-This Container is Not on this Ship->'


class HeavyShip(Ship):

    def __init__(self, port, fuel, ship_config):
        super().__init__(port, fuel, ship_config)

    def sail_to(self, port_to_go):
        sailing_fuel_cost = self.port.get_distance(port_to_go) * self.configs.fuel_consumption_per_km
        for container in self.containers:
            sailing_fuel_cost += container.consumption()
        if self.port is port_to_go:
            return 'Ship already is in this port'
        else:
            if sailing_fuel_cost < self.fuel:
                self.port.outgoing_ship(self)
                port_to_go.incoming_ship(self)
                self.port = port_to_go
                self.fuel -= sailing_fuel_cost
                return '<-Ship starts going to new Port->'
            else:
                return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container):
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                return '<-Container is loaded on Ship->'
            else:
                return '<-Ship is full and can`t load anymore Containers->'
        else:
            return '<-This Container is in another port->'

    def unload(self, container):
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            return '<-Container is unloaded from Ship->'
        else:
            return '<-This Container is Not on this Ship->'