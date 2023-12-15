# Importing container classes and other related modules
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship

# Creating instances of different container types
basic_container = BasicContainer(1, 2000)
heavy_container = HeavyContainer(2, 4000)
refrigerated_container = RefrigeratedContainer(3, 3500)
liquid_container = LiquidContainer(4, 4000)

# Creating instances of ports
port1 = Port(1, 40.7128, 74.0060)
port2 = Port(2, 34.0522, 118.2437)

# Creating an instance of the ship with specified parameters
ship = Ship(1, 750, port1, 3000, 8, 3, 2, 1, 0.15)

# Creating a list of containers
containers = [basic_container, heavy_container, refrigerated_container, liquid_container]

# Displaying information about each container
for container in containers:
    print(f"Container ID {container.ID} - Weight: {container.weight} kg")
    print()

# Creating additional containers
container1 = BasicContainer(5, 2500)
container2 = BasicContainer(6, 2500)
container3 = HeavyContainer(7, 3500)

# Displaying information about ports
print(f"Port 1 - ID: {port1.ID}, Latitude: {port1.latitude}, Longitude: {port1.longitude}")
print(f"Port 2 - ID: {port2.ID}, Latitude: {port2.latitude}, Longitude: {port2.longitude}")

# Displaying information about the ship
print("Ship data:")
print(f"ID: {ship.ID}")
print(f"Fuel: {ship.fuel} liters")
print(f"Current port ID: {ship.currentPort.ID}")
print(f"Total weight capacity of the ship: {ship.totalWeightCapacity} kg")
print(f"Maximum number of all containers: {ship.maxNumberOfAllContainers}")
print(f"Maximum number of HeavyContainers: {ship.maxNumberOfHeavyContainers}")
print(f"Maximum number of RefrigeratedContainers: {ship.maxNumberOfRefrigeratedContainers}")
print(f"Maximum number of LiquidContainers: {ship.maxNumberOfLiquidContainers}")
print(f"Fuel consumption per kilometer: {ship.fuelConsumptionPerKM} liters per km")# Importing container classes and other related modules
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship

# Creating instances of different container types
basic_container = BasicContainer(1, 2000)
heavy_container = HeavyContainer(2, 4000)
refrigerated_container = RefrigeratedContainer(3, 3500)
liquid_container = LiquidContainer(4, 4000)

# Creating instances of ports
port1 = Port(1, 40.7128, 74.0060)
port2 = Port(2, 34.0522, 118.2437)

# Creating an instance of the ship with specified parameters
ship = Ship(1, 750, port1, 3000, 8, 3, 2, 1, 0.15)

# Creating a list of containers
containers = [basic_container, heavy_container, refrigerated_container, liquid_container]

# Displaying information about each container
for container in containers:
    print(f"Container ID {container.ID} - Weight: {container.weight} kg")
    print()

# Creating additional containers
container1 = BasicContainer(5, 2500)
container2 = BasicContainer(6, 2500)
container3 = HeavyContainer(7, 3500)

# Displaying information about ports
print(f"Port 1 - ID: {port1.ID}, Latitude: {port1.latitude}, Longitude: {port1.longitude}")
print(f"Port 2 - ID: {port2.ID}, Latitude: {port2.latitude}, Longitude: {port2.longitude}")

# Displaying information about the ship
print("Ship data:")
print(f"ID: {ship.ID}")
print(f"Fuel: {ship.fuel} liters")
print(f"Current port ID: {ship.currentPort.ID}")
print(f"Total weight capacity of the ship: {ship.totalWeightCapacity} kg")
print(f"Maximum number of all containers: {ship.maxNumberOfAllContainers}")
print(f"Maximum number of HeavyContainers: {ship.maxNumberOfHeavyContainers}")
print(f"Maximum number of RefrigeratedContainers: {ship.maxNumberOfRefrigeratedContainers}")
print(f"Maximum number of LiquidContainers: {ship.maxNumberOfLiquidContainers}")
print(f"Fuel consumption per kilometer: {ship.fuelConsumptionPerKM} liters per km")
