namespace Lab_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int N = 5;
            int M = 3;

            Customer[] customers = new Customer[N];
            Operator[] operators = new Operator[M];
            Bill[] bills = new Bill[N];

            operators[0] = new Operator(0, 0.1, 0.02, 0.05, 10);
            operators[1] = new Operator(1, 0.12, 0.03, 0.06, 8);
            operators[2] = new Operator(2, 0.11, 0.025, 0.055, 12);

            customers[0] = new Customer(0, "Alice", 25, operators, bills, 100);
            customers[1] = new Customer(1, "Bob", 18, operators, bills, 120);
            customers[2] = new Customer(2, "Charlie", 30, operators, bills, 80);

            customers[0].Talk(30, customers[1]);
            customers[1].Message(50, customers[2]);
            customers[2].Connection(200);
            customers[2].ChangeOperator(operators[1]);
            customers[0].ChangeBillLimit(250);

            foreach (Customer customer in customers)
            {
                if (customer != null)
                {
                    Console.WriteLine($"{customer.GetName()}'s Bill: {(customer.GetBill()?.GetCurrentDebt() ?? 0):C}");
                }
            }
        }
    }
}