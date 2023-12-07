from fastapi import APIRouter, Depends
from fastapi import HTTPException
from starlette import status
from app.schemas.port import Port
from app.schemas.ship import *
from app.schemas.items import *
from app.schemas.containers import *
from app.db.database import get_db
from app.db.repositories.ports import PortRepository
from app.db.repositories.ships import ShipRepository
from app.db.repositories.containers import ContainerRepository
from app.db.repositories.items import ItemsRepository

import json
import random

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


@router.get("/", response_model=list[Port], status_code=status.HTTP_200_OK)
def initdb(db: Session = Depends(get_db)):
    port_crud = PortRepository(db_session=db)
    ship_crud = ShipRepository(db_session=db)
    container_crud = ContainerRepository(db_session=db)
    items_crud = ItemsRepository(db_session=db)
    with open("input.json") as input_file:
        data = json.load(input_file)



    i = 0
    cont_id = 1
    items_id = 1
    for port_data in data["ports"]:
        port_id = port_data["port_id"]
        title = port_data["title"]
        basic = port_data["basic"]
        heavy = port_data["heavy"]
        refrigerated = port_data["refrigerated"]
        liquid = port_data["liquid"]
        containers = port_data["containers"]
        basic_items = port_data["basic_items"]
        heavy_items = port_data["heavy_items"]
        refrigerated_items = port_data["refrigerated_items"]
        liquid_items = port_data["liquid_items"]
        latitude = random.uniform(30.0, 32.0)
        longitude = random.uniform(20.0, 22.0)

        port = Port(id=port_id,title=title, basic=basic, heavy=heavy,
                    refrigerated=refrigerated, liquid=liquid,basic_items=basic_items,heavy_items=heavy_items,refrigerated_items=refrigerated_items,liquid_items=liquid_items, latitude=latitude,
                    longitude=longitude)

        db_port = port_crud.get_by_id(port_id=port.id)
        if db_port:
            print(f"Port already exists")
        else:
            db_port = port_crud.create_port(port=port)



        ships = port_data["ships"]
        for j in range(0, len(ships)):
            ship_data = ships[j]
            ship_id = ship_data["ship_id"]
            port_deliver_id = ship_data["port_deliver_id"]
            fuel = ship_data["fuel"]
            port = ship_data["port_id"]
            totalWeightCapacity = ship_data["totalWeightCapacity"]
            maxNumberOfAllContainers = ship_data["maxNumberOfAllContainers"]
            maxNumberOfHeavyContainers = ship_data["maxNumberOfHeavyContainers"]
            maxNumberOfRefrigeratedContainers = ship_data["maxNumberOfRefrigeratedContainers"]
            maxNumberOfLiquidContainers = ship_data["maxNumberOfLiquidContainers"]
            maxNumberOfBasicContainers = ship_data["maxNumberOfBasicContainers"]
            fuelConsumptionPerKM = ship_data["fuelConsumptionPerKM"]
            ship_type = ship_data["ship_type"]
            ship_title = ship_data["title"]



            ship = IShip(type_=ship_type, id=ship_id, port_id=port, title=ship_title, fuel=fuel,
                         port_deliver_id=port_deliver_id,
                         total_weight_capacity=totalWeightCapacity,
                         max_number_of_all_containers=maxNumberOfAllContainers,
                         max_number_of_basic_containers=maxNumberOfBasicContainers,
                         max_number_of_heavy_containers=maxNumberOfHeavyContainers,
                         max_number_of_refrigerated_containers=maxNumberOfRefrigeratedContainers,
                         max_number_of_liquid_containers=maxNumberOfLiquidContainers,
                         fuel_consumption_per_km=fuelConsumptionPerKM)

            db_ship = ship_crud.get_by_id(ship.id)
            if db_ship:
                print(f"Ship already exist")
            else:
                 db_ship = ship_crud.create_ship(ship=ship)





        for count in range(0, basic):
            container = BasicContainer(id=cont_id, weight=random.uniform(5.0, 15.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                cont_id += 1


        for count in range(0, heavy):
            container = HeavyContainer(id=cont_id, weight=random.uniform(10.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                cont_id += 1

        for count in range(0, refrigerated):
            container = RefrigeratedContainer(id=cont_id, weight=random.uniform(15.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                cont_id += 1




        for count in range(0, liquid):
            container = LiquidContainer(id=cont_id, weight=random.uniform(15.0, 20.0), port_id=port_id, ship_id=-1)
            db_container = container_crud.get_by_id(container.id)
            if db_container:
                print(f"Container already exist")
            else:
                db_container = container_crud.create_container(container=container)
                cont_id += 1



        for count in range(basic_items):
            basic_item = BasicItem(id=items_id, weight=random.uniform(5.0, 15.0), port_id=port_id,type="basic_item")
            items_crud.create_item(item=basic_item)
            items_id += 1




        for count in range(heavy_items):
            heavy_item = HeavyItem(id=items_id, weight=random.uniform(10.0, 20.0), port_id=port_id,type="heavy_item")
            items_crud.create_item(item=heavy_item)
            items_id += 1


        for count in range(refrigerated_items):
            refrigerated_item = RefrigeratedItem(id=items_id, weight=random.uniform(15.0, 20.0), port_id=port_id,type="refrigerated_item")
            items_crud.create_item(item=refrigerated_item)
            items_id += 1


        for count in range(liquid_items):
            liquid_item = LiquidItem(id=items_id, weight=random.uniform(15.0, 20.0), port_id=port_id,type="liquid_item")
            items_crud.create_item(item=liquid_item)
            items_id += 1

        i = i + 1

    print(f"port list = {port_crud.get_all_ports()}")
    return port_crud.get_all_ports()
