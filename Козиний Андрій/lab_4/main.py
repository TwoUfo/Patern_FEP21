from uuid import uuid4
from fastapi import FastAPI, HTTPException
from Models import *
from DB import *


app = FastAPI()


@app.post('/CreatePort')
def post_port(port_data: PortModel):
    """Створення порта"""
    random_id = str(uuid4())
    new_port_dict = {
        "id": random_id,
        "latitude": port_data.latitude,
        "longitude": port_data.longitude
    }

    port = TablePort(random_id, port_data.latitude, port_data.longitude)
    session.add(port)
    session.commit()
    return new_port_dict


@app.post('/CreateShip')
def post_ship(ship_data: ShipModel):
    random_id = str(uuid4())
    new_ship_dict = {
        "id": random_id,
        "fuel": ship_data.fuel,
        "current_port": ship_data.port_id,
        "total_weight_capacity": ship_data.total_weight_capacity,
        "max_all_containers": ship_data.max_all_cont,
        "max_heavy_containers": ship_data.max_heavy_cont,
        "max_refrigerated_containers": ship_data.max_refrigerated_cont,
        "max_liquid_containers": ship_data.max_liquid_cont,
        "fuel_consumption_per_km": ship_data.fuel_consumption_per_km
    }

    ship = TableShip(random_id, ship_data.fuel, ship_data.port_id, ship_data.total_weight_capacity,
                     ship_data.max_all_cont, ship_data.max_heavy_cont, ship_data.max_refrigerated_cont,
                     ship_data.max_liquid_cont, ship_data.fuel_consumption_per_km)
    session.add(ship)
    session.commit()
    return new_ship_dict


@app.post('/sail_to')
def sail_to(current_port_id: str, destination_port_id: str, ship_to_sail_id: str):
    starting_port = session.query(TablePort).filter(TablePort.id == current_port_id).first()
    ending_port = session.query(TablePort).filter(TablePort.id == destination_port_id).first()
    ship = session.query(TableShip).filter(TableShip.id == ship_to_sail_id).first()
    if ship.port_id == starting_port.id:
        ship.port_id = ending_port.id
        session.commit()
        return 'Sailing was successfull'
    else:
        raise HTTPException(status_code=404, detail="Given ship isn't in given port")
