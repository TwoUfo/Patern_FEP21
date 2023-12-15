# Importing necessary modules and classes
from typing import List
from containers import Container
from port import Port

# Defining the Ship class
class Ship:
    def __init__(self, ID, fuel, currentPort, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers,
                 maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, fuelConsumptionPerKM):
        self.ID = ID
        self.fuel = fuel
        self.currentPort = currentPort
        self.totalWeightCapacity = totalWeightCapacity
        self.maxNumberOfAllContainers = maxNumberOfAllContainers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.fuelConsumptionPerKM = fuelConsumptionPerKM

    # Method to get the current containers on the ship
    def getCurrentContainers(self) -> List[Container]:
        return []  # Replace with actual implementation

# Creating an instance of a port (New York Port)
port1 = Port(1, 40.7128, -74.0060)
# Creating an instance of a ship with specified parameters
ship1 = Ship(1, 1000, port1, 5000, 10, 5, 3, 2, 0.2)

# Obtaining and displaying the current containers on the ship
current_containers = ship1.getCurrentContainers()
for container in current_containers:
    print(f"Container {container.ID}: Type - {container.type}")
