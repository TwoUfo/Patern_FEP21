import sqlite3


class Input:
    @staticmethod
    def ship(ID, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers, maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, fuelConsumptionPerKM, fuel, port_id):
        conn = sqlite3.connect('mainapi\db\data.db')

        command = '''INSERT INTO ship (id, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers, maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, fuelConsumptionPerKM, fuel, port_id) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        val = (ID, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers, maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, fuelConsumptionPerKM, fuel, port_id)
        conn.cursor().execute(command, val)
        conn.commit()
        conn.close()

    @staticmethod
    def port(ID, latitude, longitude):
        conn = sqlite3.connect('mainapi\db\data.db')
        command = '''INSERT INTO port (id, latitude, longitude) VALUES(?, ?, ?)'''
        val = (ID, latitude, longitude)
        conn.cursor().execute(command, val)
        conn.commit()
        conn.close()

    @staticmethod
    def container(ID, Type, weight, port_id):
        conn = sqlite3.connect('mainapi\db\data.db')
        command = '''INSERT INTO container (id, type, weight, port_id) VALUES(?, ?, ?, ?)'''
        val = (ID, Type, weight, port_id)
        conn.cursor().execute(command, val)
        conn.commit()
        conn.close()

