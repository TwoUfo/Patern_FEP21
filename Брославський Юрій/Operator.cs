using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_1
{
    internal class Operator
    {
        private int ID;
        private double TalkingCharge;
        private double MessageCost;
        private double NetworkCharge;
        private int DiscountRate;

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
            double charge = TalkingCharge * minute;
            return charge;
        }

        public double CalculateMessageCost(int quantity, Customer customer, Customer other)
        {
            double charge = MessageCost * quantity;
            return charge;
        }

        public double CalculateNetworkCost(double amount)
        {
            return NetworkCharge * amount;
        }

        public int GetID()
        {
            return ID;
        }

        public int GetDiscountRate()
        {
            return DiscountRate;
        }
    }
}
