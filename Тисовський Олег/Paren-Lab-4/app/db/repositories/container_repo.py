from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models
from app.schemas.containers import Container


class ContainerRepository:
    # Implements CRUD (Create, Read, Update and Delete) for port objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_container(self, container: Container) -> models.ContainerModel:
        db_container = models.ContainerModel(
            id=container.id,
            title=container.title,
            weight=container.weight,
            items=container.items
        )
        self.db_session.add(db_container)
        self.db_session.commit()
        self.db_session.refresh(db_container)
        return db_container

    def get_by_id(self, port_id: int) -> models.ContainerModel:
        port = self.db_session.execute(
            select(models.ContainerModel).filter(models.ContainerModel.id == port_id)
        )
        return port.scalars().first()

    def get_all_containers(self):
        containers = self.db_session.execute(select(models.ContainerModel).order_by(models.Container.id))
        return containers.scalars().all()

    def update_container(self, container: Container) -> None:
        container_update = update(models.ContainerModel).where(
            models.ContainerModel.id == container.id
        )
        container_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(container_update)
        return

    def delete_container(self, container_id: int) -> None:
        container_delete = delete(models.ContainerModel).where(
            models.ContainerModel.id == container_id
        )
        self.db_session.execute(container_delete)
        self.db_session.commit()
