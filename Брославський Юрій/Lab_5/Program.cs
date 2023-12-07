using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

public class CreditCard
{
    public string Client { get; set; }
    public string AccountNumber { get; set; }
    public float CreditLimit { get; set; }
    public int GracePeriod { get; set; }

    private string _cvv;

    public string Cvv
    {
        get { return Decrypt(_cvv); }
        set { _cvv = Encrypt(value); }
    }

    public Dictionary<string, object> GiveDetails()
    {
        return new Dictionary<string, object>
        {
            { "client", Client },
            { "account_number", AccountNumber },
            { "credit_limit", CreditLimit },
            { "grace_period", GracePeriod },
            { "cvv", Cvv }
        };
    }

    private string Encrypt(string value)
    {
        using (SHA256 sha256 = SHA256.Create())
        {
            byte[] hashedBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(value));
            return BitConverter.ToString(hashedBytes).Replace("-", "").ToLower();
        }
    }

    private string Decrypt(string value)
    {
        return value;
    }
}

public class GoldenCreditCard : CreditCard
{
    public GoldenCreditCard(CreditCard baseCard) : base()
    {
        this.Client = baseCard.Client;
        this.AccountNumber = baseCard.AccountNumber;
        this.CreditLimit = baseCard.CreditLimit * 1.5f;
        this.GracePeriod = baseCard.GracePeriod;
        this.Cvv = baseCard.Cvv;
    }
}

public class BankInfo
{
    public string BankName { get; set; }
    public string HolderName { get; set; }
    public List<string> AccountsNumber { get; set; }
    public Dictionary<string, object> CreditHistory { get; set; }

    public List<string> TransactionList(string accountNumber)
    {
        return new List<string> { "Transaction 1", "Transaction 2" };
    }
}

public class BankCustomer
{
    public PersonalInfo PersonalInfo { get; set; }
    public BankInfo BankDetails { get; set; }

    public Dictionary<string, object> GiveDetails()
    {
        var personalInfoDetails = new Dictionary<string, object>
        {
            { "name", PersonalInfo.Name },
            { "age", PersonalInfo.Age },
        };

        var bankDetails = new Dictionary<string, object>
        {
            { "bank_name", BankDetails.BankName },
            { "holder_name", BankDetails.HolderName },
            { "accounts_number", BankDetails.AccountsNumber },
            { "credit_history", BankDetails.CreditHistory },
            { "transaction_list", BankDetails.TransactionList(PersonalInfo.AccountNumber) }
        };

        var result = new Dictionary<string, object>
        {
            { "personal_info", personalInfoDetails },
            { "bank_details", bankDetails }
        };

        return result;
    }
}

public class IndividualCustomer : BankCustomer
{
    public IndividualCustomer(BankCustomer baseCustomer) : base()
    {
        this.PersonalInfo = baseCustomer.PersonalInfo;
        this.BankDetails = baseCustomer.BankDetails;
    }
}

public class PersonalInfo
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string AccountNumber { get; set; }
}

class Program
{
    static void Main()
    {
        CreditCard baseCreditCard = new CreditCard
        {
            Client = "John Doe",
            AccountNumber = "1234567890123456",
            CreditLimit = 5000,
            GracePeriod = 30,
            Cvv = "123"
        };

        GoldenCreditCard goldenCreditCard = new GoldenCreditCard(baseCreditCard);

        BankCustomer baseBankCustomer = new BankCustomer
        {
            PersonalInfo = new PersonalInfo
            {
                Name = "John Doe",
                Age = 30,
                AccountNumber = "1234567890123456"
            },
            BankDetails = new BankInfo
            {
                BankName = "ABC Bank",
                HolderName = "John Doe",
                AccountsNumber = new List<string> { "1234567890123456" },
                CreditHistory = new Dictionary<string, object>()
            }
        };

        IndividualCustomer individualCustomer = new IndividualCustomer(baseBankCustomer);

        DisplayDetails(baseCreditCard, goldenCreditCard, baseBankCustomer, individualCustomer);
    }

    static void DisplayDetails(CreditCard baseCard, CreditCard decoratedCard, BankCustomer baseCustomer, BankCustomer decoratedCustomer)
    {
        Console.WriteLine("Base CreditCard Details:");
        DisplayCardDetails(baseCard);

        Console.WriteLine("\nGolden CreditCard Details:");
        DisplayCardDetails(decoratedCard);

        Console.WriteLine("\nBase BankCustomer Details:");
        DisplayCustomerDetails(baseCustomer);

        Console.WriteLine("\nIndividual Customer Details:");
        DisplayCustomerDetails(decoratedCustomer);
    }

    static void DisplayCardDetails(CreditCard card)
    {
        var details = card.GiveDetails();
        foreach (var entry in details)
        {
            Console.WriteLine($"{entry.Key}: {entry.Value}");
        }
    }

    static void DisplayCustomerDetails(BankCustomer customer)
    {
        var details = customer.GiveDetails();
        foreach (var entry in details)
        {
            Console.WriteLine($"{entry.Key}: {entry.Value}");
        }
    }
}
