using Microsoft.VisualStudio.TestTools.UnitTesting;
using Лабораторна_робота__2;

[TestClass]
public class ShipTests
{
    [TestMethod]
    public void TestSailTo_ValidDestination_ReturnsTrue()
    {
        Port currentPort = new Port(1, 0, 0);
        Port destinationPort = new Port(2, 1, 1);
        Ship ship = new Ship(1, 100, currentPort, 5000, 10, 5, 3, 2, 0.2);

        bool result = ship.SailTo(destinationPort);

        Assert.IsTrue(result);
        Assert.AreEqual(destinationPort, ship.CurrentPort);
    }

    [TestMethod]
    public void TestSailTo_InsufficientFuel_ReturnsFalse()
    {
        Port currentPort = new Port(1, 0, 0);
        Port destinationPort = new Port(2, 1, 1);
        Ship ship = new Ship(1, 10, currentPort, 5000, 10, 5, 3, 2, 0.2);

        bool result = ship.SailTo(destinationPort);

        Assert.IsFalse(result);
        Assert.AreEqual(currentPort, ship.CurrentPort);
    }

    [TestMethod]
    public void TestRefuel_IncreasesFuelLevel()
    {
        Ship ship = new Ship(1, 100, new Port(1, 0, 0), 5000, 10, 5, 3, 2, 0.2);

        ship.Refuel(50);

        Assert.AreEqual(150, ship.Fuel);
    }
}
