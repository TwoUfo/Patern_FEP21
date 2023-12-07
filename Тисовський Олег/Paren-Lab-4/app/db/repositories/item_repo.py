from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.future import select

from app.models import models
from app.schemas.items import Item


class ItemRepository:
    # Implements CRUD (Create, Read, Update and Delete) for port objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_item(self, item: Item) -> models.ItemModel:
        db_item = models.ItemModel(
            id=item.id,
            title=item.title,
            weight=item.weight,
            count=item.count,
            container_id=item.container_id
        )
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return db_item

    def get_by_id(self, item_id: int) -> models.ItemModel:
        item = self.db_session.execute(
            select(models.ItemModel).filter(models.ItemModel.id == item_id)
        )
        return item.scalars().first()

    def get_all_items(self):
        items = self.db_session.execute(select(models.ItemModel).order_by(models.ItemModel.id))
        return items.scalars().all()

    def update_item(self, item: Item) -> None:
        container_update = update(models.ItemModel).where(
            models.ItemModel.id == item.id
        )
        container_update.execution_options(
            synchronize_session="fetch"
        )
        self.db_session.execute(container_update)
        return

    def delete_item(self, item_id: int) -> None:
        item_delete = delete(models.ItemModel).where(
            models.ItemModel.id == item_id
        )
        self.db_session.execute(item_delete)
        self.db_session.commit()
