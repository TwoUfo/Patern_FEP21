import math
from container import Container

class Port:
    def __init__(self, ID, latitude, longitude):
        self.ID = ID
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []

    def get_distance(self, other):
        earth_radius_km = 6371

        lat1_rad = math.radians(self.latitude)
        lon1_rad = math.radians(self.longitude)
        lat2_rad = math.radians(other.latitude)
        lon2_rad = math.radians(other.longitude)

        lat_diff = lat2_rad - lat1_rad
        lon_diff = lon2_rad - lon1_rad

        a = math.sin(lat_diff / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(lon_diff / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_km = earth_radius_km * c

        return distance_km

    def add_container(self, container):
        self.containers.append(container)
