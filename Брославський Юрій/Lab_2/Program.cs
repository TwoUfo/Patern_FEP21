using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;

namespace Lab_2
{
    internal class Program
    {
        public abstract class Container
        {
            public int ID { get; private set; }
            public int Weight { get; private set; }

            public Container(int id, int weight)
            {
                ID = id;
                Weight = weight;
            }

            public abstract double Consumption();
        }

        public class BasicContainer : Container
        {
            public BasicContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 2.50 * Weight;
            }
        }

        public class HeavyContainer : Container
        {
            public HeavyContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 3.00 * Weight;
            }
        }

        public class RefrigeratedContainer : HeavyContainer
        {
            public RefrigeratedContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 5.00 * Weight;
            }
        }

        public class LiquidContainer : HeavyContainer
        {
            public LiquidContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 4.00 * Weight;
            }
        }

        public interface IPort
        {
            void IncomingShip(Ship ship);
            void OutgoingShip(Ship ship);
        }

        public interface IShip
        {
            bool SailTo(Port destinationPort);
            void ReFuel(double newFuel);
            bool Load(Container container);
            bool UnLoad(Container container);
        }

        public class Port : IPort
        {
            public int ID { get; private set; }
            public double Latitude { get; private set; }
            public double Longitude { get; private set; }
            public int MaxContainerCapacity { get; private set; } 

            private List<Container> containers = new List<Container>();
            private Ship currentShip = null;

            public Port(int id, double latitude, double longitude, int maxContainerCapacity)
            {
                ID = id;
                Latitude = latitude;
                Longitude = longitude;
                MaxContainerCapacity = maxContainerCapacity;
            }

            public void IncomingShip(Ship ship)
            {
                if (currentShip == null)
                {
                    currentShip = ship; 
                    currentShip.CurrentPort = this; 
                }
            }

            public void OutgoingShip(Ship ship)
            {
                if (currentShip == ship)
                {
                    currentShip = null; 
                }
            }

            public double GetDistance(Port other)
            {
                return CalculateDistance(this, other);
            }

            public bool LoadContainer(Container container)
            {
                if (containers.Count < MaxContainerCapacity)
                {
                    containers.Add(container);
                    return true;
                }
                return false;
            }

            public bool UnloadContainer(Container container)
            {
                if (containers.Contains(container))
                {
                    containers.Remove(container);
                    return true;
                }
                return false;
            }
        }

        public class Ship : IShip
        {
            public int ID { get; private set; }
            public double Fuel { get; private set; }
            public Port CurrentPort { get; set; }
            public int TotalWeightCapacity { get; private set; }
            public int MaxNumberOfAllContainers { get; private set; }
            public int MaxNumberOfHeavyContainers { get; private set; }
            public int MaxNumberOfRefrigeratedContainers { get; private set; }
            public int MaxNumberOfLiquidContainers { get; private set; }
            public double FuelConsumptionPerKM { get; private set; }

            private List<Container> containers = new List<Container>();

            public Ship(int id, int portID, int totalWeightCapacity, int maxNumberOfAllContainers,
                        int maxNumberOfHeavyContainers, int maxNumberOfRefrigeratedContainers,
                        int maxNumberOfLiquidContainers, double fuelConsumptionPerKM)
            {
                ID = id;
                Fuel = 0.0; 
                TotalWeightCapacity = totalWeightCapacity;
                MaxNumberOfAllContainers = maxNumberOfAllContainers;
                MaxNumberOfHeavyContainers = maxNumberOfHeavyContainers;
                MaxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers;
                MaxNumberOfLiquidContainers = maxNumberOfLiquidContainers;
                FuelConsumptionPerKM = fuelConsumptionPerKM;
            }

            public bool SailTo(Port destinationPort)
            {
                double distance = CurrentPort.GetDistance(destinationPort);
                double fuelRequired = distance * FuelConsumptionPerKM;

                if (Fuel >= fuelRequired)
                {
                    Fuel -= fuelRequired;
                    CurrentPort.OutgoingShip(this);
                    destinationPort.IncomingShip(this);
                    CurrentPort = destinationPort;
                    return true;
                }
                return false;
            }

            public void ReFuel(double newFuel)
            {
                Fuel += newFuel;
            }

            public bool Load(Container container)
            {

                if (containers.Count < MaxNumberOfAllContainers)
                {
                    if (container is HeavyContainer)
                    {
                        if (container is RefrigeratedContainer && containers.Count(c => c is RefrigeratedContainer) < MaxNumberOfRefrigeratedContainers)
                        {
                            containers.Add(container);
                            return true;
                        }
                        else if (container is LiquidContainer && containers.Count(c => c is LiquidContainer) < MaxNumberOfLiquidContainers)
                        {
                            containers.Add(container);
                            return true;
                        }
                        else if (containers.Count(c => c is HeavyContainer) < MaxNumberOfHeavyContainers)
                        {
                            containers.Add(container);
                            return true;
                        }
                    }
                    else if (container is BasicContainer)
                    {
                        containers.Add(container);
                        return true;
                    }
                }
                return false;
            }

            public bool UnLoad(Container container)
            {
                if (containers.Contains(container))
                {
                    containers.Remove(container);
                    return true;
                }
                return false;
            }

            public List<Container> GetCurrentContainers()
            {
                return containers;
            }
        }


        public class MainClass
        {
            public static void Main(string[] args)
            {
                string inputJson = File.ReadAllText("input.json");
                var inputData = JsonConvert.DeserializeObject<InputData>(inputJson);

                var ports = new List<Port>(); 
                var ships = new List<Ship>(); 
                var containers = new List<Container>();

                Console.WriteLine("Starting simulation...");

                foreach (var action in inputData.Actions)
                {
                    Console.WriteLine($"Processing action: {action.Type}");

                    if (action.Type == "create_port")
                    {
                        var newPort = new Port(action.PortID, action.Latitude, action.Longitude, action.MaxNumberOfAllContainers);
                        ports.Add(newPort);
                        Console.WriteLine($"Created Port ID: {action.PortID}");
                    }
                    else if (action.Type == "create_ship")
                    {
                        var newShip = new Ship(action.ShipID, action.PortID, action.TotalWeightCapacity,
                                               action.MaxNumberOfAllContainers, action.MaxNumberOfHeavyContainers,
                                               action.MaxNumberOfRefrigeratedContainers, action.MaxNumberOfLiquidContainers,
                                               action.FuelConsumptionPerKM);
                        ships.Add(newShip);

                        var currentPort = ports.FirstOrDefault(p => p.ID == action.PortID);
                        if (currentPort != null)
                        {
                            currentPort.IncomingShip(newShip);
                            newShip.CurrentPort = currentPort;
                        }
                        Console.WriteLine($"Created Ship ID: {action.ShipID}");
                    }
                    else if (action.Type == "load_container")
                    {
                        var ship = ships.FirstOrDefault(s => s.ID == action.ShipID);

                        if (ship != null)
                        {
                            Container newContainer = null;

                            if (action.ContainerType == "BasicContainer")
                            {
                                newContainer = new BasicContainer(action.ContainerID, action.MaxContainerCapacity);
                            }
                            else if (action.ContainerType == "HeavyContainer")
                            {
                                newContainer = new HeavyContainer(action.ContainerID, action.MaxContainerCapacity);
                            }
                            else if (action.ContainerType == "RefrigeratedContainer")
                            {
                                newContainer = new RefrigeratedContainer(action.ContainerID, action.MaxContainerCapacity);
                            }
                            else if (action.ContainerType == "LiquidContainer")
                            {
                                newContainer = new LiquidContainer(action.ContainerID, action.MaxContainerCapacity);
                            }

                            if (newContainer != null)
                            {
                                containers.Add(newContainer);

                                ship.Load(newContainer);
                            }
                            Console.WriteLine($"Loaded Container ID: {action.ContainerID} onto Ship ID: {action.ShipID}");
                        }
                    }
                    else if (action.Type == "unload_container")
                    {
                        var ship = ships.FirstOrDefault(s => s.ID == action.ShipID);

                        if (ship != null)
                        {
                            var container = containers.FirstOrDefault(c => c.ID == action.ContainerID);

                            if (container != null)
                            {
                                ship.UnLoad(container);
                                Console.WriteLine($"Unloaded Container ID: {action.ContainerID} from Ship ID: {action.ShipID}");
                            }
                        }
                    }
                    else if (action.Type == "sail_ship")
                    {
                        var ship = ships.FirstOrDefault(s => s.ID == action.ShipID);
                        var destinationPort = ports.FirstOrDefault(p => p.ID == action.DestinationPortID);

                        if (ship != null && destinationPort != null)
                        {
                            ship.SailTo(destinationPort);
                            Console.WriteLine($"Ship ID: {action.ShipID} sailed to Port ID: {action.DestinationPortID}");
                        }
                    }
                    else if (action.Type == "refuel_ship")
                    {
                        var ship = ships.FirstOrDefault(s => s.ID == action.ShipID);
                        if (ship != null)
                        {
                            ship.ReFuel(action.NewFuel);
                            Console.WriteLine($"Refueled Ship ID: {action.ShipID} with {action.NewFuel} fuel");
                        }
                    }
                    Console.WriteLine();
                }

                Console.WriteLine("Simulation completed.");

                var outputData = new OutputData
                {
                    Ports = ports,
                    Ships = ships
                };

                string outputJson = JsonConvert.SerializeObject(outputData, Formatting.Indented);
                File.WriteAllText("output.json", outputJson);
            }

        }


        public class InputData
        {
            public List<Action> Actions { get; set; }
        }

        public class Action
        {
            public string Type { get; set; }
            public int PortID { get; set; }
            public int ShipID { get; set; }
            public int ContainerID { get; set; }
            public int DestinationPortID { get; set; }
            public double NewFuel { get; set; }
            public double Latitude { get; set; }
            public double Longitude { get; set; }
            public int TotalWeightCapacity { get; set; }
            public int MaxNumberOfAllContainers { get; set; }
            public int MaxNumberOfHeavyContainers { get; set; }
            public int MaxNumberOfRefrigeratedContainers { get; set; }
            public int MaxNumberOfLiquidContainers { get; set; }
            public double FuelConsumptionPerKM { get; set; }
            public string ContainerType { get; set; }
            public int MaxContainerCapacity { get; set; }
        }

        public class OutputData
        {
            public List<Port> Ports { get; set; }
            public List<Ship> Ships { get; set; }
        }

        private static double CalculateDistance(Port port1, Port port2)
        {
            double lat1 = port1.Latitude;
            double lon1 = port1.Longitude;
            double lat2 = port2.Latitude;
            double lon2 = port2.Longitude;

            return 0.0;
        }
    }
}