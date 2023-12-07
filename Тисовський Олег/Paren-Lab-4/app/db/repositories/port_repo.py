from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models
from app.schemas.port import Port


class PortRepository:
    # Implements CRUD (Create, Read, Update and Delete) for port objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_port(self, port: Port) -> models.PortModel:
        db_port = models.PortModel(
            id=port.id,
            title=port.title,
            longitude=port.longitude,
            latitude=port.latitude,
        )
        self.db_session.add(db_port)
        self.db_session.commit()
        self.db_session.refresh(db_port)
        return db_port

    def get_by_id(self, port_id: int) -> models.PortModel:
        port = self.db_session.execute(
            select(models.PortModel).filter(models.PortModel.id == port_id)
        )
        return port.scalars().first()

    def get_all_ports(self):
        ports = self.db_session.execute(select(models.PortModel).order_by(models.PortModel.id))
        return ports.scalars().all()

    def update_port(self, port: Port) -> None:
        port_update = update(models.PortModel).where(
            models.PortModel.id == port.id
        ).values(
            title=port.title,
            longitude=port.longitude,
            latitude=port.latitude
        )
        self.db_session.execute(port_update)
        self.db_session.commit()

    def delete_port(self, port_id: int) -> None:
        port_delete = delete(models.PortModel).where(
            models.PortModel.id == port_id
        )
        self.db_session.execute(port_delete)
        self.db_session.commit()
