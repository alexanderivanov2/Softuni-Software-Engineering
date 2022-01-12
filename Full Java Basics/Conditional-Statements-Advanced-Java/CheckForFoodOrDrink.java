import java.util.Scanner;

public class CheckForFoodOrDrink {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String check = sc.nextLine();
        if (check.equals("curry") || check.equals("noodles") || check.equals("sushi")
        || check.equals("spaghetti"))
            System.out.println("food");
        else if (check.equals("tea") || check.equals("water") || check.equals("coffee"))
            System.out.println("drink");
        else
            System.out.println("unknown");
    }
}
