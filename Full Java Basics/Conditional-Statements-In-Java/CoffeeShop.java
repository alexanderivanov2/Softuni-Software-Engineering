import java.util.Scanner;

public class CoffeeShop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String drinkType = sc.nextLine();
        String extra = sc.nextLine();
        double price = 0;
        if (drinkType.equals("coffee"))
            price += 1;
        else if (drinkType.equals("tea"))
            price += 0.60;
        if (extra.equals("sugar"))
            price += 0.40;
        System.out.printf("Final price: $%.2f", price);
    }
}
