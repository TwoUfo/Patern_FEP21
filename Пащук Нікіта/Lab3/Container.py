from abc import ABC, abstractmethod


class Container(ABC):
    def __init__(self, id, weight: int, type: str):
        self.id = id
        self.weight = weight
        self.type = type
        self.items = []
        self.max_items = 2

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
    def check_category(id, weight, type=None):
        if weight <= 3000:
            return BasicContainer(id, weight, "Basic")
        elif weight > 3000 and type is None:
            return HeavyContainer(id, weight, "Heavy")
        elif type == "R":
            return RefrigeratedContainer(id, weight, "Refrigerated")
        elif type == "L":
            return LiquidContainer(id, weight, "Liquid")


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
