package source.domain;

public class Bill {
    private double limitingAmount;
    private double currentDebt;

    public Bill(double limitingAmount, double currentDebt) {
        this.limitingAmount = limitingAmount;
        this.currentDebt = currentDebt;
    }

    public boolean check(double amount) {
        if(amount > limitingAmount)
            return false;
        else
            return true;
    }

    public void add(double amount) {
        this.currentDebt += amount;
    }

    public void pay(double amount) {
        this.currentDebt -= amount;
    }

    public void changeTheLimit(double newAmount) {
        this.limitingAmount = newAmount;
    }

    public double getLimitingAmount() {
        return limitingAmount;
    }

    public double getCurrentDebt() {
        return currentDebt;
    }

    public void setCurrentDebt(double currentDebt) {
        this.currentDebt = currentDebt;
    }

}
