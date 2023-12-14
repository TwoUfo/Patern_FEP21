from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from typing import List

Base = declarative_base()


class Port(Base):
    __tablename__ = "ports"

    id: int = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    # items = relationship("Item", back_populates="port")
    # containers = relationship("Container", back_populates="port")
    # ships = relationship("Ship", back_populates="port")


class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, index=True)
    fuel = Column(Float, nullable=False)
    total_weight_capacity = Column(Integer, nullable=False)
    max_number_of_all_containers = Column(Integer, nullable=False)
    max_number_of_basic_containers = Column(Integer, nullable=False)
    max_number_of_heavy_containers = Column(Integer, nullable=False)
    max_number_of_refrigerated_containers = Column(Integer, nullable=False)
    max_number_of_liquid_containers = Column(Integer, nullable=False)
    fuel_consumption_per_km = Column(Integer, nullable=False)
    # containers = relationship("Container", back_populates="ship")
    port_id = Column(Integer, ForeignKey("ports.id"))
    # port = relationship("Port", back_populates="ships")

    __mapper_args__ = {
        'polymorphic_identity': 'ships',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f'Ship(title={self.title})'


class LightWeightShip(Ship):
    __tablename__ = 'light_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'LightWeightShip',
    }


class MediumWeightShip(Ship):
    __tablename__ = 'medium_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'MediumWeightShip',
    }


class HeavyWeightShip(Ship):
    __tablename__ = 'heavy_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'HeavyWeightShip',
    }

# class Container(Base):
#     __tablename__ = "containers"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(80), nullable=False, unique=True, index=True)
#     weight = Column(Float, nullable=False)
#     consumption = Column(Float, nullable=False)
#     items_id = Column(Integer, ForeignKey("items.id"))
#     port_id = Column(Integer, ForeignKey("ports.id"))
#     ship_id = Column(Integer, ForeignKey("ships.id"))
#     port = relationship("Port", back_populates="containers")
#     ship = relationship("Ship", back_populates="containers")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(80), nullable=False, unique=True, index=True)
#     weight = Column(Float, nullable=False, unique=True)
#     count = Column(Float, nullable=False, unique=True)
#     container_id = Column(Integer, ForeignKey("containers.id"))
#     port = relationship("Port", back_populates="items")
#
#     def __repr__(self):
#         return f'Item(title={self.title})'
