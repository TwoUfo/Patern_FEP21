from app.models import models
from app.schemas.port import Port
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound


class PortRepository:

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_port(self, port: Port) -> models.Port:
        db_port = models.Port(
            id=port.id,
            title=port.title,
            longitude=port.longitude,
            latitude=port.latitude,
            basic=port.basic,
            heavy=port.heavy,
            refrigerated=port.refrigerated,
            liquid=port.liquid,
            basic_items=port.basic_items,
            heavy_items=port.heavy_items,
            refrigerated_items=port.refrigerated_items,
            liquid_items=port.liquid_items
        )
        self.db_session.add(db_port)
        self.db_session.commit()
        self.db_session.refresh(db_port)
        return db_port

    def get_by_id(self, port_id: int) -> models.Port:
        port = self.db_session.execute(
            select(models.Port).filter(models.Port.id == port_id)
        )
        return port.scalars().first()

    def get_port_name_by_id(self, port_id: int) -> str:
        port = self.db_session.query(models.Port).filter(models.Port.id == port_id).first()
        return port.title if port else None

    def get_all_ports(self):
        ports = self.db_session.execute(select(models.Port).order_by(models.Port.id)).scalars().all()
        return ports


    def delete_port(self, port_id: int) -> None:
        try:
            port_to_delete = (
                self.db_session.query(models.Port)
                .filter(models.Port.id == port_id)
                .one()
            )

            self.db_session.delete(port_to_delete)
            self.db_session.commit()

        except NoResultFound:
            raise Exception(f"Port with id {port_id} not found in the database.")


    def update(self, port: Port) -> models.Port:
        port_update = (
            update(models.Port)
            .values(
                id=port.id,
                title=port.title,
                longitude=port.longitude,
                latitude=port.latitude,
                basic=port.basic,
                heavy=port.heavy,
                refrigerated=port.refrigerated,
                liquid=port.liquid,
                basic_items=port.basic_items,
                heavy_items=port.heavy_items,
                refrigerated_items=port.refrigerated_items,
                liquid_items=port.liquid_items
            )
            .where(
                models.Port.id == port.id
            )
        )
        port_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(port_update)
        self.db_session.commit()
        return port

