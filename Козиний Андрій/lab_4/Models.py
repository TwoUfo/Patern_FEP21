from pydantic import BaseModel


class PortModel(BaseModel):
    latitude: float
    longitude: float


class ShipModel(BaseModel):
    fuel: int
    port_id: str
    total_weight_capacity: int
    max_all_cont: int
    max_heavy_cont: int
    max_refrigerated_cont: int
    max_liquid_cont: int
    fuel_consumption_per_km: float
