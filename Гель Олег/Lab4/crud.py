from sqlalchemy.orm import Session
from models import Port, Ship, Container
from schemas import PortCreate, ShipCreate, ContainerCreate

def create_port(db: Session, port: PortCreate):
    db_port = Port(**port.dict())
    db.add(db_port)
    db.commit()
    db.refresh(db_port)
    return db_port

def get_port(db: Session, port_id: int):
    return db.query(Port).filter(Port.id == port_id).first()

def create_ship(db: Session, ship: ShipCreate):
    db_ship = Ship(**ship.dict())
    db.add(db_ship)
    db.commit()
    db.refresh(db_ship)
    return db_ship

def get_ship(db: Session, ship_id: int):
    return db.query(Ship).filter(Ship.id == ship_id).first()

def create_container(db: Session, container: ContainerCreate):
    db_container = Container(**container.dict())
    db.add(db_container)
    db.commit()
    db.refresh(db_container)
    return db_container

def get_container(db: Session, container_id: int):
    return db.query(Container).filter(Container.id == container_id).first()
