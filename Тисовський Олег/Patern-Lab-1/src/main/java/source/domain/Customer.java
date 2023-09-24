package source.domain;

public class Customer {

    private int ID;
    private String name;
    private int age;
    private Operator operator;
    private Bill bill;

    public Customer(int ID, String name, int age, Operator operator, Bill bill) {
        this.ID = ID;
        this.name = name;
        this.age = age;
        this.operator = operator;
        this.bill = bill;
    }

    public void talk(int minutes, Customer other) {
        if(this.getBill().check(this.getBill().getCurrentDebt())) {
            this.getBill().add(this.getOperator().calcTalkingCost(minutes, this));
            System.out.println("-" + this.name + " is talking to " + other.name + " for " + minutes + " minutes");
        }
        else
            System.out.println("!-Error-!");
    }

    public void message(int quantity, Customer other) {
        if(this.getBill().check(this.getBill().getCurrentDebt())) {
            this.getBill().add(this.getOperator().calcMessageCost(quantity, this, other));
            System.out.println("-" + this.name + " sent to " + other.name + " " + quantity + " messages");
        }
        else
            System.out.println("!-Error-!");
    }

    public void connection(double amount) {
        if(this.getBill().check(this.getBill().getCurrentDebt())) {
            this.getBill().add(this.getOperator().calcNetworkCost(amount));
            System.out.println("-" + this.name + " connected to internet with " + amount + " MB");
        }
        else
            System.out.println("!-Error-!");
    }

    public int getID() {
        return ID;
    }

    public void setID(int ID) {
        this.ID = ID;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Operator getOperator() {
        return operator;
    }

    public void setOperator(Operator operator) {
        this.operator = operator;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

    @Override
    public String toString() {
        return "Customer{" +
                "ID=" + ID +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", operator=" + operator +
                ", bill=" + bill +
                '}';
    }
}
