from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.db.repositories.containers import ContainerRepository
from app.schemas.containers import Container


class IShip(BaseModel):
    title:str
    type_:str
    fuel:int
    total_weight_capacity: float
    max_number_of_all_containers: int
    max_number_of_basic_containers: int
    max_number_of_heavy_containers: int
    max_number_of_refrigerated_containers: int
    max_number_of_liquid_containers: int
    fuel_consumption_per_km: float
    port_id: int
    port_deliver_id : int
    id: int



    def sail_to(self, distance: float) -> bool:
        if distance >= 1000:
            self.port_id = self.port_deliver_id
            self.port_deliver_id = 0
            return True
        else:
            return False

    def refuel(self, amount_of_fuel: float) -> None:
        self.fuel += amount_of_fuel

    def load(self, db: Session, container: Container) -> bool:
        container_crud = ContainerRepository(db)
        container.port_id = None
        container.ship_id = self.id
        container_crud.update_container(container)

        return True

    def unload(self, db: Session, container: Container) -> bool:
        container_crud = ContainerRepository(db)
        container.port_id = self.port_id
        container.ship_id = None
        container_crud.update_container(container)

        return True


    class Config:
        orm_mode = True
        from_attributes = True


class LightWeightShip(IShip):
    pass


class MediumShip(IShip):
    pass


class HeavyShip(IShip):
    pass

