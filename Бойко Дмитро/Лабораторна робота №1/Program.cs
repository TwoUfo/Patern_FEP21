using System.Text;

namespace Lab_1
{
    class MainClass
    {
        private static int currentCustomerId = 2;  // Поточний ID для нових клієнтів

        public static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;
            int N = 5;
            int M = 3;

            Customer[] customers = new Customer[N];
            Operator[] operators = new Operator[M];
            Bill[] bills = new Bill[N];

            for (int i = 0; i < N; i++)
            {
                bills[i] = null;
            }

            for (int i = 0; i < M; i++)
            {
                operators[i] = null;
            }

            if (N > 0)
            {
                customers[0] = new Customer(1, "Customer1", 25, null, null, 1000.0);
                bills[0] = new Bill(1000.0);
                customers[0].Bills = new Bill[] { bills[0] };

                customers[1] = new Customer(2, "Customer2", 30, null, null, 1000.0);
                bills[1] = new Bill(1000.0);
                customers[1].Bills = new Bill[] { bills[1] };
            }

            if (M > 0)
            {
                operators[0] = new Operator(100, 20, 30, 0.3, 1);
                customers[0].Operators = new Operator[] { operators[0] };
                customers[1].Operators = new Operator[] { operators[0] };
            }

            while (true)
            {
                Console.WriteLine("Проведення всіх можливих дій:");

                Console.WriteLine("Дія 1: Створення клієнта");
                CreateCustomer(customers, ref currentCustomerId);

                Console.WriteLine("Дія 2: Створення оператора");
                CreateOperator(operators, ref currentCustomerId);

                Console.WriteLine("Дія 3: Клієнт розмовляє з іншим клієнтом");
                TalkWithAnotherCustomer(customers);

                Console.WriteLine("Дія 4: Клієнт надсилає повідомлення");
                SendMessages(customers);

                Console.WriteLine("Дія 5: Клієнт використовує мережу");
                UseNetwork(customers);

                Console.WriteLine("Дія 6: Клієнт сплачує рахунок");
                PayBill(customers);

                Console.WriteLine("Дія 7: Змінити оператора для клієнта");
                ChangeOperatorForCustomer(customers, operators);

                Console.WriteLine("Дія 8: Змінити ліміт рахунку для клієнта");
                ChangeBillLimitForCustomer(customers);

                Console.WriteLine("Дія 9: Вихід");
                break;
            }
        }

        private static void CreateCustomer(Customer[] customers, ref int currentCustomerId)
        {
            string customerName = $"Customer{currentCustomerId}";
            int customerAge = currentCustomerId * 5;
            double customerLimit = currentCustomerId * 1000;

            currentCustomerId++;
            customers[currentCustomerId - 1] = new Customer(currentCustomerId, customerName, customerAge, null, null, customerLimit);
            Console.WriteLine($"Клієнт {currentCustomerId} створений.");
            Console.WriteLine($"ID: {currentCustomerId}, Ліміт: {customerLimit}");
        }

        private static void CreateOperator(Operator[] operators, ref int currentCustomerId)
        {
            double talkingCharge = currentCustomerId * 0.1;
            double messageCost = currentCustomerId * 0.05;
            double networkCharge = currentCustomerId * 0.02;
            int discountRate = currentCustomerId;

            operators[currentCustomerId - 1] = new Operator(currentCustomerId, talkingCharge, messageCost, networkCharge, discountRate);
            Console.WriteLine($"Оператор {currentCustomerId} створений.");
            Console.WriteLine($"ID: {currentCustomerId}");
        }

        private static void TalkWithAnotherCustomer(Customer[] customers)
        {
            customers[0].Talk(10, customers[1]);
            Console.WriteLine("Клієнт розмовляє з іншим клієнтом.");
            Console.WriteLine($"Залишок грошей клієнта {customers[0].ID}: {customers[0].GetRemainingAmount()}");
        }

        private static void SendMessages(Customer[] customers)
        {
            customers[0].Message(5, customers[1]);
            Console.WriteLine("Клієнт надсилає повідомлення.");
            Console.WriteLine($"Залишок грошей клієнта {customers[0].ID}: {customers[0].GetRemainingAmount()}");
        }

        private static void UseNetwork(Customer[] customers)
        {
            customers[0].Connection(100);
            Console.WriteLine("Клієнт використовує мережу.");
            Console.WriteLine($"Залишок грошей клієнта {customers[0].ID}: {customers[0].GetRemainingAmount()}");
        }

        private static void PayBill(Customer[] customers)
        {
            customers[0].PayBill(500);
            Console.WriteLine("Клієнт сплатив рахунок.");
            Console.WriteLine($"Залишок грошей клієнта {customers[0].ID}: {customers[0].GetRemainingAmount()}");
        }


        private static void ChangeOperatorForCustomer(Customer[] customers, Operator[] operators)
        {
            // Вибираємо клієнта для зміни оператора (наприклад, перший клієнт)
            Customer selectedCustomer = customers[0];

            // Перевіряємо, чи є вибраний клієнт та чи є оператор для зміни
            if (selectedCustomer != null && operators.Length > 0)
            {
                selectedCustomer.ChangeOperator(operators[0]); // Зміна оператора для вибраного клієнта
                Console.WriteLine($"Клієнт {selectedCustomer.Name} тепер має нового оператора.");
            }
            else
            {
                Console.WriteLine("Неможливо змінити оператора. Невірні вхідні дані.");
            }
        }

        private static void ChangeBillLimitForCustomer(Customer[] customers)
        {
            // Вибираємо клієнта для зміни ліміту рахунку (наприклад, перший клієнт)
            Customer selectedCustomer = customers[0];

            // Перевіряємо, чи є вибраний клієнт та чи є рахунок для зміни ліміту
            if (selectedCustomer != null && selectedCustomer.Bills.Length > 0)
            {
                double newLimit = 3000; // Новий ліміт рахунку (можна замінити на потрібне значення)
                selectedCustomer.ChangeBillLimit(newLimit); // Зміна ліміту рахунку для вибраного клієнта
                Console.WriteLine($"Клієнт {selectedCustomer.Name} тепер має новий ліміт рахунку: {newLimit}.");
            }
            else
            {
                Console.WriteLine("Неможливо змінити ліміт рахунку. Немає рахунку або невірні вхідні дані.");
            }
        }
    }
}