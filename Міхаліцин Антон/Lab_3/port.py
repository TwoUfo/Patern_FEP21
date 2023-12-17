"""Holds details about port objects"""

# Import necessary modules
from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Ship

# Import haversine library for distance calculations
import haversine as hs

# Define an abstract base class for ports
class IPort(ABC):

    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass

# Implement the Port class that inherits from the abstract base class IPort
class Port(IPort):
    """Implements port logic"""

    def __init__(self, port_id, latitude: float, longitude: float) -> None:
        # Initialize port with a unique ID, latitude, and longitude
        self.id = port_id
        self.latitude = latitude
        self.longitude = longitude

        # Different lists to categorize ships based on their cargo type
        self.basic = []
        self.heavy = []
        self.liquid = []
        self.refrigerated = []

        # Lists to keep track of the ship history and current ships at the port
        self.ship_history = []
        self.current_ships = []

    def __repr__(self):
        # String representation of the Port object
        return f"Port with ID {self.id}"

    def get_distance(self, port) -> float:
        # Calculate and return the haversine distance between two ports
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        print(f"dist = {dist}")
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        # Add a ship to the current_ships list if it's a valid Ship object and not already present
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True
        else:
            return False

    def outgoing_ship(self, ship: Ship) -> bool:
        # Remove a ship from the current_ships list, add it to ship_history if valid
        # TODO: Add checker (comment indicates a potential future enhancement)
        if isinstance(ship, Ship) and ship in self.current_ships:
            self.current_ships.remove(ship)
            self.ship_history.append(ship)
            return True
        else:
            return False
