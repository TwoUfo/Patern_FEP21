from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy.exc import NoResultFound
from app.models import models
from app.schemas.ship import IShip


class ShipRepository:
    def __init__(self, db_session: Session) ->None:
        self.db_session = db_session


    def create_ship(self, ship: IShip) -> models.Ship:
        db_ship = models.Ship(id=ship.id, title=ship.title, type_=ship.type_, fuel=ship.fuel, port_id=ship.port_id,
                              port_deliver_id=ship.port_deliver_id, total_weight_capacity=ship.total_weight_capacity,
                              max_number_of_all_containers=ship.max_number_of_all_containers,
                              max_number_of_basic_containers=ship.max_number_of_basic_containers,
                              max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
                              max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
                              max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
                              fuel_consumption_per_km=ship.fuel_consumption_per_km)
        self.db_session.add(db_ship)
        self.db_session.commit()
        self.db_session.refresh(db_ship)

        return db_ship

    def get_by_id(self, ship_id: int) -> models.Ship:
        return self.db_session.query(models.Ship).filter(models.Ship.id == ship_id).first()

    def get_all_ships(self) -> list[models.Ship]:
        ships = self.db_session.query(models.Ship).order_by(models.Ship.id).all()
        return ships



    def delete_ship(self, ship_id: int) -> None:
        try:

            ship_to_delete = (
                self.db_session.query(models.Ship)
                .filter(models.Ship.id == ship_id)
                .one()
            )

            self.db_session.delete(ship_to_delete)
            self.db_session.commit()

        except NoResultFound:
            raise Exception(f"Ship with id {ship_id} not found in the database.")


    def update_ship(self, ship: IShip) -> models.Ship:
        ship_update = (update(models.Ship)
        .values(
            title=ship.title, type_=ship.type_, fuel=ship.fuel, port_id=ship.port_id,
            port_deliver_id=ship.port_deliver_id, total_weight_capacity=ship.total_weight_capacity,
            max_number_of_all_containers=ship.max_number_of_all_containers,
            max_number_of_basic_containers=ship.max_number_of_basic_containers,
            max_number_of_heavy_containers=ship.max_number_of_heavy_containers,
            max_number_of_refrigerated_containers=ship.max_number_of_refrigerated_containers,
            max_number_of_liquid_containers=ship.max_number_of_liquid_containers,
            fuel_consumption_per_km=ship.fuel_consumption_per_km
        )
        .where(
            models.Ship.id == ship.id
        ))
        ship_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(ship_update)
        self.db_session.commit()
        return ship

    def sail_to(self, ship: IShip) -> bool:
        distance = ship.fuel / ship.fuel_consumption_per_km
        if distance >= 1000:
            ship_update = (
                update(models.Ship)
                .values(
                    port_id=ship.port_deliver_id,
                    port_deliver_id=0,
                )
                .where(models.Ship.id == ship.id)
                .returning(models.Ship)
            )
            updated_ship = self.db_session.execute(ship_update).fetchone()

            if updated_ship:
                return True
        return False