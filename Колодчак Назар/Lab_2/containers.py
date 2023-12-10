from abc import ABC, abstractmethod
from uuid import uuid4


class Контейнер(ABC):
    def __init__(self, вага: float) -> None:
        self.id = uuid4()
        self.вага = вага

    @abstractmethod
    def споживання(self) -> float:
        pass

    def __eq__(self, інший) -> bool:
        перевірка_id = self.id == інший.id
        перевірка_ваги = self.вага == інший.вага
        перевірка_типу = self.__class__ == інший.__class__
        if перевірка_id and перевірка_ваги and перевірка_типу:
            return True
        else:
            return False


class ЗвичайнийКонтейнер(Контейнер):
    def __init__(self, вага: float) -> None:
        super().__init__(вага=вага)

    def споживання(self) -> float:
        return self.вага * 2.5


class ВажкийКонтейнер(Контейнер):
    def __init__(self, вага: float) -> None:
        super().__init__(вага=вага)

    def споживання(self) -> float:
        return self.вага * 3.0


class РефрижераторнийКонтейнер(ВажкийКонтейнер):
    def __init__(self, вага: float) -> None:
        super().__init__(вага=вага)

    def споживання(self) -> float:
        return self.вага * 5.0


class РідкийКонтейнер(ВажкийКонтейнер):
    def __init__(self, вага: float) -> None:
        super().__init__(вага=вага)

    def споживання(self) -> float:
        return self.вага * 4.0
