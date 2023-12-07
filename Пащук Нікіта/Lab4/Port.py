from abc import ABC, abstractmethod
from pydantic import BaseModel
from haversine import haversine


class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, s):
        pass

    def outgoing_ship(self, s):
        pass


class Port(IPort, BaseModel):
    id: str
    latitude: float
    longitude: float
    containers: list = []
    ship_history: list = []
    ship_current: list = []

    def get_distance(self, other_port: 'Port'):
        dist = haversine((self.latitude, self.longitude), (other_port.latitude, other_port.longitude))
        return round(dist, 2)

    def incoming_ship(self, s):
        current_id_found = any(obj.id == s.id for obj in self.ship_current)
        if not current_id_found:
            self.ship_current.append(s)

    def outgoing_ship(self, s):
        history_id_found = any(obj.id == s.id for obj in self.ship_history)
        current_id_found = any(obj.id == s.id for obj in self.ship_current)
        if not history_id_found:
            self.ship_history.append(s)
            if current_id_found:
                self.ship_current.remove(s)
