from dataclasses import dataclass
from abc import ABC, abstractmethod
import uuid


class IShip(ABC):
    @abstractmethod
    def sail_to(self, p1, p2, p3):
        pass

    @abstractmethod
    def re_fuel(self, new_fuel: float):
        pass

    @abstractmethod
    def load(self, cont):
        pass

    @abstractmethod
    def unload(self, cont):
        pass


@dataclass
class DataShip:
    total_weight_capacity: int
    maxNumberOfAllContainers: int
    maxNumberOfBasicContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float


class Ship(IShip):
    def __init__(self, id: str, fuel: float, current_port, ships_data: DataShip):
        self.id = id
        self.fuel = fuel
        self.current_port = current_port
        self.containers = []
        self.ships_data = ships_data
        self.total_weight = 0
        self.total_containers_types = []
        self.total_containers_consumption = 0

    def get_current_containers(self):
        sorted_containers = sorted(self.containers, key=lambda cont_id: uuid.UUID(cont_id))
        i = 1
        if len(self.containers) > 0:
            for container in sorted_containers:
                print(f"Container #{i}: {container}")
                i += 1
            return ''
        else:
            return 'There are no containers on the ship'

    def sail_to(self, p1, p2, p3):
        total_fuel_needed1 = self.ships_data.fuelConsumptionPerKM*p1.get_distance(p2) + self.total_containers_consumption
        if self.id in p1.ship_current and total_fuel_needed1 <= self.fuel:
            if self.id not in p1.ship_history:
                p1.outgoing_ship(self)
            p2.incoming_ship(self)
            self.fuel -= total_fuel_needed1
            return 'Ship has successfully sailed to another port'
        elif self.id not in p1.ship_current:
            return 'There is no such ship in this port'
        elif self.id in p1.ship_current and total_fuel_needed1 > self.fuel:
            total_fuel_needed2 = self.ships_data.fuelConsumptionPerKM*p1.get_distance(p3) + self.total_containers_consumption
            if total_fuel_needed2 <= self.fuel:
                if self.id not in p1.ship_history:
                    p1.outgoing_ship(self)
                p3.incoming_ship(self)
                self.fuel -= total_fuel_needed2
                total_fuel_needed1 = self.ships_data.fuelConsumptionPerKM*p3.get_distance(p2) + self.total_containers_consumption
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(1000)
                if self.id not in p3.ship_history:
                    p3.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                return 'Ship has successfully sailed to intermediate port to refuel and sailed to wanted port'
            elif total_fuel_needed2 > self.fuel:
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(1000)
                if self.id not in p1.ship_history:
                    p1.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                return 'Ship has successfully sailed to another port after refueling in the starting port'

    def re_fuel(self, new_fuel: float):
        self.fuel += new_fuel

    def load(self, cont):
        if cont.id in self.current_port.containers:
            if (len(self.containers) < self.ships_data.maxNumberOfAllContainers
                    and cont.id not in self.containers):
                if (self.total_containers_types.count('Basic') <= self.ships_data.maxNumberOfBasicContainers
                        and self.total_containers_types.count('Heavy') <= self.ships_data.maxNumberOfHeavyContainers
                        and self.total_containers_types.count('Refrigerated') <= self.ships_data.maxNumberOfRefrigeratedContainers
                        and self.total_containers_types.count('Liquid') <= self.ships_data.maxNumberOfLiquidContainers):
                    self.containers.append(cont.id)
                    self.total_weight += cont.weight
                    self.total_containers_consumption += cont.consumption()
                    self.total_containers_types.append(cont.type)
                    self.current_port.containers.remove(cont.id)
                    if self.total_weight < self.ships_data.total_weight_capacity:
                        return f"{cont.type} container has been loaded on the ship"
                    else:
                        self.containers.remove(cont.id)
                        self.total_weight -= cont.weight
                        self.total_containers_types.remove(cont.type)
                        self.current_port.containers.append(cont.id)
                        return "Current ship's weight exceeded max weight cap"
                else:
                    return "Max amount of containers was reached"
            else:
                return "Max amount of containers was reached"
        else:
            return False

    def unload(self, cont):
        if cont.id in self.containers:
            self.containers.remove(cont.id)
            self.current_port.containers.append(cont.id)
            self.total_weight -= cont.weight
            self.total_containers_consumption -= cont.consumption()
            self.total_containers_types.remove(cont.type)
            return f"{cont.type} container has been unloaded from the ship"
        else:
            return False



