from sqlalchemy import func
from fastapi import FastAPI, HTTPException
from typing import List
from random import choice
from uuid import uuid4
from Create_db import TablePort, TableShip, TableContainer, TableItem, session, engine
from Port import Port
from Ship import Ship, DataShip
from Container import Container
from Item import IItem
from Create_and_delivery_classes import CreatePort, CreateContainer, CreateShip, CreateItem, DeliveryInput

app = FastAPI()


connection = engine.connect()


def assign_port_id():
    port_ids_in_ports = [row[0] for row in session.query(TablePort.id).all()]
    current_port_id = choice(port_ids_in_ports)
    return current_port_id


def assign_cont_id(item_type):
    specific_type_conts = session.query(TableContainer).filter(TableContainer.type == item_type).all()
    for cont in specific_type_conts:
        count = session.query(func.count()).filter(TableItem.container_id == cont.id).scalar()
        if count < 3:
            return cont.id


@app.post("/createPort", status_code=200)
def create_port(port: CreatePort):
    """Створення порта"""
    random_id = str(uuid4())
    new_port_dict = {
        "id": random_id,
        "latitude": port.latitude,
        "longitude": port.longitude
    }
    port = TablePort(random_id, port.latitude, port.longitude)
    session.add(port)
    session.commit()
    return new_port_dict


@app.post("/createShip", status_code=200)
def create_ship(ships: List[CreateShip]):
    """Створення корабля"""
    ships_to_db = []
    for ship in ships:
        random_id = str(uuid4())
        current_port_id = assign_port_id()
        new_ship_dict = {
            "id": random_id,
            "fuel": ship.fuel,
            "current_port": current_port_id,
            "total_weight_capacity": ship.total_weight_capacity,
            "max_all_containers": ship.maxNumberOfAllContainers,
            "max_basic_containers": ship.maxNumberOfBasicContainers,
            "max_heavy_containers": ship.maxNumberOfHeavyContainers,
            "max_refrigerated_containers": ship.maxNumberOfRefrigeratedContainers,
            "max_liquid_containers": ship.maxNumberOfLiquidContainers,
            "fuel_consumption_per_km": ship.fuelConsumptionPerKM
        }
        ships_to_db.append(new_ship_dict)
        ship_to_db = TableShip(random_id, current_port_id, ship.fuel, ship.total_weight_capacity,
                               ship.maxNumberOfAllContainers,
                               ship.maxNumberOfBasicContainers, ship.maxNumberOfHeavyContainers,
                               ship.maxNumberOfRefrigeratedContainers, ship.maxNumberOfLiquidContainers,
                               ship.fuelConsumptionPerKM, ship.assign_type())
        session.add(ship_to_db)
    session.commit()
    return ships_to_db


@app.post('/createContainers', status_code=200)
def create_containers(containers: List[CreateContainer]):
    """Створення контейнерів"""
    new_containers = []
    for cont in containers:
        random_cont_id = str(uuid4())
        port_id = assign_port_id()
        new_cont_dict = {
            "id": random_cont_id,
            "port_id": port_id,
            "weight": cont.weight,
            "type": cont.type
        }
        new_containers.append(new_cont_dict)
        cont_obj = TableContainer(random_cont_id, port_id, cont.weight, cont.type)
        session.add(cont_obj)

    session.commit()
    return new_containers


@app.post('/CreateItemsPack', status_code=200)
def create_items_pack(items: List[CreateItem]):
    """Створення паків з айтемами"""
    new_items = []
    for item in items:
        try:
            random_item_id = str(uuid4())
            cont_id = assign_cont_id(item.type)
            if cont_id is None:
                raise HTTPException(status_code=404, detail="There aren't any free containers for this pack of items")
            new_cont_dict = {
                "id": random_item_id,
                "container_id": cont_id,
                "weight": item.weight,
                "count": item.count,
                "type": item.type
            }
            new_items.append(new_cont_dict)
            cont_obj = TableItem(random_item_id, cont_id, item.weight, item.count, item.type)
            session.add(cont_obj)
        except HTTPException:
            continue

    session.commit()
    return new_items


@app.post('/Delivery', status_code=200)
def delivery(ids_data: DeliveryInput):
    """Доставлення контейнерів з одного порту в інший"""

    """Порти"""

    starting_port = session.query(TablePort).filter(TablePort.id == ids_data.starting_port_id).first()
    transitional_port = session.query(TablePort).filter(TablePort.id == ids_data.transitional_port_id).first()
    ending_port = session.query(TablePort).filter(TablePort.id == ids_data.ending_port_id).first()
    all_ports = [starting_port, ending_port, transitional_port]

    """Корабель"""

    ship_to_sail = session.query(TableShip).filter(TableShip.id == ids_data.ship_to_sail_id).first()

    """Контейнери"""

    conts_in_start_port = [row for row in
                           session.query(TableContainer).filter(TableContainer.port_id == starting_port.id).all()]
    conts_in_end_port = [row for row in
                         session.query(TableContainer).filter(TableContainer.port_id == ending_port.id).all()]
    """Паки айтемів"""

    conts_in_port_id = [row for row in
                        session.query(TableContainer.id).filter(TableContainer.port_id == starting_port.id).all()]
    all_items = session.query(TableItem).all()
    item_packs = [row for row in all_items if row.container_id in conts_in_port_id]
    """Створення необхідних об'єктів"""

    """Порти"""

    for i, port in enumerate(all_ports):
        port_obj = Port(id=port.id, latitude=port.latitude, longitude=port.longitude)
        all_ports[i] = port_obj
    """Корабель"""

    if ship_to_sail.port_id == starting_port.id:
        ship_obj = Ship.check_type(id=ship_to_sail.id, fuel=ship_to_sail.fuel, current_port=all_ports[0],
                                   ships_data=DataShip(
                                       ship_to_sail.total_weight_capacity, ship_to_sail.max_all_cont,
                                       ship_to_sail.max_basic_cont,
                                       ship_to_sail.max_heavy_cont, ship_to_sail.max_refrigerated_cont,
                                       ship_to_sail.max_liquid_cont,
                                       ship_to_sail.fuel_consumption_per_km))
        all_ports[0].ship_current.append(ship_obj)
    else:
        raise HTTPException(status_code=404, detail="Given ship isn't in given port")

    """Контейнери"""

    all_conts = []
    all_conts_for_result = []
    for cont in conts_in_start_port:
        cont_obj = Container.check_category(id=cont.id, weight=cont.weight, type=cont.type)
        all_conts.append(cont_obj)
        all_ports[0].containers.append(cont_obj)
    for cont in conts_in_end_port:
        cont_obj = Container.check_category(id=cont.id, weight=cont.weight, type=cont.type)
        all_ports[1].containers.append(cont_obj)
        all_conts_for_result.append(all_ports[1].containers)

    """Паки айтемів"""

    all_packs_of_items = []
    for pack in item_packs:
        pack_obj = IItem.check_type(id=pack.id, weight=pack.weight, count=pack.count, item_type=pack.type,
                                    container_id=pack.container_id)
        all_packs_of_items.append(pack_obj)

    for pack in all_packs_of_items:
        for cont in all_conts:
            if cont.id == pack.container_id:
                cont.items.append(pack)
                cont.weight += pack.getTotalWeight()

    """Основна логіка"""

    """Завантаження контейнерів з айтемами на корабель"""

    temp_copy = list(ship_obj.current_port.containers)
    for cont in temp_copy:
        ship_obj.load(cont)

    """Рух корабля до потрібного порта"""
    ship_obj.sail_to(all_ports[0], all_ports[1], all_ports[2])
    row_to_update = session.query(TableShip).filter(TableShip.port_id == starting_port.id).first()
    row_to_update.port_id = ending_port.id
    session.commit()

    """Розвантаження контейнерів з айтемами в новий порт"""
    for _ in ship_obj.containers:
        row_to_update = session.query(TableContainer).filter(TableContainer.port_id == starting_port.id).first()
        row_to_update.port_id = ending_port.id
        session.commit()
        session.close()

    while ship_obj.containers:
        ship_obj.unload(ship_obj.containers[0])
    return (f"Кількість контейнерів у новому порті перед доставленням: {len(all_conts_for_result)}. "
            f"Кількість контейнерів у новому порті після доставлення: {len(all_ports[1].containers)}. Доставлення "
            f"пройшла успішно!")


@app.get("/getPortState", status_code=200)
def get_port_state(obj_id: str):
    """Дістати дані про порт та об'єкти (і їх дані) в ньому"""
    query = session.query(TablePort).filter(TablePort.id == obj_id)
    result = {column.name: getattr(query.first(), column.name) for column in TablePort.__table__.columns}
    ship_info = session.query(TableShip).filter(TableShip.port_id == obj_id).all()
    container_info = session.query(TableContainer).filter(TableContainer.port_id == obj_id).all()
    c_in_port_id = [row[0] for row in session.query(TableContainer.id).filter(TableContainer.port_id == obj_id).all()]
    all_items = session.query(TableItem).all()
    item_packs = [row for row in all_items if row.container_id in c_in_port_id]
    ships_data = []
    conts_data = []
    for ship in ship_info:
        ship_dict = {
            "id": ship.id,
            "port_id": ship.port_id,
            "fuel": ship.fuel,
            "total_weight_capacity": ship.total_weight_capacity,
            "max_all_containers": ship.max_all_cont,
            "max_basic_containers": ship.max_basic_cont,
            "max_heavy_containers": ship.max_heavy_cont,
            "max_refrigerated_containers": ship.max_refrigerated_cont,
            "max_liquid_containers": ship.max_liquid_cont,
            "fuel_consumption_per_km": ship.fuel_consumption_per_km,
            "type": ship.type
        }
        ships_data.append(ship_dict)
    for cont in container_info:
        items_data = []
        for pack in item_packs:
            if cont.id == pack.container_id:
                pack_dict = {
                    "id": pack.id,
                    "container_id": pack.container_id,
                    "weight": pack.weight,
                    "count": pack.count,
                    "type": pack.type
                }
                items_data.append(pack_dict)
        cont_dict = {
            "id": cont.id,
            "port_id": cont.port_id,
            "weight": cont.weight,
            "type": cont.type,
            "items": items_data
        }
        conts_data.append(cont_dict)
    result["Ships"] = ships_data
    result["Containers"] = conts_data
    return result

