using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Лабораторна_робота__2
{
    public interface IShip
    {
        bool SailTo(Port port);
        void Refuel(double amountOfFuel);
        bool Load(Container container);
        bool Unload(Container container);
    }

    // Ship class
    public class Ship : IShip
    {
        public int ID { get; private set; }
        public double Fuel { get; private set; }
        public Port CurrentPort { get; private set; }
        public int TotalWeightCapacity { get; private set; }
        public int MaxNumberOfAllContainers { get; private set; }
        public int MaxNumberOfHeavyContainers { get; private set; }
        public int MaxNumberOfRefrigeratedContainers { get; private set; }
        public int MaxNumberOfLiquidContainers { get; private set; }
        public double FuelConsumptionPerKM { get; private set; }
        public List<Container> Containers { get; private set; }

        public Ship(int id, double fuel, Port currentPort, int totalWeightCapacity,
                    int maxNumberOfAllContainers, int maxNumberOfHeavyContainers,
                    int maxNumberOfRefrigeratedContainers, int maxNumberOfLiquidContainers,
                    double fuelConsumptionPerKM)
        {
            ID = id;
            Fuel = fuel;
            CurrentPort = currentPort;
            TotalWeightCapacity = totalWeightCapacity;
            MaxNumberOfAllContainers = maxNumberOfAllContainers;
            MaxNumberOfHeavyContainers = maxNumberOfHeavyContainers;
            MaxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers;
            MaxNumberOfLiquidContainers = maxNumberOfLiquidContainers;
            FuelConsumptionPerKM = fuelConsumptionPerKM;
            Containers = new List<Container>();
        }

        public List<Container> GetCurrentContainers()
        {
            // TODO: Implement logic to get current containers
            return Containers.OrderBy(c => c.ID).ToList();
        }

        public bool SailTo(Port port)
        {
            // Розрахунок відстані між поточним і цільовим портами
            double distance = CurrentPort.GetDistance(port);

            // Розрахунок витрат палива для подолання відстані
            double fuelRequired = distance * FuelConsumptionPerKM;

            // Перевірка наявності достатнього палива
            if (Fuel >= fuelRequired)
            {
                Fuel -= fuelRequired;  // Зменшення палива
                CurrentPort.OutgoingShip(this);  // Вибуття з поточного порту
                CurrentPort = port;  // Зміна поточного порту
                port.IncomingShip(this);  // Вхід у цільовий порт
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
            // Поповнення палива
            Fuel += amountOfFuel;
            Console.WriteLine("Паливо поповнено. Поточний рівень палива: {0}", Fuel);
        }

        public bool Load(Container container)
        {
            // Перевірка обмежень корабля на кількість та типи контейнерів
            if (Containers.Count >= MaxNumberOfAllContainers)
            {
                Console.WriteLine("Корабель перевантажений. Неможливо завантажити більше контейнерів.");
                return false;
            }

            if (container is HeavyContainer && Containers.Count(c => c is HeavyContainer) >= MaxNumberOfHeavyContainers)
            {
                Console.WriteLine("Досягнуто максимальну кількість важких контейнерів.");
                return false;
            }

            if (container is RefrigeratedContainer && Containers.Count(c => c is RefrigeratedContainer) >= MaxNumberOfRefrigeratedContainers)
            {
                Console.WriteLine("Досягнуто максимальну кількість холодильних контейнерів.");
                return false;
            }

            if (container is LiquidContainer && Containers.Count(c => c is LiquidContainer) >= MaxNumberOfLiquidContainers)
            {
                Console.WriteLine("Досягнуто максимальну кількість рідких контейнерів.");
                return false;
            }

            // Додавання контейнера до списку контейнерів
            Containers.Add(container);
            Console.WriteLine("Контейнер {0} успішно завантажено в корабель.", container.ID);
            return true;
        }

        public bool Unload(Container container)
        {
            // Перевірка наявності контейнера у кораблі
            if (Containers.Contains(container))
            {
                // Видалення контейнера зі списку контейнерів
                Containers.Remove(container);
                Console.WriteLine("Контейнер {0} успішно розгружено з корабля.", container.ID);
                return true;
            }
            else
            {
                Console.WriteLine("Контейнер {0} не знайдено у кораблі.", container.ID);
                return false;
            }
        }

    }
}
