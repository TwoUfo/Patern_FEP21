import sqlite3
from mainapi.models.inputdata import Input


class Update:
    @staticmethod
    def ship(ship):
        conn = sqlite3.connect('mainapi\db\data.db')
        conn.cursor().execute('''DELETE FROM ship WHERE id = ?''', (ship.id,))
        conn.commit()
        conn.close()

        Input.ship(ship.id, ship.data.totalWeightCapacity, ship.data.maxNumberOfAllContainers, ship.data.maxNumberOfHeavyContainers, ship.data.maxNumberOfRefrigeratedContainers, ship.data.maxNumberOfLiquidContainers, ship.data.fuelConsumptionPerKM, ship.fuel, ship.port.id)
