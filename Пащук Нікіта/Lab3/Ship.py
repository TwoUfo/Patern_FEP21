from dataclasses import dataclass
from abc import ABC, abstractmethod


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
        self.items = []

    def get_current_containers(self):
        if len(self.containers) > 0:
            for container in self.containers:
                print(container.id)
        else:
            return 'There are no containers on the ship'

    def check_current_id(self, port):
        id_found = any(ship.id == self.id for ship in port.ship_current)
        return id_found

    def check_history_id(self, port):
        id_found = any(ship.id == self.id for ship in port.ship_history)
        return id_found

    def sail_to(self, *ports):
        p1, p2, p3 = ports
        total_fuel_needed1 = (self.ships_data.fuelConsumptionPerKM * p1.get_distance(p2) +
                              self.total_containers_consumption)
        if self.check_current_id(p1) and total_fuel_needed1 <= self.fuel:
            if not self.check_history_id(p1):
                p1.outgoing_ship(self)
            p2.incoming_ship(self)
            self.fuel -= total_fuel_needed1
            self.current_port = p2
            return 'Ship has successfully sailed to another port'

        elif not self.check_current_id(p1):
            return 'There is no such ship in this port'

        elif self.check_current_id(p1) and total_fuel_needed1 > self.fuel:
            total_fuel_needed2 = self.ships_data.fuelConsumptionPerKM * p1.get_distance(
                p3) + self.total_containers_consumption
            if total_fuel_needed2 <= self.fuel:
                if not self.check_history_id(p1):
                    p1.outgoing_ship(self)
                p3.incoming_ship(self)
                self.fuel -= total_fuel_needed2
                total_fuel_needed1 = self.ships_data.fuelConsumptionPerKM * p3.get_distance(
                    p2) + self.total_containers_consumption
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(100)
                if not self.check_history_id(p3):
                    p3.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                self.current_port = p2
                return 'Ship has successfully sailed to intermediate port to refuel and sailed to wanted port'

            elif total_fuel_needed2 > self.fuel:
                while self.fuel < total_fuel_needed1:
                    self.re_fuel(100)
                if not self.check_history_id(p1):
                    p1.outgoing_ship(self)
                p2.incoming_ship(self)
                self.fuel -= total_fuel_needed1
                self.current_port = p2
                return 'Ship has successfully sailed to another port after refueling in the starting port'

    def re_fuel(self, new_fuel: float):
        self.fuel += new_fuel

    def load(self, cont):
        max_counts = {
            'Basic': self.ships_data.maxNumberOfBasicContainers,
            'Heavy': self.ships_data.maxNumberOfHeavyContainers,
            'Refrigerated': self.ships_data.maxNumberOfRefrigeratedContainers,
            'Liquid': self.ships_data.maxNumberOfLiquidContainers,
        }
        found_cont_in_port = any(obj.id == cont.id for obj in self.current_port.containers)
        found_cont_on_ship = any(obj.id == cont.id for obj in self.containers)
        if found_cont_in_port:
            if (len(self.containers) < self.ships_data.maxNumberOfAllContainers
                    and not found_cont_on_ship):
                self.containers.append(cont)
                self.total_weight += cont.weight
                self.total_containers_consumption += cont.consumption()
                self.total_containers_types.append(cont.type)
                self.current_port.containers.remove(cont)
                if all(self.total_containers_types.count(container_type) <= max_count
                       for container_type, max_count in max_counts.items()):
                    if self.total_weight < self.ships_data.total_weight_capacity:
                        return f"{cont.type} container has been loaded on the ship"
                    else:
                        self.containers.remove(cont)
                        self.total_weight -= cont.weight
                        self.total_containers_consumption -= cont.consumption()
                        self.total_containers_types.remove(cont.type)
                        self.current_port.containers.append(cont)
                        return f"{cont.type} container hasn't been loaded on the ship: max weight cap reached"
                else:
                    self.containers.remove(cont)
                    self.total_weight -= cont.weight
                    self.total_containers_consumption -= cont.consumption()
                    self.total_containers_types.remove(cont.type)
                    self.current_port.containers.append(cont)
                    return (f"{cont.type} container hasn't been loaded on the ship: max amount "
                            f"of {cont.type} containers was reached")
            else:
                return f"{cont.type} container hasn't been loaded on the ship: max amount of all containers was reached"
        else:
            return False

    def unload(self, cont):
        found_cont_on_ship = any(obj.id == cont.id for obj in self.containers)
        if found_cont_on_ship:
            self.containers.remove(cont)
            self.current_port.containers.append(cont)
            self.total_weight -= cont.weight
            self.total_containers_consumption -= cont.consumption()
            self.total_containers_types.remove(cont.type)
            return f"{cont.type} container has been unloaded from the ship"
        else:
            return f"failed to unload {cont.id}"


class LightWeightShip(Ship):
    def __init__(self, id: str, fuel: float, current_port, ships_data: DataShip, ship_type):
        self.ship_type = ship_type
        super().__init__(id, fuel, current_port, ships_data)


class MediumShip(Ship):
    def __init__(self, id: str, fuel: float, current_port, ships_data: DataShip, ship_type):
        self.ship_type = ship_type
        super().__init__(id, fuel, current_port, ships_data)


class HeavyShip(Ship):
    def __init__(self, id: str, fuel: float, current_port, ships_data: DataShip, ship_type):
        self.ship_type = ship_type
        super().__init__(id, fuel, current_port, ships_data)


class MakeShip:

    @staticmethod
    def check_type(id: str, fuel: float, current_port, ships_data: DataShip):
        if ships_data.total_weight_capacity <= 20000:
            return LightWeightShip(id, fuel, current_port, ships_data, "Light")
        elif ships_data.total_weight_capacity <= 40000:
            return MediumShip(id, fuel, current_port, ships_data, "Medium")
        elif ships_data.total_weight_capacity <= 60000:
            return HeavyShip(id, fuel, current_port, ships_data, "Heavy")
