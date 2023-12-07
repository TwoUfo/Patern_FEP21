from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship

from app.db.database import Base


class PortModel(Base):
    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    # items = relationship('ItemModel', back_populates='port')
    # containers = relationship('ContainerModel', back_populates='port')
    current_ships = relationship('ShipModel', back_populates='port')
    # ships_history: Mapped[List[IShip]] = relationship(back_populates="port")


class ShipModel(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    port_id = Column(Integer, ForeignKey('ports.id'))
    port = relationship('PortModel', back_populates='current_ships')
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    fuel = Column(Float, nullable=False, unique=False)
    total_weight_capacity = Column(Integer, nullable=False, unique=False)
    max_number_of_all_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_basic_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_heavy_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_refrigerated_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_liquid_containers = Column(Integer, nullable=False, unique=False)
    fuel_consumption_per_km = Column(Integer, nullable=False, unique=False)

    # containers = relationship('ContainerModel', back_populates='ship')

    __mapper_args__ = {
        'polymorphic_identity': 'ships',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f'Ship(title={self.title})'


class LightWeightShip(ShipModel):
    __tablename__ = 'light_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'LightWeightShip',
    }


class MediumWeightShip(ShipModel):
    __tablename__ = 'medium_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'MediumWeightShip',
    }


class HeavyWeightShip(ShipModel):
    __tablename__ = 'heavy_weight_ships'

    id = Column(Integer, ForeignKey('ships.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'HeavyWeightShip',
    }


#
# class ContainerModel(Base):
#     __tablename__ = 'containers'
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     title = Column(String(80), nullable=False, unique=True, index=True)
#     weight = Column(Float, nullable=False, unique=False)
#     items = relationship('ItemModel', back_populates='container')
#     port_id = Column(Integer, ForeignKey('ports.id'))
#     port = relationship('PortModel', back_populates='containers')
#     ship_id = Column(Integer, ForeignKey('ships.id'))
#     ship = relationship('ShipModel', back_populates='containers')

# class ItemModel(Base):
#     __tablename__ = 'items'
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     title = Column(String(80), nullable=False, unique=True, index=True)
#     weight = Column(Float, nullable=False, unique=False)
#     count = Column(Integer, nullable=False, unique=False)
#     port_id = Column(Integer, ForeignKey('ports.id'))
#     port = relationship('PortModel', back_populates='items')
#     container_id = Column(Integer, ForeignKey('containers.id'))
#     container = relationship('ContainerModel', back_populates='items')
