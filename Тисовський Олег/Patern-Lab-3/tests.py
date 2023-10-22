from input import *
import unittest

class TestPortObjects(unittest.TestCase):

    def test_port(self):
        ships, ports, containers, items = get_data()
        self.assertEqual(ports[0].current_ships, ships[:3])
        self.assertEqual(ports[1].load_item_to_container(ports[1].items[0], ports[1].containers[0]), '<-This Item was loaded in Container->')
        self.assertEqual(ports[1].load_item_to_container(ports[1].items[-2], ports[1].containers[0]), '<-This Item to heavy to load in Container->')

    def test_ship(self):
        ships, ports, containers, items = get_data()
        self.assertEqual(ships[0].sail_to(ports[0]), 'Ship already is in this port')
        self.assertEqual(ships[0].sail_to(ports[1]), '<-The Ship does\'nt have enough fuel to sail->')
        ships[0].refuel(50000)
        self.assertEqual(ships[0].sail_to(ports[1]), '<-Ship starts going to new Port->')


if __name__ == '__main__':
    unittest.main()