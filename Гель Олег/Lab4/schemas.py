from pydantic import BaseModel

class PortCreate(BaseModel):
    name: str
    location: str

class ShipCreate(BaseModel):
    name: str
    port_id: int

class ContainerCreate(BaseModel):
    name: str
    ship_id: int
