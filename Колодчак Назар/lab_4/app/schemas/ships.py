from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING
from pydantic import BaseModel
from sqlalchemy import Enum

from app.schemas.port import Port
from app.schemas.containers import *


class IShip(BaseModel, ABC):
    total_weight_capacity: int
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float

    id: int
    port_id: int
    title: str
    fuel: float
    containers: List[Container] = []

    @abstractmethod
    def sail_to(self, port_to_go: Port, db_session) -> None:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container: Container) -> None:
        pass

    @abstractmethod
    def unload(self, container: Container) -> None:
        pass

    class Config:
        from_attributes = True


from app.db.repositories.ship_repo import ShipRepository
from app.db.repositories.port_repo import PortRepository
from app.services.port_service import PortFactory


class LightWeightShip(IShip):

    def sail_to(self, port_to_go: Port, db_session) -> None:
        if self.port_id == port_to_go.id:
            pass
            # return 'Ship already is in this port'
        else:
            curr_port = PortFactory.create_port(
                PortRepository(db_session=db_session).get_by_id(port_id=self.port_id).__dict__)
            sailing_fuel_cost = curr_port.get_distance(port_to_go) * self.fuel_consumption_per_km
            print(sailing_fuel_cost)
            for container in self.containers:
                sailing_fuel_cost += container.consumption()
            if sailing_fuel_cost < self.fuel:
                curr_port.outgoing_ship(self.id)
                port_to_go.incoming_ship(self.id)
                self.port_id = port_to_go.id
                self.fuel -= sailing_fuel_cost


                ShipRepository(db_session=db_session).update_ship(self)
                PortRepository(db_session=db_session).update_port(curr_port)
                PortRepository(db_session=db_session).update_port(port_to_go)
                # return '<-Ship starts going to new Port->'
            else:
                pass
                # return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: Container) -> None:
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                # return '<-Container is loaded on Ship->'
            else:
                pass
                # return '<-Ship is full and can`t load anymore Containers->'
        else:
            pass
            # return '<-This Container is in another port->'

    def unload(self, container: Container) -> None:
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            # return '<-Container is unloaded from Ship->'
        else:
            pass
            # return '<-This Container is Not on this Ship->'

    def get_current_containers(self) -> list:
        return self.containers


class MediumWeightShip(IShip):
    def sail_to(self, port_to_go: Port) -> None:
        if self.port.id == port_to_go.id:
            pass
            # return 'Ship already is in this port'
        else:
            curr_port = PortRepository().get_by_id(port_id=self.port_id)
            sailing_fuel_cost = curr_port.get_distance(port_to_go) * self.fuel_consumption_per_km

            for container in self.containers:
                if isinstance(container, RefrigeratedContainer) or isinstance(container, LiquidContainer):
                    if not container.items:
                        for con in self.containers:
                            sailing_fuel_cost += con.consumption()
                        if sailing_fuel_cost < self.fuel:
                            curr_port.outgoing_ship(self.id)
                            port_to_go.incoming_ship(self.id)
                            self.port_id = port_to_go.id
                            self.fuel -= sailing_fuel_cost

                            ShipRepository.update_ship(self)
                            PortRepository.update_port(curr_port)
                            PortRepository.update_port(port_to_go)
                            break
                            # return '<-Ship starts going to new Port->'
            else:
                pass
                # return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: Container) -> None:
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                # return '<-Container is loaded on Ship->'
            else:
                pass
                # return '<-Ship is full and can`t load anymore Containers->'
        else:
            pass
            # return '<-This Container is in another port->'

    def unload(self, container: Container) -> None:
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            # return '<-Container is unloaded from Ship->'
        else:
            pass
            # return '<-This Container is Not on this Ship->'

    def get_current_containers(self) -> list:
        return self.containers


class HeavyWeightShip(IShip):
    def sail_to(self, port_to_go: Port) -> None:
        if self.port.id == port_to_go.id:
            pass
            # return 'Ship already is in this port'
        else:
            curr_port = PortRepository().get_by_id(port_id=self.port_id)
            sailing_fuel_cost = curr_port.get_distance(port_to_go) * self.fuel_consumption_per_km

            for container in self.containers:
                if isinstance(container, RefrigeratedContainer) or isinstance(container, LiquidContainer):
                    if not container.items:
                        for con in self.containers:
                            sailing_fuel_cost += con.consumption()
                        if sailing_fuel_cost < self.fuel:
                            curr_port.outgoing_ship(self.id)
                            port_to_go.incoming_ship(self.id)
                            self.port_id = port_to_go.id
                            self.fuel -= sailing_fuel_cost

                            ShipRepository.update_ship(self)
                            PortRepository.update_port(curr_port)
                            PortRepository.update_port(port_to_go)
                            break
                            # return '<-Ship starts going to new Port->'
            else:
                pass
                # return '<-The Ship does\'nt have enough fuel to sail->'

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, container: Container) -> None:
        if container in self.port.containers:
            if self.configs.max_number_of_all_containers >= len(self.containers) + 1:
                self.containers.append(container)
                self.port.containers.remove(container)
                # return '<-Container is loaded on Ship->'
            else:
                pass
                # return '<-Ship is full and can`t load anymore Containers->'
        else:
            pass
            # return '<-This Container is in another port->'

    def unload(self, container: Container) -> None:
        if container in self.containers:
            self.containers.remove(container)
            self.port.containers.append(container)
            # return '<-Container is unloaded from Ship->'
        else:
            pass
            # return '<-This Container is Not on this Ship->'

    def get_current_containers(self) -> list:
        return self.containers
