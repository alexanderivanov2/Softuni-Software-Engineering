import java.util.Scanner;

public class ProductOf3Numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n1 = sc.nextDouble();
        double n2 = sc.nextDouble();
        double n3 = sc.nextDouble();
        if (n1 == 0 || n2 == 0 || n3 == 0)
            System.out.println("zero");
        else {
            int negativeNumbersCount = 0;
            if (n1 < 0) negativeNumbersCount++;
            if (n2 < 0) negativeNumbersCount++;
            if (n3 < 0) negativeNumbersCount++;
            if (negativeNumbersCount % 2 == 0)
                System.out.println("positive");
            else
                System.out.println("negative");
        }
    }
}
