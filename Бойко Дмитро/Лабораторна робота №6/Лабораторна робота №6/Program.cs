using System;
using System.Text;

// Facade Pattern

// Subsystem 1
public class ShoppingCart
{
    public void AddItem() => Console.WriteLine("Додавання товару до кошика");
    public void UpdateAmount() => Console.WriteLine("Оновлення кількості товару в кошику");
    public void Checkout() => Console.WriteLine("Виписка з кошика");
}

// Subsystem 2
public class Stock
{
    public void SelectStockItem() => Console.WriteLine("Вибір товару зі складу");
    public void UpdateStock() => Console.WriteLine("Оновлення запасів");
}

// Subsystem 3
public class Shipment
{
    public void CreateShipment() => Console.WriteLine("Створення відправлення");
    public void AddProvider() => Console.WriteLine("Додавання постачальника доставки");
    public void ModifyProvider() => Console.WriteLine("Зміна постачальника доставки");
}

// Subsystem 4
public class Payment
{
    public void AddCardDetails() => Console.WriteLine("Додавання реквізитів картки для оплати");
    public void VerifyPayment() => Console.WriteLine("Перевірка платежу");
}

// Facade
public class OrderFacade
{
    private ShoppingCart shoppingCart = new ShoppingCart();
    private Stock stock = new Stock();
    private Shipment shipment = new Shipment();
    private Payment payment = new Payment();

    public void DoOperation()
    {
        shoppingCart.AddItem();
        shoppingCart.UpdateAmount();
        shoppingCart.Checkout();

        stock.SelectStockItem();
        stock.UpdateStock();

        shipment.CreateShipment();
        shipment.AddProvider();
        shipment.ModifyProvider();

        payment.AddCardDetails();
        payment.VerifyPayment();
    }
}

// Bridge Pattern

// Implementor
interface IDevice
{
    void Start();
    void Stop();
}

// ConcreteImplementor
class Appliance : IDevice
{
    public void Start() => Console.WriteLine("Пристрій запущено");
    public void Stop() => Console.WriteLine("Прилад зупинився");
}

// Abstraction
abstract class Switch
{
    protected IDevice device;

    public void SetDevice(IDevice device) => this.device = device;

    public abstract void TurnOn();
    public abstract void TurnOff();
}

// RefinedAbstraction
class RemoteController : Switch
{
    public override void TurnOn() => device.Start();
    public override void TurnOff() => device.Stop();
}

class Program
{
    static void Main()
    {
        Console.OutputEncoding = Encoding.UTF8;
        // Using Facade Pattern
        OrderFacade orderFacade = new OrderFacade();
        orderFacade.DoOperation();

        Console.WriteLine("\n-------------------\n");

        // Using Bridge Pattern
        Appliance appliance = new Appliance();
        RemoteController remote = new RemoteController();
        remote.SetDevice(appliance);

        remote.TurnOn();
        remote.TurnOff();
    }
}
