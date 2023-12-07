
from pydantic import BaseModel

class DeliveryRequest(BaseModel):
    ship_id: int
    max_containers: int

class DeliveryResponse(BaseModel):
    message: str
    containers_delivered: int

class DeliveryInfoResponse(BaseModel):
    delivery_id: int
    ship_title: str
    port_from: str
    port_to: str
