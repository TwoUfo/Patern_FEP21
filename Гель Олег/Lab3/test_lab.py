import unittest
from container import BasicContainer
from port import Port
from ship import Ship

class TestPortShipContainer(unittest.TestCase):
    def test_add_container_to_port_and_ship(self):
        port = Port(1, 40.7128, -74.0060)
        ship = Ship(1, 1000, port, 5000, 10, 5, 3, 2, 0.2)
        container = BasicContainer("C1", 2500)

if __name__ == '__main__':
    unittest.main()
