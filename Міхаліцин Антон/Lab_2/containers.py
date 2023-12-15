# containers.py

from abc import ABC, abstractmethod

class Container(ABC):
    def __init__(self, ID, weight):
        self.ID = ID
        self.weight = weight

    @abstractmethod
    def consumption(self):
        pass

    def equals(self, other):
        return (
            isinstance(other, Container) and
            self.ID == other.ID and
            self.weight == other.weight
        )

class BasicContainer(Container):
    def __init__(self, ID, weight):
        if weight <= 3000:
            super().__init__(ID, weight)
        else:
            raise ValueError("Weight of BasicContainer should be <= 3000.")

    def consumption(self):
        return 2.50 * self.weight

class HeavyContainer(Container):
    def __init__(self, ID, weight):
        if weight > 3000:
            super().__init__(ID, weight)
        else:
            raise ValueError("Weight of HeavyContainer should be > 3000.")

    def consumption(self):
        # Fuel consumption for HeavyContainer: 3.00 per unit of weight
        return 3.00 * self.weight

class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        # Fuel consumption for RefrigeratedContainer: 5.00 per unit of weight
        return 5.00 * self.weight

class LiquidContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        # Fuel consumption for LiquidContainer: 4.00 per unit of weight
        return 4.00 * self.weight
