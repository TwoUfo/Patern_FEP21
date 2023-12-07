from abc import ABC, abstractmethod
from pydantic import BaseModel


class Container(BaseModel, ABC):
    id: str
    weight: int
    type: str
    items: list = []
    max_items: int = 3

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
    def check_category(id, weight, type):
        if type == "Basic":
            return BasicContainer(id=id, weight=weight, type=type)
        elif type == "Heavy":
            return HeavyContainer(id=id, weight=weight, type=type)
        elif type == "Refrigerated":
            return RefrigeratedContainer(id=id, weight=weight, type=type)
        elif type == "Liquid":
            return LiquidContainer(id=id, weight=weight, type=type)


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


def get_type(container):
    if isinstance(container, BasicContainer):
        return container.id
    elif isinstance(container, HeavyContainer):
        return container.id
    elif isinstance(container, RefrigeratedContainer):
        return container.id
    elif isinstance(container, LiquidContainer):
        return container.id
