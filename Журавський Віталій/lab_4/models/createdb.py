import sqlite3

conn = sqlite3.connect('../db/data.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE port (
    id INTEGER PRIMARY KEY,
    latitude REAL,
    longitude REAL
);
''')

cursor.execute('''
CREATE TABLE ship (
    id INTEGER PRIMARY KEY,
    totalWeightCapacity INTEGER,
    maxNumberOfAllContainers INTEGER,
    maxNumberOfHeavyContainers INTEGER,
    maxNumberOfRefrigeratedContainers INTEGER,
    maxNumberOfLiquidContainers INTEGER,
    fuelConsumptionPerKM REAL,
    fuel REAL,
    port_id INTEGER
);

''')

cursor.execute('''
CREATE TABLE container (
    id INTEGER PRIMARY KEY,
    type TEXT,
    weight REAL,
    port_id INTEGER
);

''')


conn.commit()
cursor.close()
conn.close()
