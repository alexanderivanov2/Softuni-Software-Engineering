import java.util.Scanner;

public class ValidTriangle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        boolean valid = true;
        if (a+b < c)
            valid = false;
        else if (b + c < a)
            valid = false;
        else if (c+a < b)
            valid = false;

        if (valid)
            System.out.println("Valid Triangle");
        else
            System.out.println("Invalid Triangle");
    }
}
