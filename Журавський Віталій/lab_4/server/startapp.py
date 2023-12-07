from fastapi import FastAPI
from mainapi.server.basemodels import *
from mainapi.models.inputdata import Input
from mainapi.server.logic.createobj import CreateObj
from mainapi.models.updatedata import Update
from typing import List

app = FastAPI()


@app.post('/')
def create(port: PortModel, ship: ShipModel, containers: List[ContainerModel]):
    if ship.id != 0:
        Input.ship(ship.id, ship.totalWeightCapacity, ship.maxNumberOfAllContainers, ship.maxNumberOfHeavyContainers, ship.maxNumberOfRefrigeratedContainers, ship.maxNumberOfLiquidContainers, ship.fuelConsumptionPerKM, ship.fuel, ship.port_id)

    if port.id != 0:
        Input.port(port.id, port.latitude, port.longitude)

    for container in containers:
        if container.id != 0:
            Input.container(container.id, container.type, container.weight, container.port_id)


@app.post('/Delivery')
def delivery(ship_id: int, port_id_1: int, port_id_2: int):
    port_1 = CreateObj.port(port_id_1)
    port_2 = CreateObj.port(port_id_2)

    if ship_id in port_1.current_ships:
        ship = CreateObj.ship(ship_id, port_1)
        ship.sail_to(port_2)

        Update.ship(ship)

        return {'ship_id': ship.id, 'fuel': ship.fuel, 'curr_port': ship.port.id}

    else:
        return {'Error': 'No ship found in this port'}


