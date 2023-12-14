from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models


class ShipRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_ships(self, ship) -> models.Ship:
        db_ship = models.Ship(id=ship.id,
                              port_id=ship.port_id,
                              title=ship.title,
                              type=str(ship.__class__.__name__),
                              total_weight_capacity=ship.total_weight_capacity,
                              max_number_of_all_containers=ship.max_number_of_all_containers,
                              max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
                              max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
                              max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
                              fuel_consumption_per_km=ship.fuel_consumption_per_km,
                              fuel=ship.fuel)
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)
        return db_ship

    def get_by_id(self, ship_id: int) -> models.Ship:
        ship = self.db_session.execute(
            select(models.Ship).filter(models.Ship.id == ship_id)
        )
        return ship.scalars().first()

    def get_all_ships(self):
        ships = self.db_session.execute(select(models.Ship).order_by(models.Ship.id))
        return ships.scalars().all()

    def update_ships(self, ship) -> None:
        ship_update = update(models.Ship).where(
            models.Ship.id == ship.id
        ).values(
            title=ship.title,
            fuel=ship.fuel,
            total_weight_capacity=ship.total_weight_capacity,
            max_number_of_all_containers=ship.max_number_of_all_containers,
            max_number_of_basic_containers=ship.max_number_of_basic_containers,
            max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
            max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
            max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
            fuel_consumption_per_km=ship.fuel_consumption_per_km,
            port_id=ship.port_id,
        )
        ship_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(ship_update)
        self.db_session.commit()
        return

    def delete_ship(self, ship_id: int) -> None:
        ship_delete = delete(models.Ship).where(
            models.Ship.id == ship_id
        )
        self.db_session.execute(ship_delete)
        self.db_session.commit()
