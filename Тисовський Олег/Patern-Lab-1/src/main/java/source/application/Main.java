package source.application;
import source.domain.Bill;
import source.domain.Customer;
import source.domain.Operator;

public class Main {
    public static void main(String[] args) {

        Operator kyivstar = new Operator(0,1,1,1, 2);
        Operator vodafone = new Operator(1,2,2,2, 3);

        Bill b1 = new Bill(300,200);
        Bill b2 = new Bill(200,300);
        Bill b3 = new Bill(400,100);

        Customer c1 = new Customer(0, "Oleh", 30, kyivstar, b1);
        Customer c2 = new Customer(1, "Nazar", 70, kyivstar, b2);
        Customer c3 = new Customer(1, "Ivan", 32, vodafone, b3);

        c1.talk(10, c2);
        c1.message(2, c2);
        c1.connection(1000);

        int amount = 100;
        System.out.println("\n-"+ c1.getName() + " current dept is: " + c1.getBill().getCurrentDebt());
        System.out.println("-" + c1.getName() + " payed " + amount + " for his dept");
        c1.getBill().pay(amount);
        System.out.println("-"+ c1.getName() + " current dept is: " + c1.getBill().getCurrentDebt());

        int newBillLimit = 500;
        System.out.println("\n-"+ c1.getName() + " current bill limit is: " + c1.getBill().getLimitingAmount());
        System.out.println("-" + c1.getName() + " changed his bill limit to " + newBillLimit);
        c1.getBill().changeTheLimit(500);
        System.out.println("-"+ c1.getName() + " current bill limit is: " + c1.getBill().getLimitingAmount());

        int minutes = 25;
        int quanity = 10;
        System.out.println("\n-Cost of talking of " + c2.getName() + " for " + minutes + "min -> " + c2.getOperator().calcTalkingCost(25, c2));
        System.out.println("-Cost of talking of " + c1.getName() + " for " + minutes + "min -> " + c1.getOperator().calcTalkingCost(25, c1));
        System.out.println("\n-" + quanity + " messages from " + c1.getName() + " to " + c2.getName() + " costs -> " + c2.getOperator().calcMessageCost(10, c1, c2));
        System.out.println("-" + quanity + " messages from " + c2.getName() + " to " + c3.getName() + " costs -> " + c2.getOperator().calcMessageCost(10, c2, c3));

    }
}