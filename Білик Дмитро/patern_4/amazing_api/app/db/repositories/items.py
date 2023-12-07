from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import update
from app.models import models
from app.schemas.items import Item, BasicItem, HeavyItem, RefrigeratedItem, LiquidItem
from sqlalchemy.exc import NoResultFound


class ItemsRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_item(self, item: Item) -> models.Items:
        type_mapping = {
            BasicItem: "basic_item",
            HeavyItem: "heavy_item",
            RefrigeratedItem: "refrigerated_item",
            LiquidItem: "liquid_item",
        }

        item_type = type_mapping.get(type(item))
        if item_type is None:
            raise Exception("unknown item type")

        port_id = item.port_id if item.port_id != -1 else None

        db_item = models.Items(id=item.id, type=item_type, weight=item.weight, port_id=port_id)
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return db_item

    def get_by_id(self, item_id: int) -> models.Items:
        item = self.db_session.execute(
            select(models.Items).filter(models.Items.id == item_id)
        )
        return item.scalars().first()

    def get_all_items(self):
        items = self.db_session.execute(select(models.Items).order_by(models.Items.id))
        return items.scalars().all()

    def delete_item(self, item_id: int) -> None:
        try:
            item_to_delete = (
                self.db_session.query(models.Items)
                .filter(models.Items.id == item_id)
                .one()
            )


            self.db_session.delete(item_to_delete)
            self.db_session.commit()

        except NoResultFound:
            raise Exception(f"Item with id {item_id} not found in the database.")

    def update(self, item: Item) -> None:
        type_mapping = {
            BasicItem: "basic_item",
            HeavyItem: "heavy_item",
            RefrigeratedItem: "refrigerated_item",
            LiquidItem: "liquid_item",
        }

        item_type = type_mapping.get(type(item))
        if item_type is None:
            raise Exception("unknown item type")

        item_update = (
            update(models.Items)
            .values(type=item_type, weight=item.weight)
            .where(models.Items.id == item.id)
        )

        item_update.execution_options(synchronize_session="fetch")
        self.db_session.execute(item_update)
        self.db_session.commit()
