using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    internal class Bill
    {
        private double LimitingAmount;
        private double CurrentDebt;
        private string CustomerName;

        public Bill(double limitingAmount)
        {
            LimitingAmount = limitingAmount;
            CurrentDebt = 0;
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
                Console.WriteLine("Exceeded bill limit. Action canceled.");
            }
        }

        public void Pay(double amount, string customerName)
        {
            if (amount <= 0)
            {
                Console.WriteLine("Payment amount must be greater than zero.");
                return;
            }

            if (CurrentDebt == 0)
            {
                Console.WriteLine($"{customerName}'s bill is already paid.");
                return;
            }

            if (amount >= CurrentDebt)
            {
                CurrentDebt = 0;
                Console.WriteLine($"{customerName}'s bill fully paid.");
            }
            else
            {
                CurrentDebt -= amount;
                Console.WriteLine($"Paid {amount:C} towards {customerName}'s bill. Remaining debt: {CurrentDebt:C}");
            }
        }

        public void ChangeTheLimit(double amount)
        {
            LimitingAmount = amount;
            Console.WriteLine($"Bill limit changed to {amount:C}");
        }

        public double GetCurrentDebt()
        {
            return CurrentDebt;
        }
    }
}
