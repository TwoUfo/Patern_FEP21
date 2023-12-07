from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Containers import *
    from Port import *


@dataclass
class ConfigShip:
    """Dataclass containing Configuration of a Ship"""
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float


class IShip(ABC):
    """Interface of a Ship with abstract methods."""

    @abstractmethod
    def sailTo(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass


class ShipСlass(IShip):
    """Ship implementation"""

    # ------------------------------ Initialization ------------------------------
    def __init__(self, id, Port: PortClass, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0) -> None:
        self.id = id
        self.fuel = fuel
        self.port = Port
        self.configs = shipConfig
        self._containersOnShip = Containers
        self._containersOnShipID = []
        self.usedContainers = []
        self.unloadedContainersID = []
        self._usedPortsID = []

    def __str__(self) -> str:
        return f"id: {self.id}\nfuel: {self.fuel}\nport: {self.port}\nconfigs:\n\t{self.configs}\ncontainers: {self.containersOnShip}"

    # -------------------------------- Properties --------------------------------
    @property
    def containersOnShip(self):
        """Returns containers on ship."""
        return self._containersOnShip

    @property
    def containersOnShipID(self):
        """Return IDs of containers on ship."""
        shipContainersID = []
        for shipContainer in self.containersOnShip:
            if type(shipContainer) == str:
                shipContainersID.append(shipContainer)
                continue
            else:
                shipContainersID.append(shipContainer.id)
        self._containersOnShipID = shipContainersID
        return self._containersOnShipID

    @property
    def usedPortsID(self):
        """Returns IDs of Used Ports"""
        return self._usedPortsID

    # ---------------------------------- Methods ----------------------------------
    def getExtraFuelConsumptionFromContainer(self) -> float:
        """Return an extra amount of fuel needed depending on weight of Container.
    """
        extraFuel = 0
        # Traversing through each container on ship
        for shipContainer in self.containersOnShip:
            # If current container on ship is an object of class, and not string, then, execute code.
            if type(shipContainer) != str:
                extraFuel += shipContainer.consumption()
            # Else continue cycle
            else:
                continue
        return extraFuel

    def sailTo(self, port: PortClass) -> bool:
        """Travel from current port to anotherm. Parameter port means port you want to get to from current port.
    """
        for currentPort in self.port:
            # Check is enough fuel to travel to port
            if (int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.usedPortsID:
                # If there is enough fuel, travel to port.
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"Ship {self.id} has been sent to port {port.id} successfully.")
                return True
            elif currentPort.id in self.usedPortsID:
                continue
            else:
                # Else, refuel ship
                self.refuel(int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                # Travel to port given
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"Ship {self.id} has been refueld and sent to port {port.id} successfully.")
                return True

    def refuel(self, amountOfFuelToAdd: float = 0) -> None:
        """Adds needed amount of fuel. If amount of fuel has not been passed, does nothing.
    """
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        print(f"{amountOfFuelToAdd} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amountOfFuelToAdd

    def checkCompatibilityOfShipAndContainer(self, i: int) -> bool:
        """Check if ship can accept container.
    """
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return True
        else:
            return False

    def deleteContainerOnShip(self, containerID: str) -> None:
        """Delete container from list of containers on ship if it matches passed ID in it.
    """
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers

    def load(self, containerID: str) -> None:
        """Load passed container onto a ship.
    """
        currentContainersOnShip = self.containersOnShip
        for i in range(len(currentContainersOnShip)):
            for currentPort in self.port:
                if type(currentContainersOnShip[i]) == str:
                    break
                elif containerID == currentContainersOnShip[i].id and self.checkCompatibilityOfShipAndContainer(i):
                    currentContainersOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been succesfully loaded.")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers) - 1) and containerID == self.usedContainers[i - 1]:
                        break

    def unload(self, containerID: str) -> None:
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self.containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been succesfully unloaded.")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} not found.")
