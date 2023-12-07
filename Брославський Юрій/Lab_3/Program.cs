using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Lab_3
{
    internal class Program
    {
        public interface IShip
        {
            bool SailTo(Port destinationPort);
            void ReFuel(double newFuel);
            bool Load(Container container);
            bool UnLoad(Container container);
        }

        public abstract class Item
        {
            public int ID { get; private set; }
            public double Weight { get; private set; }
            public int Count { get; private set; }
            public int ContainerID { get; private set; }

            public Item(int id, double weight, int count, int containerID)
            {
                ID = id;
                Weight = weight;
                Count = count;
                ContainerID = containerID;
            }

            public abstract double GetTotalWeight();
        }

        public class SmallItem : Item
        {
            public SmallItem(int id, double weight, int count, int containerID) : base(id, weight, count, containerID) { }

            public override double GetTotalWeight()
            {
                return Weight * Count;
            }
        }

        public class HeavyItem : Item
        {
            public HeavyItem(int id, double weight, int count, int containerID) : base(id, weight, count, containerID) { }

            public override double GetTotalWeight()
            {
                return Weight * Count;
            }
        }

        public class RefrigeratedItem : Item
        {
            public RefrigeratedItem(int id, double weight, int count, int containerID) : base(id, weight, count, containerID) { }

            public override double GetTotalWeight()
            {
                return Weight * Count;
            }
        }

        public class LiquidItem : Item
        {
            public LiquidItem(int id, double weight, int count, int containerID) : base(id, weight, count, containerID) { }

            public override double GetTotalWeight()
            {
                return Weight * Count;
            }
        }

        public interface IItemFactory
        {
            Item CreateItem(int id, double weight, int count, int containerID, string type);
        }

        public class ItemFactory : IItemFactory
        {
            public Item CreateItem(int id, double weight, int count, int containerID, string type)
            {
                if (type == "SmallItem")
                {
                    return new SmallItem(id, weight, count, containerID);
                }
                else if (type == "HeavyItem")
                {
                    return new HeavyItem(id, weight, count, containerID);
                }
                else if (type == "RefrigeratedItem")
                {
                    return new RefrigeratedItem(id, weight, count, containerID);
                }
                else if (type == "LiquidItem")
                {
                    return new LiquidItem(id, weight, count, containerID);
                }
                else
                {
                    return null;
                }
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

            public Ship(int id, int totalWeightCapacity, int maxNumberOfAllContainers,
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

        public class Container
        {
            public int ID { get; private set; }
            public int Weight { get; private set; }

            public Container(int id, int weight)
            {
                ID = id;
                Weight = weight;
            }

            public virtual double Consumption()
            {
                return 2.50 * Weight;
            }

            public virtual void GetContainerInfo()
            {
                Console.WriteLine($"Container ID: {ID}");
                Console.WriteLine($"Weight: {Weight}");
            }
        }

        public class BasicContainer : Container
        {
            public BasicContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 2.50 * Weight;
            }

            public override void GetContainerInfo()
            {
                Console.WriteLine($"Container ID: {ID}");
                Console.WriteLine($"Weight: {Weight}");
                Console.WriteLine("Container Type: Basic");
            }
        }

        public class HeavyContainer : Container
        {
            public HeavyContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 3.00 * Weight;
            }

            public override void GetContainerInfo()
            {
                Console.WriteLine($"Container ID: {ID}");
                Console.WriteLine($"Weight: {Weight}");
                Console.WriteLine("Container Type: Heavy");
            }
        }

        public class RefrigeratedContainer : HeavyContainer
        {
            public RefrigeratedContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 5.00 * Weight;
            }

            public override void GetContainerInfo()
            {
                Console.WriteLine($"Container ID: {ID}");
                Console.WriteLine($"Weight: {Weight}");
                Console.WriteLine("Container Type: Refrigerated");
            }
        }

        public class LiquidContainer : HeavyContainer
        {
            public LiquidContainer(int id, int weight) : base(id, weight) { }

            public override double Consumption()
            {
                return 4.00 * Weight;
            }

            public override void GetContainerInfo()
            {
                Console.WriteLine($"Container ID: {ID}");
                Console.WriteLine($"Weight: {Weight}");
                Console.WriteLine("Container Type: Liquid");
            }
        }

        public interface IPort
        {
            void IncomingShip(Ship ship);
            void OutgoingShip(Ship ship);
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

        public class MainClass
        {
            public static void Main(string[] args)
            {
                string outputJson = File.ReadAllText("output.json");
                var outputData = JsonConvert.DeserializeObject<OutputData>(outputJson);

                Console.WriteLine("List of Ports:");
                foreach (var port in outputData.Ports)
                {
                    Console.WriteLine($"Port ID: {port.ID}");
                    Console.WriteLine($"Latitude: {port.Latitude}");
                    Console.WriteLine($"Longitude: {port.Longitude}");
                    Console.WriteLine($"Max Container Capacity: {port.MaxContainerCapacity}");

                    Console.WriteLine();
                }

                Console.WriteLine("List of Ships:");
                foreach (var ship in outputData.Ships)
                {
                    Console.WriteLine($"Ship ID: {ship.ID}");
                    Console.WriteLine($"Fuel: {ship.Fuel}");
                    Console.WriteLine($"Total Weight Capacity: {ship.TotalWeightCapacity}");
                    Console.WriteLine() ;
                    Console.WriteLine($"Max Number Of All Containers: {ship.MaxNumberOfAllContainers}");
                    Console.WriteLine($"Max Number Of Heavy Containers: {ship.MaxNumberOfHeavyContainers}");
                    Console.WriteLine($"Max Number Of Refrigerated Containers: {ship.MaxNumberOfRefrigeratedContainers}");
                    Console.WriteLine($"Max Number Of Liquid Containers: {ship.MaxNumberOfLiquidContainers}");
                    Console.WriteLine($"Fuel Consumption Per KM: {ship.FuelConsumptionPerKM}");
                }
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
            public double NewFuel { get; set; }
            public double Latitude { get; set; }
            public double Longitude { get; set; }
            public int MaxContainerCapacity { get; set; }
            public int MaxNumberOfHeavyContainers { get; set; }
            public int MaxNumberOfRefrigeratedContainers { get; set; }
            public int MaxNumberOfLiquidContainers { get; set; }
            public double FuelConsumptionPerKM { get; set; }
            public double Weight { get; set; }
            public int Count { get; set; }
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

            // Implement the distance calculation logic here.
            // Return the distance between two ports.
            return 0.0;
        }
    }
}
