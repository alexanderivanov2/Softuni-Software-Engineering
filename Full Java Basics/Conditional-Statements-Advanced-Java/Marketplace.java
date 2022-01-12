import java.util.Scanner;

public class Marketplace {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String product = sc.nextLine();
        String day = sc.nextLine();
        double price = 0;
        if (product.equals("Banana")) {
            if (day.equals("Weekday"))
                price += 2.50;
            else
                price += 2.70;
        } else if (product.equals("Apple")){
            if (day.equals("Weekday"))
                price += 1.30;
            else
                price += 1.60;
        } else if (product.equals("Kiwi")){
            if (day.equals("Weekday"))
                price += 2.20;
            else
                price += 3.00;
        }
        System.out.printf("%.2f", price);
    }
}
