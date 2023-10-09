#1. load data from JSON
import json
import random
from uuid import uuid4

portsID = [str(uuid4()) for i in range(5)]
randoming = random.randint(1,10)
myShips = []
for i in range(10):
   randoming = random.randint(1, 10)
   addedShipList = {}
   addedShipList["ship_id"] = str(uuid4())
   addedShipList["port_id"] = random.choice(portsID)
   addedShipList["ports_deliver"] = random.choice([i for i in portsID if i != addedShipList["ship_id"]])
   addedShipList["totalWeightCapacity"] = 200 * randoming
   addedShipList["maximumOfAllContainers"] = 4 * randoming
   addedShipList["maximumOfHeavyContainers"] = 1 * randoming
   addedShipList["maximumOfRefrigeratedContainers"] = round(1/2 * randoming)
   addedShipList["maximumOfLiquidContainers"] = 1 * randoming
   addedShipList["fuelConsumptionPerKM"] = 4 * randoming
   myShips.append(addedShipList)



myPorts = []
for i in range(5):
  addedPortList = {}
  addedPortList["port_id"] = portsID[i]
  addedPortList["ships"] = [ship for ship in myShips if ship["port_id"] == addedPortList["port_id"]]
  addedPortList["basic"] = random.randint(1, 10)
  addedPortList["heavy"] = random.randint(1, 8)
  addedPortList["refrigerated"] = random.randint(1, 5)
  addedPortList["liquid"] = random.randint(1, 5)
  myPorts.append(addedPortList)


json_object = json.dumps(myPorts, indent=2)


from containers import *
from port import IPort, PortClass
from ship import IShip, ShipСlass, ConfigShip

with open("input.json", "w") as outfile:
  outfile.write(json_object)

containers = [BasicContainer(250), BasicContainer(450), HeavyContainer(350), RefrigeratedContainer(250.5), LiquidContainer(124)]
ports = [PortClass(
  myPorts[i]["port_id"],
  round(random.uniform(0, 10**6)/10**6, 6),
  round(random.uniform(0, 10**6)/10**6, 6),
  containers
) for i in range(len(myPorts))]
ships = [ShipСlass(
    myShips[i]["ship_id"],
    ports,
    ConfigShip(
        myShips[i]["totalWeightCapacity"],
        myShips[i]["maximumOfAllContainers"],
        myShips[i]["maximumOfHeavyContainers"],
        myShips[i]["maximumOfRefrigeratedContainers"],
        myShips[i]["maximumOfLiquidContainers"],
        myShips[i]["fuelConsumptionPerKM"]
    ),
    containers,
    random.randint(100,1000)
  ) for i in range(len(myShips))]
for i in range(len(containers)-1):
  for ship in ships:
    if type(containers[i]) == str:
      break
    containerID = containers[i].id
    ship.load(containerID)
    ship.unload(containerID)
    ship.sailTo(ports[i])
  i+=1