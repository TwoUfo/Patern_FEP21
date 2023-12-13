from typing import Dict, Any, Union

from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_db
from app.db.repositories.ships import ShipRepository
from app.schemas.ship import Ship
from app.services.ship_serv import ShipFactory
from sqlalchemy.orm import Session  
from app.db.repositories.ports import PortRepository
from app.services.port_serv import PortFactory

router = APIRouter()


@router.post("/", response_model=Ship, status_code=status.HTTP_201_CREATED)
def create_ship(ship_data: Ship, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    print(ship_data)
    ship = ShipFactory().create_ship(ship_data)
    if db_ship:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Port already exist"
        )
    db_ship = ship_crud.create_ships(ship=ship)
    return db_ship


@router.get("/", response_model=Ship,
            status_code=status.HTTP_200_OK)
def get_ship_by_id(ship_id: int, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    ship = ship_crud.get_by_id(ship_id=ship_id)

    if ship is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ship not found"
        )
    return ship


@router.put("/", response_model=Ship,
            status_code=status.HTTP_200_OK)
def update_ship(ship: Ship, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    existing_ship = ship_crud.get_by_id(ship_id=ship.id)
    if not existing_ship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ship not found"
        )
    ship_crud.update_ship(ship=ship)
    return ship


@router.delete("/", response_model=Ship,
               status_code=status.HTTP_200_OK)
def delete_ship(ship_id: int, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    return ship_crud.delete_ship(ship_id)

@router.put("/{ship_id}/sail", response_model=Ship, status_code=status.HTTP_200_OK)
def sail_ship(ship_id: int, port_to_go_id: int, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    ship_model = ship_crud.get_by_id(ship_id=ship_id)
    if not ship_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ship not found"
        )

    ship = ShipFactory().create_ship(ship_model.__dict__)

    port_crud = PortRepository(db_session=db)
    port_model = port_crud.get_by_id(port_id=port_to_go_id)
    if not port_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Port not found"
        )

    port = PortFactory.create_port(port_model.__dict__)

    ship.sail_to(port_id=port.id)
    
    ship_crud.update_ships(ship)
    # port_crud.update_port(curr_port)
    # port_crud.update_port(port_to_go)
    return ship
