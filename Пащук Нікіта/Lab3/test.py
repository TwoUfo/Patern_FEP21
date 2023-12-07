import unittest
from unittest.mock import Mock, MagicMock
from Port import Port, ContainerDetails
from Ship import DataShip, MakeShip
from Container import Container
from Item import IItem
from uuid import uuid4


class TestPort(unittest.TestCase):
    def setUp(self):
        self.port = Port(str(uuid4()), 40.0, -75.0, ContainerDetails(10, 20, 5, 3))

    def test_get_distance(self):
        other_port = Port(str(uuid4()), 41.0, -74.0, ContainerDetails(5, 15, 10, 2))

        with unittest.mock.patch.object(self.port, 'get_distance', return_value=139.69) as distance_mock:
            distance = self.port.get_distance(other_port)

            self.assertAlmostEqual(distance, 139.69, places=1)
            distance_mock.assert_called_once_with(other_port)


class TestShip(unittest.TestCase):
    def setUp(self):
        self.data_ship = DataShip(60000, 100, 40, 20, 10, 30, 5.0)
        self.port = Port(str(uuid4()), 40.0, -75.0, ContainerDetails(10, 20, 5, 3))
        self.ship = MakeShip.check_type(str(uuid4()), 10000, self.port, self.data_ship)

    def test_load_and_unload(self):
        container = Container.check_category(str(uuid4()), 5000, "R")
        self.ship.load = MagicMock(return_value=False)
        result = self.ship.load(container)
        self.assertFalse(result)
        self.assertEqual(len(self.ship.containers), 0)


class TestContainer(unittest.TestCase):
    def test_consumption(self):
        basic_container = Container.check_category(str(uuid4()), 3000, "Basic")
        heavy_container = Container.check_category(str(uuid4()), 4000)

        basic_container.consumption = Mock(return_value=7500.0)
        heavy_container.consumption = Mock(return_value=12000.0)

        self.assertEqual(basic_container.consumption(), 7500.0)
        basic_container.consumption.assert_called_once()

        self.assertEqual(heavy_container.consumption(), 12000.0)
        heavy_container.consumption.assert_called_once()


class TestItem(unittest.TestCase):
    def test_getTotalWeight(self):
        small_item = IItem.check_type(str(uuid4()), 100, 5)
        heavy_item = IItem.check_type(str(uuid4()), 500, 2)

        small_item.getTotalWeight = Mock(return_value=500)
        heavy_item.getTotalWeight = Mock(return_value=1000)

        self.assertEqual(small_item.getTotalWeight(), 500)
        small_item.getTotalWeight.assert_called_once()

        self.assertEqual(heavy_item.getTotalWeight(), 1000)
        heavy_item.getTotalWeight.assert_called_once()


if __name__ == '__main__':
    unittest.main()
