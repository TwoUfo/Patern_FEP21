using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Лабораторна_робота__2
{
    public interface IPort
    {
        void IncomingShip(Ship ship);
        void OutgoingShip(Ship ship);
    }

    // Port class
    public class Port : IPort
    {
        public int ID { get; private set; }
        public double Latitude { get; private set; }
        public double Longitude { get; private set; }
        public List<Container> Containers { get; private set; }
        public List<Ship> ShipHistory { get; private set; }
        public List<Ship> CurrentShips { get; private set; }

        public Port(int id, double latitude, double longitude)
        {
            ID = id;
            Latitude = latitude;
            Longitude = longitude;
            Containers = new List<Container>();
            ShipHistory = new List<Ship>();
            CurrentShips = new List<Ship>();
        }

        public double GetDistance(Port other)
        {
            // Calculate distance using haversine formula
            const double EarthRadius = 6371;  // Earth radius in kilometers

            double lat1 = Latitude * Math.PI / 180;
            double lon1 = Longitude * Math.PI / 180;
            double lat2 = other.Latitude * Math.PI / 180;
            double lon2 = other.Longitude * Math.PI / 180;

            double dlat = lat2 - lat1;
            double dlon = lon2 - lon1;

            double a = Math.Pow(Math.Sin(dlat / 2), 2) + Math.Cos(lat1) * Math.Cos(lat2) * Math.Pow(Math.Sin(dlon / 2), 2);
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));

            return EarthRadius * c;  // Distance in kilometers
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
}
