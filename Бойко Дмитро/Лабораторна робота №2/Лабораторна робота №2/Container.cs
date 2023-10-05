using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Лабораторна_робота__2
{
    public abstract class Container
    {
        public int ID { get; protected set; }
        public int Weight { get; protected set; }

        public abstract double Consumption();

        public bool Equals(Container other)
        {
            return this.GetType() == other.GetType() && this.ID == other.ID && this.Weight == other.Weight;
        }
    }

    // BasicContainer class
    public class BasicContainer : Container
    {
        public BasicContainer(int id, int weight)
        {
            ID = id;
            Weight = weight;
        }

        public override double Consumption()
        {
            return Weight * 2.5;
        }
    }

    // HeavyContainer class
    public class HeavyContainer : Container
    {
        public HeavyContainer(int id, int weight)
        {
            ID = id;
            Weight = weight;
        }

        public override double Consumption()
        {
            return Weight * 3.0;
        }
    }

    // RefrigeratedContainer class
    public class RefrigeratedContainer : HeavyContainer
    {
        public RefrigeratedContainer(int id, int weight) : base(id, weight) { }

        public override double Consumption()
        {
            return Weight * 5.0;
        }
    }

    // LiquidContainer class
    public class LiquidContainer : HeavyContainer
    {
        public LiquidContainer(int id, int weight) : base(id, weight) { }

        public override double Consumption()
        {
            return Weight * 4.0;
        }
    }
}
