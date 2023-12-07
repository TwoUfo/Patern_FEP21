from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
from app.db.repositories.ships import ShipRepository
from app.db.repositories.containers import ContainerRepository
from app.schemas.deliver import DeliveryRequest, DeliveryResponse, DeliveryInfoResponse
from app.schemas.ship import IShip
from app.schemas.port import Port
from app.schemas.containers import Container
from typing import List

router = APIRouter()

@router.post("/", response_model=DeliveryResponse, status_code=status.HTTP_200_OK)
async def deliver_containers(request: DeliveryRequest, db: Session = Depends(get_db)):
    ship_repository = ShipRepository(db)
    port_repository = PortRepository(db)
    container_repository = ContainerRepository(db)


    ship: IShip = ship_repository.get_ship(request.ship_id)
    if not ship:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ship not found")


    port : Port = port_repository.get_by_id(ship.port_id)
    deliver_port = port_repository.get_by_id(ship.port_deliver_id)

    if not port or not deliver_port:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Port or Deliver Port not found")


    distance = port.get_distance(deliver_port)
    if not ship.sail_to(distance):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient fuel for the journey"
        )


    containers_to_load : Container = container_repository.get_containers_for_ship(request.ship_id, request.max_containers)
    for container in containers_to_load:
        ship.load(db, container)


    ship_repository.update_ship(ship)

    return DeliveryResponse(
        message=f"Containers delivered successfully to {deliver_port.title}",
        containers_delivered=len(containers_to_load),
    )

@router.get("/", response_model=List[DeliveryInfoResponse])
async def get_all_deliveries(db: Session = Depends(get_db)):
    ship_repository = ShipRepository(db)
    port_repository = PortRepository(db)


    all_ships = ship_repository.get_all_ships()

    delivery_info_list = []
    for ship in all_ships:
        port_from = port_repository.get_port_name_by_id(ship.port.id) if ship.port else "N/A"
        port_to = port_repository.get_port_name_by_id(ship.port_deliver_id) if ship.port_deliver_id else "N/A"

        delivery_info = DeliveryInfoResponse(
            delivery_id=ship.id,
            ship_title=ship.title,
            port_from=port_from,
            port_to=port_to
        )
        delivery_info_list.append(delivery_info)

    return delivery_info_list
