# Importing the math module
import math

# Defining the Port class
class Port:
    def __init__(self, ID, latitude, longitude):
        self.ID = ID
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []  # List to store containers at the port
        self.history = []     # List to store historical data
        self.current = []     # List to store current data

    # Method to calculate the distance between two ports
    def getDistance(self, other):
        earth_radius = 6371

        # Converting latitude and longitude to radians
        latitude1_rad = math.radians(self.latitude)
        longitude1_rad = math.radians(self.longitude)
        latitude2_rad = math.radians(other.latitude)
        longitude2_rad = math.radians(other.longitude)

        # Calculating differences in latitude and longitude
        latitude_diff = latitude2_rad - latitude1_rad
        longitude_diff = longitude2_rad - longitude1_rad

        # Haversine formula to calculate distance
        a = math.sin(latitude_diff / 2)**2 + math.cos(latitude1_rad) * math.cos(latitude2_rad) * math.sin(longitude_diff / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_km = earth_radius * c

        return distance_km

# Creating instances of ports
port1 = Port(1, 40.7128, 74.0060)
port2 = Port(2, 34.0522, 118.2437)

# Calculating and displaying the distance between ports
distance = port1.getDistance(port2)
print(f"Distance between Port 1 and Port 2 is {distance:.2f} kilometers.\n")
