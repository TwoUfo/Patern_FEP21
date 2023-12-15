from uuid import uuid4
from fastapi import FastAPI, HTTPException
from Model import *
from DataBase import *

app = FastAPI()

@app.post('/create_port')
def post_port(port_data: PortModel):
    """Create a new port"""
    random_id = str(uuid4())
    new_port_dict = {
        "id": random_id,
        "latitude": port_data.latitude,
        "longitude": port_data.longitude
    }

    # Creating a new port in the database
    port = TablePort(random_id, port_data.latitude, port_data.longitude)
    session.add(port)
    session.commit()
    return new_port_dict

@app.post('/create_ship')
def post_ship(ship_data: ShipModel):
    random_id = str(uuid4())
    new_ship_dict = {
        "id": random_id,
        "fuel": ship_data.fuel,
        "current_port": ship_data.port_id,
        "total_weight_capacity": ship_data.total_weight_capacity,
        "max_all_containers": ship_data.max_all_containers,
        "max_heavy_containers": ship_data.max_heavy_containers,
        "max_refrigerated_containers": ship_data.max_refrigerated_containers,
        "max_liquid_containers": ship_data.max_liquid_containers,
        "fuel_consumption_per_km": ship_data.fuel_consumption_per_km
    }

    # Creating a new ship in the database
    ship = TableShip(random_id, ship_data.fuel, ship_data.port_id, ship_data.total_weight_capacity,
                     ship_data.max_all_containers, ship_data.max_heavy_containers, ship_data.max_refrigerated_containers,
                     ship_data.max_liquid_containers, ship_data.fuel_consumption_per_km)
    session.add(ship)
    session.commit()
    return new_ship_dict

@app.post('/sail_to')
def sail_to(current_port_id: str, destination_port_id: str, ship_to_sail_id: str):
    # Querying the current, starting, and ending ports from the database
    starting_port = session.query(TablePort).filter(TablePort.id == current_port_id).first()
    ending_port = session.query(TablePort).filter(TablePort.id == destination_port_id).first()
    ship = session.query(TableShip).filter(TableShip.id == ship_to_sail_id).first()
    
    # Checking if the ship is in the starting port
    if ship.port_id == starting_port.id:
        # Changing the current port of the ship in the database
        ship.port_id = ending_port.id
        session.commit()
        return 'Sailing was successful'
    else:
        raise HTTPException(status_code=404, detail="Given ship isn't in the given port")
    
