package source.domain;

public class Operator {
    private int ID;
    private double talkingCharge;
    private double messageCost;
    private double networkCharge;
    private int discountRate;

    public Operator(int ID, double talkingCharge, double messageCost, double networkCharge, int discountRate) {
        this.ID = ID;
        this.talkingCharge = talkingCharge;
        this.messageCost = messageCost;
        this.networkCharge = networkCharge;
        this.discountRate = discountRate;
    }

    public double calcTalkingCost(int minutes, Customer customer) {
        if(customer.getAge() < 18 || customer.getAge() > 65){
            return minutes * 2;
        }
        else
            return minutes * 2 * discountRate;
    }

    public double calcMessageCost(int quantity, Customer customer, Customer other) {
        if(customer.getOperator() == other.getOperator()){
            return quantity * 2;
        }
        else
            return quantity * 2 * discountRate;
    }

    public double calcNetworkCost(double amount) {
        return amount * networkCharge;
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public double getTalkingCharge() {
        return talkingCharge;
    }

    public void setTalkingCharge(double talkingCharge) {
        this.talkingCharge = talkingCharge;
    }

    public double getMessageCost() {
        return messageCost;
    }

    public void setMessageCost(double messageCost) {
        this.messageCost = messageCost;
    }

    public double getNetworkCharge() {
        return networkCharge;
    }

    public void setNetworkCharge(double networkCharge) {
        this.networkCharge = networkCharge;
    }

    public int getDiscountRate() {
        return discountRate;
    }

    public void setDiscountRate(int discountRate) {
        this.discountRate = discountRate;
    }

}
