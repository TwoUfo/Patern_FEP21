from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class TablePort(Base):
    __tablename__ = "Ports"

    id = Column("id", String, primary_key=True)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)

    def __init__(self, id: str, latitude: float, longitude: float):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude


class TableShip(Base):
    __tablename__ = "Ships"

    id = Column("id", String, primary_key=True)
    port_id = Column("port_id", String, ForeignKey('Ports.id'))
    fuel = Column("fuel", Integer)
    total_weight_capacity = Column("total_weight_capacity", Integer)
    max_all_cont = Column("max_all_cont", Integer)
    max_heavy_cont = Column("max_heavy_cont", Integer)
    max_refrigerated_cont = Column("max_refrigerated_cont", Integer)
    max_liquid_cont = Column("max_liquid_cont", Integer)
    fuel_consumption_per_km = Column("fuel_consumption_per_km", Integer)

    def __init__(self, id: str, fuel: int, port_id: str, total_weight_capacity: int, max_all_cont: int,
                 max_heavy_cont: int, max_refrigerated_cont: int, max_liquid_cont: int,
                 fuel_consumption_per_km: int):
        self.id = id
        self.fuel = fuel
        self.port_id = port_id
        self.total_weight_capacity = total_weight_capacity
        self.max_all_cont = max_all_cont
        self.max_heavy_cont = max_heavy_cont
        self.max_refrigerated_cont = max_refrigerated_cont
        self.max_liquid_cont = max_liquid_cont
        self.fuel_consumption_per_km = fuel_consumption_per_km

    port = relationship("TablePort")


engine = create_engine("sqlite:///input_data.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
