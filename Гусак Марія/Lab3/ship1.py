from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conteiners1 import *
    from port1 import *

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ConfigShip:
    totalWeightCapacity: int
    maxNumberOfAllContainers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float

class IShip(ABC):

    @abstractmethod
    def sailTo(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amountOfFuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass

class ShipClass(IShip, ABC):

    def __init__(self, id, Port: PortClass, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0):
        self.id = id
        self.fuel = fuel
        self.port = Port
        self.configs = shipConfig
        self._containersOnShip = Containers
        self._containersOnShipID = []
        self.usedContainers = []
        self.unloadedContainersID = []
        self._usedPortsID = []

    @property
    def containersOnShip(self):
        return self._containersOnShip

    @property
    def containersOnShipID(self):
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
        return self._usedPortsID

    def getExtraFuelConsumptionFromContainer(self) -> float:
        extraFuel = 0
        for shipContainer in self.containersOnShip:
            if type(shipContainer) != str:
                extraFuel += shipContainer.consumption()
            elif type(shipContainer) == str:
                continue
        return extraFuel


class LightWeightShip(ShipClass):

    def __init__(self, id, Port: PortClass, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0):
        super().__init__(id, Port, shipConfig, Containers, fuel)

    def sailTo(self, port: PortClass) -> bool:
        for currentPort in self.port:
            if (int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.usedPortsID:
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"LightWeightShip {self.id} has been sent to port {port.id} successfully.")
                return True
            elif currentPort.id in self.usedPortsID:
                continue
            else:
                self.refuel(int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"LightWeightShip {self.id} has been refueled and sent to port {port.id} successfully.")
                return True

    def refuel(self, amountOfFuelToAdd: float) -> None:
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        print(f"{amountOfFuelToAdd} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amountOfFuelToAdd

    def checkCompatibilityOfShipAndContainer(self, i: int) -> bool:
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return True
        else:
            return False

    def deleteContainerOnShip(self, containerID) -> None:
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers

    def load(self, containerID: uuid4) -> None:
        print("Loading container...")
        currentContainersOnShip = self.containersOnShip
        for i in range(len(currentContainersOnShip)):
            for currentPort in self.port:
                if type(currentContainersOnShip[i]) == str:
                    break
                elif containerID == currentContainersOnShip[i].id and self.checkCompatibilityOfShipAndContainer(i):
                    currentContainersOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been succesfully loaded on LightWeightShip.")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers) - 1) and containerID == self.usedContainers[i - 1]:
                        break

    def unload(self, containerID):
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self.containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been succesfully unloaded from LightWeightShip.")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} not found.")


class MediumShip(ShipClass):

    def __init__(self, id, Port: PortClass, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0):
        super().__init__(id, Port, shipConfig, Containers, fuel)
        # Additional attributes or methods specific to MediumShip

    def sailTo(self, port: PortClass) -> bool:
        for currentPort in self.port:
            if (int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.usedPortsID:
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"MediumShip {self.id} has been sent to port {port.id} successfully.")
                return True
            elif currentPort.id in self.usedPortsID:
                continue
            else:
                self.refuel(int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"MediumShip {self.id} has been refueled and sent to port {port.id} successfully.")
                return True

    def refuel(self, amountOfFuelToAdd: float) -> None:
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        print(f"{amountOfFuelToAdd} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amountOfFuelToAdd

    def checkCompatibilityOfShipAndContainer(self, i: int) -> bool:
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return True
        else:
            return False

    def deleteContainerOnShip(self, containerID) -> None:
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers

    def load(self, containerID: uuid4) -> None:
        print("Loading container...")
        currentContainersOnShip = self.containersOnShip
        for i in range(len(currentContainersOnShip)):
            for currentPort in self.port:
                if type(currentContainersOnShip[i]) == str:
                    break
                elif containerID == currentContainersOnShip[i].id and self.checkCompatibilityOfShipAndContainer(i):
                    currentContainersOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been succesfully loaded on MediumShip.")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers) - 1) and containerID == self.usedContainers[i - 1]:
                        break

    def unload(self, containerID):
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self.containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been successfully unloaded from MediumShip.")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} not found.")

class HeavyShip(ShipClass):

    def __init__(self, id, Port: PortClass, shipConfig: ConfigShip, Containers: Container, fuel: float = 0.0):
        super().__init__(id, Port, shipConfig, Containers, fuel)
        # Additional attributes or methods specific to HeavyShip

    def sailTo(self, port: PortClass) -> bool:
        for currentPort in self.port:
            if (int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer()) < self.fuel and currentPort.id not in self.usedPortsID:
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"HeavyShip {self.id} has been sent to port {port.id} successfully.")
                return True
            elif currentPort.id in self.usedPortsID:
                continue
            else:
                self.refuel(int(port.getDistance(
                    currentPort)) / self.configs.fuelConsumptionPerKM + self.getExtraFuelConsumptionFromContainer() - self.fuel)
                currentPort.incomingShip(self)
                self.usedPortsID.append(currentPort.id)
                print(f"HeavyShip {self.id} has been refueled and sent to port {port.id} successfully.")
                return True

    def refuel(self, amountOfFuelToAdd: float) -> None:
        if amountOfFuelToAdd < 0:
            raise ValueError(f"Amount of fuel given is less that 0.")
        print(f"{amountOfFuelToAdd} liters has been added to previous amount of fuel: {self.fuel}.")
        self.fuel += amountOfFuelToAdd

    def checkCompatibilityOfShipAndContainer(self, i: int) -> bool:
        if self.containersOnShip[i].weight <= self.configs.totalWeightCapacity:
            return True
        else:
            return False

    def deleteContainerOnShip(self, containerID) -> None:
        containers = [container for container in self.containersOnShip if container.id != containerID]
        self.containersOnShip = containers

    def load(self, containerID: uuid4) -> None:
        print("Loading container...")
        currentContainersOnShip = self.containersOnShip
        for i in range(len(currentContainersOnShip)):
            for currentPort in self.port:
                if type(currentContainersOnShip[i]) == str:
                    break
                elif containerID == currentContainersOnShip[i].id and self.checkCompatibilityOfShipAndContainer(i):
                    currentContainersOnShip.append(containerID)
                    currentPort.deleteContainer(containerID)
                    print(f"Container {containerID} has been successfully loaded on HeavyShip.")
                    self.usedContainers.append(containerID)
                    if i > (len(self.usedContainers) - 1) and containerID == self.usedContainers[i - 1]:
                        break

    def unload(self, containerID):
        for shipContainer in self.containersOnShip:
            for currentPort in self.port:
                if type(shipContainer) == str:
                    break
                elif containerID in self.containersOnShipID and containerID not in self.unloadedContainersID:
                    self.containersOnShip.remove(shipContainer)
                    currentPort.currentContainersInPort.append(shipContainer)
                    self.unloadedContainersID.append(containerID)
                    print(f"Container {containerID} has been successfully unloaded from HeavyShip.")
                elif containerID in self.unloadedContainersID:
                    continue
                else:
                    return ValueError(f"Container with ID {containerID} not found.")
