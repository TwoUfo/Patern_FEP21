from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from app.schemas.port import Port
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
import random

router = APIRouter()

@router.put("/{port_id}", response_model=Port, status_code=status.HTTP_200_OK)
def update_port(
    port_id: int = Path(..., title="The ID of the port to update"),
    port: Port = Depends(),
    db: Session = Depends(get_db)
):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=port_id)

    if not db_port:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Port not found",
        )


    db_port.title = port.title
    db_port.latitude = port.latitude
    db_port.longitude = port.longitude

    port_crud.update(db_port)
    return db_port

@router.delete("/{port_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_port(port_id: int, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=port_id)

    if not db_port:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Port not found",
        )

    for ship in db_port.ships:
        db.delete(ship)
        db.commit()

    port_crud.delete_port(port_id=port_id)

    return None
