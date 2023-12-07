from port import Port


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


port1 = Port(1, 40.7128, -74.0060)  # New York Port
ship1 = Ship(1, 1000, port1, 5000, 10, 5, 3, 2, 0.2)


