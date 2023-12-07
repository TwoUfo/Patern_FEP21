from typing import Dict, Any, Union

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.db.database import get_db

from app.db.repositories.ship_repo import ShipRepository
from app.db.repositories.port_repo import PortRepository
from app.services.ship_service import LightWeightShip, MediumWeightShip, HeavyWeightShip, ShipFactory
from app.services.port_service import PortFactory

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Union[LightWeightShip, MediumWeightShip, HeavyWeightShip], status_code=status.HTTP_201_CREATED)
def create_ship(ship_data: Dict[str, Any], db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    db_ship = ship_crud.get_by_id(ship_id=ship_data.get('id'))
    if db_ship:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ship already exist"
        )
    print(ship_data)
    ship = ShipFactory().create_ship(ship_data)
    db_ship = ship_crud.create_ship(ship=ship)
    return db_ship


@router.get("/", response_model=list[Union[LightWeightShip, MediumWeightShip, HeavyWeightShip]], status_code=status.HTTP_200_OK)
def get_all_ships(db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)
    return ship_crud.get_all_ships()


@router.put("/", response_model=Union[LightWeightShip, MediumWeightShip, HeavyWeightShip], status_code=status.HTTP_200_OK)
def update_ship(ship_data: Dict[str, Any], db: Session = Depends(get_db)):
    ship_crud = ShipRepository(db_session=db)

    existing_ship = ship_crud.get_by_id(ship_id=ship_data.get('id'))

    if not existing_ship:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ship not found"
        )

    updated_ship = ShipFactory.create_ship(ship_data)
    ship_crud.update_ship(ship=updated_ship)

    return updated_ship


@router.put("/{ship_id}/sail", response_model=Union[LightWeightShip, MediumWeightShip, HeavyWeightShip], status_code=status.HTTP_200_OK)
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

    ship.sail_to(port_to_go=port, db_session=db)
    return ship
