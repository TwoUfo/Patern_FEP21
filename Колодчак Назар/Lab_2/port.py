from abc import ABC, abstractmethod
from uuid import uuid4
from ship import Корабель

import haversine as hs


class IПорт(ABC):

    @abstractmethod
    def вхід_корабля(self, корабель: Корабель):
        pass

    @abstractmethod
    def вихід_корабля(self, корабель: Корабель):
        pass


class Порт(IПорт):

    def __init__(self, широта: float, довгота: float) -> None:
        self.id = uuid4()
        self.широта = широта
        self.довгота = довгота
        self.контейнери = []
        self.історія_кораблів = []
        self.поточні_кораблі = []

    def отримати_відстань(self, порт) -> float:
        відстань = hs.haversine((self.широта, self.довгота), (порт.широта, порт.довгота))
        return відстань

    def вхід_корабля(self, корабель):
        if корабель.__class__ == 'Корабель':
            print('!-Даний об\'єкт не є Кораблем-!')
        elif корабель not in self.поточні_кораблі:
            self.поточні_кораблі.append(корабель)
            print('<-Корабель прибув до нового порту->')
        else:
            print('!-Помилка-!')

    def вихід_корабля(self, корабель: Корабель):
        if корабель.__class__ == 'Корабель':
            print('!-Даний об\'єкт не є Кораблем-!')
        elif корабель in self.поточні_кораблі:
            self.історія_кораблів.append(корабель)
            self.поточні_кораблі.remove(корабель)
            print('<-Корабель покинув поточний порт->')
        else:
            print('!-Помилка-!')
