using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    internal class Customer
    {
        private int ID;
        private string Name;
        private int Age;
        private Operator[] Operators;
        private Bill Bill;

        public Customer(int id, string name, int age, Operator[] operators, Bill[] bills, double limitingAmount)
        {
            ID = id;
            Name = name;
            Age = age;
            Operators = operators;
            Bill = new Bill(limitingAmount);
            bills[id] = Bill;
        }

        public string GetName()
        {
            return Name;
        }

        public void Talk(int minute, Customer other)
        {
            Operator customerOperator = Operators[ID];
            Operator otherOperator = Operators[other.ID];

            double charge = customerOperator.CalculateTalkingCost(minute, this);

            if (Age < 18 || Age > 65)
            {
                charge -= charge * customerOperator.GetDiscountRate() / 100.0;
            }

            Bill.Add(charge);

            Console.WriteLine($"{Name} talked to {other.GetName()} for {minute} minutes. Charge: {charge:C}");
        }

        public void Message(int quantity, Customer other)
        {
            Operator customerOperator = Operators[ID];
            Operator otherOperator = Operators[other.ID];

            double charge = customerOperator.CalculateMessageCost(quantity, this, other);

            if (customerOperator == otherOperator)
            {
                charge -= charge * customerOperator.GetDiscountRate() / 100.0;
            }

            Bill.Add(charge);

            Console.WriteLine($"{Name} sent {quantity} messages to {other.GetName()}. Charge: {charge:C}");
        }

        public void Connection(double amount)
        {
            Operator customerOperator = Operators[ID];

            double charge = customerOperator.CalculateNetworkCost(amount);

            Bill.Add(charge);

            Console.WriteLine($"{Name} connected to the internet using {amount} MB. Charge: {charge:C}");
        }

        public void PayBill(double amount)
        {
            Bill.Pay(amount, GetName());
        }

        public void ChangeOperator(Operator newOperator)
        {
            Operators[ID] = newOperator;
            Console.WriteLine($"{Name} changed operator to Operator {newOperator.GetID()}");
        }

        public void ChangeBillLimit(double newLimit)
        {
            Bill.ChangeTheLimit(newLimit);
            Console.WriteLine($"{Name} changed the bill limit to {newLimit:C}");
        }

        public Bill GetBill()
        {
            return Bill;
        }
    }
}
