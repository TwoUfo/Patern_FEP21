from abc import ABC, abstractmethod
from dataclasses import dataclass
from haversine import haversine


class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, s):
        pass

    def outgoing_ship(self, s):
        pass


@dataclass
class ContainerDetails:
    basic_cont: int
    heavy_cont: int
    refrigerated_cont: int
    liquid_cont: int


class Port(IPort):
    def __init__(self, id, latitude: float, longitude: float, data_cont: ContainerDetails):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.data_cont = data_cont
        self.containers = []
        self.ship_history = []
        self.ship_current = []

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
