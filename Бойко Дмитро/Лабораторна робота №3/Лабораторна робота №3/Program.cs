using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Newtonsoft.Json;


namespace Лабораторна_робота__3
{
    public abstract class Item
    {
        public int ID { get; protected set; }
        public double Weight { get; protected set; }
        public int Count { get; protected set; }
        public int ContainerID { get; protected set; }

        public abstract double GetTotalWeight();
    }

    public class Small : Item
    {
        public Small(int id, double weight, int count, int containerID)
        {
            ID = id;
            Weight = weight;
            Count = count;
            ContainerID = containerID;
        }

        public override double GetTotalWeight()
        {
            return Weight * Count;
        }
    }

    public class Heavy : Item
    {
        public Heavy(int id, double weight, int count, int containerID)
        {
            ID = id;
            Weight = weight;
            Count = count;
            ContainerID = containerID;
        }

        public override double GetTotalWeight()
        {
            return Weight * Count;
        }
    }

    public class Refrigerated : Item
    {
        public Refrigerated(int id, double weight, int count, int containerID)
        {
            ID = id;
            Weight = weight;
            Count = count;
            ContainerID = containerID;
        }

        public override double GetTotalWeight()
        {
            return Weight * Count;
        }
    }

    public class Liquid : Item
    {
        public Liquid(int id, double weight, int count, int containerID)
        {
            ID = id;
            Weight = weight;
            Count = count;
            ContainerID = containerID;
        }

        public override double GetTotalWeight()
        {
            return Weight * Count;
        }
    }

    public interface IShip
    {
        bool SailTo(Port port);
        void Refuel(double amountOfFuel);
        bool LoadItem(Item item);
        bool UnloadItem(Item item);
    }

    public interface IShipBuilder
    {
        IShipBuilder SetFuel(double fuel);
        IShipBuilder SetTotalWeightCapacity(int totalWeightCapacity);
        IShipBuilder SetMaxNumberOfAllItems(int maxNumberOfAllItems);
        IShipBuilder SetMaxNumberOfHeavyItems(int maxNumberOfHeavyItems);
        IShipBuilder SetMaxNumberOfRefrigeratedItems(int maxNumberOfRefrigeratedItems);
        IShipBuilder SetMaxNumberOfLiquidItems(int maxNumberOfLiquidItems);
        IShipBuilder SetFuelConsumptionPerKM(double fuelConsumptionPerKM);
        IShip Build();
    }

    public class Ship : IShip
    {
        public int ID { get; private set; }
        public double Fuel { get; private set; }
        public Port CurrentPort { get; set; }
        public int TotalWeightCapacity { get; private set; }
        public int MaxNumberOfAllItems { get; private set; }
        public int MaxNumberOfHeavyItems { get; private set; }
        public int MaxNumberOfRefrigeratedItems { get; private set; }
        public int MaxNumberOfLiquidItems { get; private set; }
        public double FuelConsumptionPerKM { get; private set; }
        public List<Item> Items { get; private set; }

        public Ship(int id, double fuel, Port currentPort, int totalWeightCapacity,
                    int maxNumberOfAllItems, int maxNumberOfHeavyItems,
                    int maxNumberOfRefrigeratedItems, int maxNumberOfLiquidItems,
                    double fuelConsumptionPerKM)
        {
            ID = id;
            Fuel = fuel;
            CurrentPort = currentPort;
            TotalWeightCapacity = totalWeightCapacity;
            MaxNumberOfAllItems = maxNumberOfAllItems;
            MaxNumberOfHeavyItems = maxNumberOfHeavyItems;
            MaxNumberOfRefrigeratedItems = maxNumberOfRefrigeratedItems;
            MaxNumberOfLiquidItems = maxNumberOfLiquidItems;
            FuelConsumptionPerKM = fuelConsumptionPerKM;
            Items = new List<Item>();
        }

        public bool SailTo(Port port)
        {
            double distance = CurrentPort.GetDistance(port);
            double fuelRequired = distance * FuelConsumptionPerKM;

            if (Fuel >= fuelRequired)
            {
                Fuel -= fuelRequired;
                CurrentPort.OutgoingShip(this);
                CurrentPort = port;
                port.IncomingShip(this);
                return true;
            }
            else
            {
                Console.WriteLine("Недостатньо палива для подорожі до цільового порту.");
                return false;
            }
        }

        public void Refuel(double amountOfFuel)
        {
            Fuel += amountOfFuel;
            Console.WriteLine("Паливо поповнено. Поточний рівень палива: {0}", Fuel);
        }

        public bool LoadItem(Item item)
        {
            if (Items.Count >= MaxNumberOfAllItems)
            {
                Console.WriteLine("Корабель перевантажений. Неможливо завантажити більше товарів.");
                return false;
            }

            if (item is Heavy && Items.Count(i => i is Heavy) >= MaxNumberOfHeavyItems)
            {
                Console.WriteLine("Досягнуто максимальну кількість важких товарів.");
                return false;
            }

            if (item is Refrigerated && Items.Count(i => i is Refrigerated) >= MaxNumberOfRefrigeratedItems)
            {
                Console.WriteLine("Досягнуто максимальну кількість холодильних товарів.");
                return false;
            }

            if (item is Liquid && Items.Count(i => i is Liquid) >= MaxNumberOfLiquidItems)
            {
                Console.WriteLine("Досягнуто максимальну кількість рідких товарів.");
                return false;
            }

            Items.Add(item);
            Console.WriteLine("Товар {0} успішно завантажено в корабель.", item.ID);
            return true;
        }

        public bool UnloadItem(Item item)
        {
            if (Items.Contains(item))
            {
                Items.Remove(item);
                Console.WriteLine("Товар {0} успішно розгружено з корабля.", item.ID);
                return true;
            }
            else
            {
                Console.WriteLine("Товар {0} не знайдено у кораблі.", item.ID);
                return false;
            }
        }
    }

    public class Port
    {
        public int ID { get; private set; }
        public double Latitude { get; private set; }
        public double Longitude { get; private set; }
        public List<Item> Items { get; private set; }
        public List<Ship> ShipHistory { get; private set; }
        public List<Ship> CurrentShips { get; private set; }

        public Port(int id, double latitude, double longitude)
        {
            ID = id;
            Latitude = latitude;
            Longitude = longitude;
            Items = new List<Item>();
            ShipHistory = new List<Ship>();
            CurrentShips = new List<Ship>();
        }

        public double GetDistance(Port other)
        {
            const double EarthRadius = 6371;

            double lat1 = Latitude * Math.PI / 180;
            double lon1 = Longitude * Math.PI / 180;
            double lat2 = other.Latitude * Math.PI / 180;
            double lon2 = other.Longitude * Math.PI / 180;

            double dlat = lat2 - lat1;
            double dlon = lon2 - lon1;

            double a = Math.Pow(Math.Sin(dlat / 2), 2) + Math.Cos(lat1) * Math.Cos(lat2) * Math.Pow(Math.Sin(dlon / 2), 2);
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));

            return EarthRadius * c;
        }

        public void IncomingShip(Ship ship)
        {
            if (ship != null && !CurrentShips.Contains(ship))
            {
                CurrentShips.Add(ship);
            }
        }

        public void OutgoingShip(Ship ship)
        {
            if (ship != null && CurrentShips.Contains(ship))
            {
                CurrentShips.Remove(ship);
                ShipHistory.Add(ship);
            }
        }
    }

    public class ShipBuilder : IShipBuilder
    {
        private int ID;
        private double Fuel;
        private Port CurrentPort;
        private int TotalWeightCapacity;
        private int MaxNumberOfAllItems;
        private int MaxNumberOfHeavyItems;
        private int MaxNumberOfRefrigeratedItems;
        private int MaxNumberOfLiquidItems;
        private double FuelConsumptionPerKM;

        public IShipBuilder SetFuel(double fuel)
        {
            Fuel = fuel;
            return this;
        }

        public IShipBuilder SetTotalWeightCapacity(int totalWeightCapacity)
        {
            TotalWeightCapacity = totalWeightCapacity;
            return this;
        }

        public IShipBuilder SetMaxNumberOfAllItems(int maxNumberOfAllItems)
        {
            MaxNumberOfAllItems = maxNumberOfAllItems;
            return this;
        }

        public IShipBuilder SetMaxNumberOfHeavyItems(int maxNumberOfHeavyItems)
        {
            MaxNumberOfHeavyItems = maxNumberOfHeavyItems;
            return this;
        }

        public IShipBuilder SetMaxNumberOfRefrigeratedItems(int maxNumberOfRefrigeratedItems)
        {
            MaxNumberOfRefrigeratedItems = maxNumberOfRefrigeratedItems;
            return this;
        }

        public IShipBuilder SetMaxNumberOfLiquidItems(int maxNumberOfLiquidItems)
        {
            MaxNumberOfLiquidItems = maxNumberOfLiquidItems;
            return this;
        }

        public IShipBuilder SetFuelConsumptionPerKM(double fuelConsumptionPerKM)
        {
            FuelConsumptionPerKM = fuelConsumptionPerKM;
            return this;
        }

        public IShip Build()
        {
            return new Ship(ID, Fuel, CurrentPort, TotalWeightCapacity, MaxNumberOfAllItems,
                            MaxNumberOfHeavyItems, MaxNumberOfRefrigeratedItems,
                            MaxNumberOfLiquidItems, FuelConsumptionPerKM);
        }
    }

    public static class Program
    {
        public static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;

            // Створення порту
            Port port = new Port(1, 52.5200, 13.4050); // Приклад координат для Берліна
            Port port2 = new Port(2, 48.8566, 2.3522);   // Порт 2 - Париж

            // Створення корабля за допомогою будівельника
            IShipBuilder shipBuilder = new ShipBuilder();
            Ship ship = (Ship)shipBuilder
                .SetFuel(1000)
                .SetTotalWeightCapacity(5000)
                .SetMaxNumberOfAllItems(10)
                .SetMaxNumberOfHeavyItems(5)
                .SetMaxNumberOfRefrigeratedItems(3)
                .SetMaxNumberOfLiquidItems(2)
                .SetFuelConsumptionPerKM(0.2)
                .Build();

            ship.CurrentPort = port; // Присвоєння поточного порту кораблю

            // Створення товарів
            Item smallItem = new Small(1, 2, 20, 1);
            Item heavyItem = new Heavy(2, 10, 5, 2);
            Item refrigeratedItem = new Refrigerated(3, 8, 15, 3);
            Item liquidItem = new Liquid(4, 6, 12, 4);

            // Виведення даних корабля
            Console.WriteLine("Дані корабля:");
            Console.WriteLine("ID: " + ship.ID);
            Console.WriteLine("Паливо: " + ship.Fuel);
            Console.WriteLine("Поточний порт ID: " + ship.CurrentPort.ID);
            Console.WriteLine("Загальна місткість корабля: " + ship.TotalWeightCapacity);
            Console.WriteLine("Максимальна кількість всіх товарів: " + ship.MaxNumberOfAllItems);
            Console.WriteLine("Максимальна кількість важких товарів: " + ship.MaxNumberOfHeavyItems);
            Console.WriteLine("Максимальна кількість холодильних товарів: " + ship.MaxNumberOfRefrigeratedItems);
            Console.WriteLine("Максимальна кількість рідких товарів: " + ship.MaxNumberOfLiquidItems);
            Console.WriteLine("Споживання палива на кілометр: " + ship.FuelConsumptionPerKM);

            // Завантаження товарів в корабель
            ship.LoadItem(smallItem);
            ship.LoadItem(heavyItem);
            ship.LoadItem(refrigeratedItem);
            ship.LoadItem(liquidItem);

            // Виведення інформації про контейнер
            var container = new List<Item> { smallItem, heavyItem, refrigeratedItem, liquidItem };
            double containerWeight = container.Sum(item => item.GetTotalWeight());
            Console.WriteLine("\nІнформація про контейнер:");
            Console.WriteLine("Загальна вага контейнера: " + containerWeight + " кг");

            Console.WriteLine("Товари в контейнері:");
            foreach (var item in container)
            {
                if (item is Small)
                {
                    Console.WriteLine("Товар ID: " + item.ID + ", Тип: Small, Кількість: " + item.Count);
                }
                else if (item is Heavy)
                {
                    Console.WriteLine("Товар ID: " + item.ID + ", Тип: Heavy, Кількість: " + item.Count);
                }
                else if (item is Refrigerated)
                {
                    Console.WriteLine("Товар ID: " + item.ID + ", Тип: Refrigerated, Кількість: " + item.Count);
                }
                else if (item is Liquid)
                {
                    Console.WriteLine("Товар ID: " + item.ID + ", Тип: Liquid, Кількість: " + item.Count);
                }
            }

            // Виведення інформації про витрати палива корабля
            Console.WriteLine("Витрати палива корабля під час подорожі:");
            double distanceTraveled = port.GetDistance(port2);
            double fuelConsumed = distanceTraveled * ship.FuelConsumptionPerKM;
            Console.WriteLine("Відстань подорожі: " + distanceTraveled.ToString("F1") + " км");
            Console.WriteLine("Спожито палива: " + fuelConsumed.ToString("F1") + " літрів");

            // Серіалізація в JSON
            string shipJson = JsonConvert.SerializeObject(ship, Newtonsoft.Json.Formatting.Indented);
            string portJson = JsonConvert.SerializeObject(port, Newtonsoft.Json.Formatting.Indented);
            string port2Json = JsonConvert.SerializeObject(port2, Newtonsoft.Json.Formatting.Indented);

            string filePath = "data.json";
            File.WriteAllText(filePath, shipJson + Environment.NewLine + portJson + Environment.NewLine + port2Json);
        }
    }
}
