from random import randint
from helpers import SERIALIZATION_FILE_PATH, DESERIALIZATION_FILE_PATH, save, load


def main():
    ports = load(DESERIALIZATION_FILE_PATH)

    port_1 = ports[randint(0, len(ports) - 1)]
    port_2 = ports[randint(0, len(ports) - 1)]

    while port_1.id == port_2.id:
        port_1 = ports[randint(0, len(ports) - 1)]
        port_2 = ports[randint(0, len(ports) - 1)]

    ship = port_1.current_ships[0]

    print(f"Selected ship with id: {ship.id}. Currently its fuel level is: {ship.fuel}")
    ship.refuel(1000000)
    print(f"Ship was refueled. Now its fuel level is: {ship.fuel}")

    print("Loading containers...")
    ship.load()

    print(f"Ship is loaded with {len(ship.containers)} containers")
    print(f"Sending ship to port with id: {port_2.id}")
    ship.sail_to(port_2)

    print(f"Unloading containers from ship with id {ship.id}")
    ship.unload()

    print(f"Saving info into {SERIALIZATION_FILE_PATH} file...")

    save(SERIALIZATION_FILE_PATH, ports)


if __name__ == "__main__":
    main()
