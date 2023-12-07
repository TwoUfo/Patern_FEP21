from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import mapped_column, Mapped
from app.db.database import Base




class Items(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    type = Column(String(80), nullable=False)
    weight = Column(Float, nullable=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"), nullable=True)



class Container(Base):
    __tablename__ = "containers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    type = Column(String(80), nullable=False)
    weight = Column(Float, nullable=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"), nullable=True)
    ship_id: Mapped[int] = mapped_column(ForeignKey("ships.id"), nullable=True)


class Port(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    basic = Column(Integer, nullable=False)
    heavy = Column(Integer, nullable=False)
    refrigerated = Column(Integer, nullable=False)
    liquid = Column(Integer, nullable=False)
    basic_items = Column(Integer, nullable=False)
    heavy_items = Column(Integer, nullable=False)
    refrigerated_items = Column(Integer, nullable=False)
    liquid_items = Column(Integer, nullable=False)

    ships = relationship("Ship", back_populates="port", foreign_keys="[Ship.port_id]")




class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String(80), nullable=True, unique=True, index=True)
    type_ = Column(String(30), nullable=False, unique=False, index=True)
    fuel = Column(Integer, nullable=True, unique=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"))
    port_deliver_id: Mapped[int] = mapped_column(ForeignKey("ports.id"), nullable=True)
    total_weight_capacity = Column(Integer, nullable=False, unique=False)
    max_number_of_all_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_basic_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_heavy_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_refrigerated_containers = Column(Integer, nullable=False, unique=False)
    max_number_of_liquid_containers = Column(Integer, nullable=False, unique=False)
    fuel_consumption_per_km = Column(Integer, nullable=False, unique=False)

    port = relationship("Port", back_populates="ships", foreign_keys=[port_id])

