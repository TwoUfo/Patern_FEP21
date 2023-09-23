using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    class Bill
    {
        public double LimitingAmount { get; set; }
        public double CurrentDebt { get; private set; }

        public Bill(double limitingAmount)
        {
            LimitingAmount = limitingAmount;
            CurrentDebt = 0.0;
        }
        public bool Check(double amount)
        {
            return CurrentDebt + amount <= LimitingAmount;
        }

        public void Add(double amount)
        {
            if (Check(amount))
            {
                CurrentDebt += amount;
            }
            else
            {
                Console.WriteLine("Ліміт перевищено. Неможливо додати більше до рахунку.");
            }
        }

        public void Pay(double amount)
        {
            if (amount <= CurrentDebt)
            {
                CurrentDebt -= amount;
            }
            else
            {
                Console.WriteLine("Сума платежу перевищує поточну заборгованість.");
            }
        }

        public void ChangeTheLimit(double amount)
        {
            LimitingAmount = amount;
        }
    }
}
