from pydantic import BaseModel


class PortModel(BaseModel):
    id: int
    latitude: float
    longitude: float


class ShipModel(BaseModel):
    id: int
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: int
    fuel: float
    port_id: int


class ContainerModel(BaseModel):
    id: int
    type: str
    weight: float
    port_id: int
