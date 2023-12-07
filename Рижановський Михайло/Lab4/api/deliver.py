from typing import Dict, Any, Union

from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_db
from app.db.repositories.ships import ShipRepository
from app.schemas.ship import Ship
from app.services.ship_serv import ShipFactory
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Ship, status_code=status.HTTP_201_CREATED)
def create_ship(ship_data: Ship, db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    print(ship_data)
    ship = ShipFactory().create_ship(ship_data)
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
