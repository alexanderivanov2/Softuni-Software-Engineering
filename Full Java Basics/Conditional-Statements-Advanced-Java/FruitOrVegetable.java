import java.util.Scanner;

public class FruitOrVegetable {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String txt = sc.nextLine();
        if (txt.equals("banana") || txt.equals("kiwi") || txt.equals("cherry")
        || txt.equals("lemon") || txt.equals("grapes") || txt.equals("apple"))
            System.out.println("fruit");
        else if (txt.equals("cucumber") || txt.equals("pepper") || txt.equals("carrot"))
            System.out.println("vegetable");
        else
            System.out.println("unknown");
    }
}
