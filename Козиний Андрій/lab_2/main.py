from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship


basic_container = BasicContainer(1, 2000)
heavy_container = HeavyContainer(2, 4000)
refrigerated_container = RefrigeratedContainer(3, 3500)
liquid_container = LiquidContainer(4, 4000)

port1 = Port(1, 40.7128, 74.0060)
port2 = Port(2, 34.0522, 118.2437)

ship = Ship(1, 750, port1, 3000, 8, 3, 2, 1, 0.15)

containers = [basic_container, heavy_container, refrigerated_container, liquid_container]

for container in containers:
    print(f"Контейнер ID {container.ID} - Вага: {container.weight} кг")
    print()

container1 = BasicContainer(5, 2500)
container2 = BasicContainer(6, 2500)
container3 = HeavyContainer(7, 3500)

print(f"Порт 1 - ID: {port1.ID}, Широта: {port1.latitude}, Довгота: {port1.longitude}")
print(f"Порт 2 - ID: {port2.ID}, Широта: {port2.latitude}, Довгота: {port2.longitude}")

print("Дані корабля:")
print(f"ID: {ship.ID}")
print(f"Пальне: {ship.fuel} літрів")
print(f"Поточний порт ID: {ship.currentPort.ID}")
print(f"Загальна ємність кораблика: {ship.totalWeightCapacity} кг")
print(f"Максимальна кількість контейнерів: {ship.maxNumberOfAllContainers}")
print(f"Максимальна кількість HeavyContainer: {ship.maxNumberOfHeavyContainers}")
print(f"Максимальна кількість RefrigeratedContainer: {ship.maxNumberOfRefrigeratedContainers}")
print(f"Максимальна кількість LiquidContainer: {ship.maxNumberOfLiquidContainers}")
print(f"Споживання пального " f": {ship.fuelConsumptionPerKM} на КМ")