from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .containers import (
    Container,
    HeavyContainer,
    RefrigeratedContainer,
    LiquidContainer,
)

import helpers


@dataclass
class ShipConfig:
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float


class IShip(ABC):
    @abstractmethod
    def sail_to(self, port):
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def unload(self):
        pass


@dataclass(repr=True)
class Ship(IShip):
    id: UUID = field(init=False, default=uuid4())
    current_weight: float = field(init=False, default=0)
    _configs: ShipConfig = None
    port: any = None
    fuel: float = 0
    containers: list = field(init=False, default_factory=list)

    @property
    def configs(self):
        return self._configs

    def _append_container(self, container: Container) -> bool:
        if not self._check_container_loadability(container):
            return False

        self._load_container(container)
        return True

    def _check_container_loadability(self, container: Container) -> bool:
        if self._is_fully_loaded() or self._is_overweight(container):
            return False

        if isinstance(container, HeavyContainer):
            if self._is_max_heavy_containers_exceeded():
                return False
            if (
                isinstance(container, RefrigeratedContainer)
                and self._is_max_refrigerated_containers_exceeded()
            ):
                return False
            if (
                isinstance(container, LiquidContainer)
                and self._is_max_liquid_containers_exceeded()
            ):
                return False

        return True

    def _is_fully_loaded(self) -> bool:
        return len(self.containers) + 1 > self.configs.max_number_of_all_containers

    def _is_overweight(self, container: Container) -> bool:
        return (
            self.current_weight + container.current_weight
            > self.configs.total_weight_capacity
        )

    def _is_max_heavy_containers_exceeded(self) -> bool:
        return (
            helpers.count_containers_by_type(self.containers, HeavyContainer) + 1
            > self.configs.max_number_of_heavy_containers
        )

    def _is_max_refrigerated_containers_exceeded(self) -> bool:
        return (
            helpers.count_containers_by_type(self.containers, RefrigeratedContainer) + 1
            > self.configs.max_number_of_refrigerated_containers
        )

    def _is_max_liquid_containers_exceeded(self) -> bool:
        return (
            helpers.count_containers_by_type(self.containers, LiquidContainer) + 1
            > self.configs.max_number_of_liquid_containers
        )

    def _load_container(self, container: Container) -> None:
        for item in self.port.items:
            is_loaded = container.load(item)
            if is_loaded:
                self.port.items.remove(item)

        self.containers.append(container)
        self.current_weight += container.current_weight

    def _unload_container(self) -> list:
        unloaded_items = []

        for container in self.containers:
            loaded_items = container.unload()
            unloaded_items.extend(loaded_items)

        return unloaded_items

    def _calc_consumption(self, port) -> float:
        distance = self.port.get_distance(port)
        fuel_for_containers_transportation = sum(
            [container.consumption() for container in self.containers]
        )

        consumption = (
            distance * self.configs.fuel_consumption_per_km
            + fuel_for_containers_transportation
        )

        return consumption

    def sail_to(self, port) -> bool:
        consumption = self._calc_consumption(port)

        if self.fuel == 0 or self.fuel < consumption:
            print(f"Ship can't sail to port with id {port.id}: not enough fuel")
            return False

        self.port.outgoing_ship(self)

        self.fuel -= consumption
        self.port = port

        port.incoming_ship(self)

        return True

    def refuel(self, amount_of_fuel: float) -> None:
        if amount_of_fuel <= 0:
            print(f"Amount of fuel must be at least grater than zero.")
            return

        self.fuel += amount_of_fuel

    def load(self) -> bool:
        for container in self.port.containers:
            is_loaded = self._append_container(container)

            if not is_loaded:
                return False

            self.port.containers.remove(container)

        return True

    def unload(self) -> bool:
        if len(self.containers) == 0:
            print("There are nothing to unload.")
            return False

        unloaded_items = self._unload_container()

        self.port.containers.extend(self.containers)
        self.port.items.extend(unloaded_items)
        self.containers.clear()

        return True

    @staticmethod
    def create(type: str):
        ship = None

        if type == "light":
            ship_config = ShipConfig(1000, 10, 2, 1, 1, 0.15)
            ship = LightWeightShip(ship_config)
        elif type == "medium":
            ship_config = ShipConfig(2500, 15, 5, 3, 2, 0.25)
            ship = MediumShip(ship_config)
        elif type == "heavy":
            ship_config = ShipConfig(5000, 20, 10, 5, 5, 0.4)
            ship = HeavyShip(ship_config)

        return ship


@dataclass(repr=True, eq=True)
class LightWeightShip(Ship):
    pass


@dataclass(repr=True, eq=True)
class MediumShip(Ship):
    pass


@dataclass(repr=True, eq=True)
class HeavyShip(Ship):
    pass
