from abc import abstractmethod, ABC
from uuid import uuid4


class IItem(ABC):
    def __init__(self, weight: float, count: int, container_id: int) -> None:
        self.id = uuid4()
        self.weight = weight
        self.count = count
        self.container_id = container_id

    @staticmethod
    def init_item(container, weight: float, count: int, container_id: int):
        if container.type == 'Basic':
            return Small(weight, count, container_id)
        if container.type == 'Heavy':
            return Heavy(weight, count, container_id)
        if container.type == 'Refrigerated':
            return Refrigerated(weight, count, container_id)
        if container.type == 'Liquid':
            return Liquid(weight, count, container_id)

class Small(IItem):
    def __init__(self, weight: float, count: int, container_id: int):
        super().__init__(weight, count, container_id)


class Heavy(IItem):
    def __init__(self, weight: float, count: int, container_id: int):
        super().__init__(weight, count, container_id)


class Refrigerated(IItem):
    def __init__(self, weight: float, count: int, container_id: int):
        super().__init__(weight, count, container_id)


class Liquid(IItem):
    def __init__(self, weight: float, count: int, container_id: int):
        super().__init__(weight, count, container_id)


