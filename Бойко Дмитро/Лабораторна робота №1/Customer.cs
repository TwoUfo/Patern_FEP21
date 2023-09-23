using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    class Customer
    {
        public int ID { get; set; }
        public string Name { get; set; }
        public int Age { get; set; }
        public Operator[] Operators { get; set; }
        public Bill[] Bills { get; set; }
        public double LimitingAmount { get; set; }

        public Customer(int iD, string name, int age, Operator[] operators, Bill[] bills, double limitingAmount)
        {
            ID = iD;
            Name = name;
            Age = age;
            Operators = operators;
            Bills = bills;
            LimitingAmount = limitingAmount;
        }
        public void Talk(int minutes, Customer other)
        {
            if (Operators != null && Operators.Length > 0)
            {
                double cost = Operators[0].CalculateTalkingCost(minutes, this);
                if (Age < 18 || Age > 65)
                {
                    cost *= (1 - Operators[0].DiscountRate / 100.0);
                }
                if (Bills != null && Bills.Length > 0)
                {
                    if (Bills[0].Check(cost))
                    {
                        Bills[0].Add(cost);
                    }
                    else
                    {
                        Console.WriteLine("Рахунок перевищено. Неможливо додати більше до рахунку.");
                    }
                }
            }
        }

        public void Message(int quantity, Customer other)
        {
            if (Operators != null && Operators.Length > 0 && other != null && other.Operators != null)
            {
                if (Operators[0] == other.Operators[0])
                {
                    double cost = Operators[0].CalculateMessageCost(quantity, this, other);
                    if (Bills != null && Bills.Length > 0)
                    {
                        if (Bills[0].Check(cost))
                        {
                            Bills[0].Add(cost);
                        }
                        else
                        {
                            Console.WriteLine("Рахунок перевищено. Неможливо додати більше до рахунку.");
                        }
                    }
                }
            }
        }
        public void Connection(double amount)
        {
            if (Operators != null && Operators.Length > 0)
            {
                double cost = Operators[0].CalculateNetworkCost(amount);
                if (Bills != null && Bills.Length > 0)
                {
                    if (Bills[0].Check(cost))
                    {
                        Bills[0].Add(cost);
                    }
                    else
                    {
                        Console.WriteLine("Рахунок перевищено. Неможливо додати більше до рахунку.");
                    }
                }
            }
        }
        public void PayBill(double amount)
        {
            if (Bills != null && Bills.Length > 0)
            {
                if (amount <= Bills[0].CurrentDebt)
                {
                    Bills[0].Pay(amount);
                }
                else
                {
                    Console.WriteLine("Сума платежу перевищує поточний борг.");
                }
            }
            else
            {
                Console.WriteLine("Неможливо здійснити платіж. Немає рахунку, пов'язаного з клієнтом.");
            }
        }
        public void ChangeOperator(Operator newOperator)
        {
            if (Operators != null && Operators.Length > 0 && newOperator != null)
            {
                Operators[0] = newOperator;
            }
        }

        public void ChangeBillLimit(double newLimit)
        {
            if (Bills != null && Bills.Length > 0)
            {
                Bills[0].ChangeTheLimit(newLimit);
            }
        }
        public double GetUsedAmount()
        {
            if (Bills != null && Bills.Length > 0)
            {
                return Bills[0].CurrentDebt;
            }
            return 0.0;
        }
        public double GetRemainingAmount()
        {
            if (Bills != null && Bills.Length > 0)
            {
                return LimitingAmount - Bills[0].CurrentDebt;
            }
            return LimitingAmount;
        }
    }
}
