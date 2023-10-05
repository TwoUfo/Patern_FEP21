using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Newtonsoft.Json;

namespace Лабораторна_робота__2
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;

            // Створення контейнерів
            Container basicContainer = new BasicContainer(1, 500);
            Container heavyContainer = new HeavyContainer(2, 1000);
            Container refrigeratedContainer = new RefrigeratedContainer(3, 800);
            Container liquidContainer = new LiquidContainer(4, 700);

            // Створення порту
            Port port = new Port(1, 52.5200, 13.4050); // Приклад координат для Берліна
            Port port2 = new Port(2, 48.8566, 2.3522);   // Порт 2 - Париж

            // Створення корабля та завантаження контейнерів
            Ship ship = new Ship(1, 1000, port, 5000, 10, 5, 3, 2, 0.2);
            ship.Load(basicContainer);
            ship.Load(heavyContainer);
            ship.Load(refrigeratedContainer);
            ship.Load(liquidContainer);

            // Виведення даних корабля
            Console.WriteLine("Дані корабля:");
            Console.WriteLine("ID: " + ship.ID);
            Console.WriteLine("Паливо: " + ship.Fuel);
            Console.WriteLine("Поточний порт ID: " + ship.CurrentPort.ID);
            Console.WriteLine("Загальна місткість корабля: " + ship.TotalWeightCapacity);
            Console.WriteLine("Максимальна кількість всіх контейнерів: " + ship.MaxNumberOfAllContainers);
            Console.WriteLine("Максимальна кількість важких контейнерів: " + ship.MaxNumberOfHeavyContainers);
            Console.WriteLine("Максимальна кількість холодильних контейнерів: " + ship.MaxNumberOfRefrigeratedContainers);
            Console.WriteLine("Максимальна кількість рідких контейнерів: " + ship.MaxNumberOfLiquidContainers);
            Console.WriteLine("Споживання палива на кілометр: " + ship.FuelConsumptionPerKM);

            // Виведення даних порту
            Console.WriteLine("\nДані порту 1:");
            Console.WriteLine("ID: " + port.ID);
            Console.WriteLine("Широта: " + port.Latitude);
            Console.WriteLine("Довгота: " + port.Longitude);

            Console.WriteLine("\nДані порту 2:");
            Console.WriteLine("ID: " + port2.ID);
            Console.WriteLine("Широта: " + port2.Latitude);
            Console.WriteLine("Довгота: " + port2.Longitude);

            // Виведення відстані між портами
            double distance = port.GetDistance(port2);
            Console.WriteLine("\nВідстань між портами: " + distance + " км");

            // Серіалізація в JSON
            string shipJson = JsonConvert.SerializeObject(ship, Newtonsoft.Json.Formatting.Indented);
            string portJson = JsonConvert.SerializeObject(port, Newtonsoft.Json.Formatting.Indented);
            string port2Json = JsonConvert.SerializeObject(port2, Newtonsoft.Json.Formatting.Indented);

            string filePath = "data.json";
            File.WriteAllText(filePath, shipJson + Environment.NewLine + portJson + Environment.NewLine + port2Json);
        }
    }
}
