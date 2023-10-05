using Lab_1;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    class Operator
    {
        public int ID { get; set; }
        public double TalkingCharge { get; set; }
        public double MessageCost { get; set; }
        public double NetworkCharge { get; set; }
        public int DiscountRate { get; set; }

        public Operator(int id, double talkingCharge, double messageCost, double networkCharge, int discountRate)
        {
            ID = id;
            TalkingCharge = talkingCharge;
            MessageCost = messageCost;
            NetworkCharge = networkCharge;
            DiscountRate = discountRate;
        }

        public double CalculateTalkingCost(int minute, Customer customer)
        {
            double cost = minute * TalkingCharge;
            if (customer.Age < 18 || customer.Age > 65)
            {
                cost *= (1 - DiscountRate / 100.0);
            }
            return cost;
        }
        public double CalculateMessageCost(int quantity, Customer customer, Customer other)
        {
            double cost = quantity * MessageCost;
            if (customer.Operators != null && other.Operators != null && customer.Operators.Length > 0)
            {
                if (customer.Operators[0] == other.Operators[0])
                {
                    cost *= (1 - customer.Operators[0].DiscountRate / 100.0);
                }
            }
            return cost;
        }
        public double CalculateNetworkCost(double amount)
        {
            return amount * NetworkCharge;
        }
    }
}
