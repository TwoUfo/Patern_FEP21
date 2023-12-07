from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.db.database import get_db
from app.db.repositories.ports import PortRepository

from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=Port, status_code=status.HTTP_201_CREATED)
def create_ports(port: Port, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    db_port = port_crud.get_by_id(port_id=port.id)
    if db_port:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Port already exist"
        )
    db_port = port_crud.create_port(port=port)
    return db_port


@router.get("/", response_model=Port, status_code=status.HTTP_200_OK)
def get_port_by_id(port_id: int, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    port = port_crud.get_by_id(port_id)

    if port is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Port not found"
        )
    return port


@router.put("/", response_model=Port, status_code=status.HTTP_200_OK)
def update_port(port: Port, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    existing_port = port_crud.get_by_id(port_id=port.id)
    if not existing_port:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Port not found"
        )
    port_crud.update_port(port=port)
    return port


@router.delete("/", response_model=None, status_code=status.HTTP_200_OK)
def delete_port(port_id: int, db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    return port_crud.delete_port(port_id)
