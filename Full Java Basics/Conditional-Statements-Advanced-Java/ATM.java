import java.util.Scanner;

public class ATM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double balance = sc.nextDouble();
        double withdraw = sc.nextDouble();
        double limit = sc.nextDouble();
        if (balance >= withdraw && withdraw <= limit)
            System.out.println("The withdraw was successful.");
        else if (balance >= withdraw && withdraw > limit)
            System.out.println("The limit was exceeded.");
        else
            System.out.println("Insufficient availability.");
    }
}
