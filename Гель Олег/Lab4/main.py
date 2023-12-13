from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from crud import create_port, get_port, create_ship, get_ship, create_container, get_container
from models import Base
from schemas import PortCreate, ShipCreate, ContainerCreate
import logging

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.post("/ports/", response_model=PortCreate)
def create_port(port: PortCreate, db: Session = Depends(get_db)):
    return create_port(db=db, port=port)

@app.get("/ports/{port_id}", response_model=PortCreate)
def read_port(port_id: int, db: Session = Depends(get_db)):
    return get_port(db=db, port_id=port_id)
@app.post("/ships/", response_model=ShipCreate)
def create_ship(ship: ShipCreate, db: Session = Depends(get_db)):
    return create_ship(db=db, ship=ship)

@app.get("/ships/{ship_id}", response_model=ShipCreate)
def read_ship(ship_id: int, db: Session = Depends(get_db)):
    return get_ship(db=db, ship_id=ship_id)
@app.post("/containers/", response_model=ContainerCreate)
def create_container(container: ContainerCreate, db: Session = Depends(get_db)):
    return create_container(db=db, container=container)

@app.get("/containers/{container_id}", response_model=ContainerCreate)
def read_container(container_id: int, db: Session = Depends(get_db)):
    return get_container(db=db, container_id=container_id)
