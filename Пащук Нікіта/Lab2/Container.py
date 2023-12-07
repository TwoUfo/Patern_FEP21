from abc import ABC, abstractmethod


class Container(ABC):
    def __init__(self, id, weight: int, type: str):
        self.id = id
        self.weight = weight
        self.type = type

    @abstractmethod
    def consumption(self):
        pass

    def __eq__(self, other_container: 'Container'):
        check_id = self.id == other_container.id
        check_weight = self.weight == other_container.weight
        check_type = isinstance(type(self), type(other_container))
        if check_id and check_weight and check_type:
            return True
        else:
            return False

    @staticmethod
    def check_category(id, weight, value=None):
        if weight <= 3000:
            return BasicContainer(id, weight, type="Basic")
        elif weight > 3000 and value is None:
            return HeavyContainer(id, weight, type="Heavy")
        elif value == "R":
            return RefrigeratedContainer(id, weight, type="Refrigerated")
        elif value == "L":
            return LiquidContainer(id, weight, type="Liquid")


class BasicContainer(Container):
    def consumption(self):
        consumption = 2.50 * self.weight
        return consumption


class HeavyContainer(Container):
    def consumption(self):
        consumption = 3.00 * self.weight
        return consumption


class RefrigeratedContainer(HeavyContainer):
    def consumption(self):
        consumption = 5.00 * self.weight
        return consumption


class LiquidContainer(HeavyContainer):
    def consumption(self):
        consumption = 4.00 * self.weight
        return consumption

