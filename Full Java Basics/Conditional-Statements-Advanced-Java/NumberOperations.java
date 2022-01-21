import java.util.Scanner;

public class NumberOperations {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n1 = Double.parseDouble(sc.nextLine());
        double n2 = Double.parseDouble(sc.nextLine());
        String operation = sc.nextLine();
        double result = 0;
        switch (operation){
            case "+":
                result = n1 + n2;
                break;
            case "-":
                result = n1 - n2;
                break;
            case "*":
                result = n1 * n2;
                break;
            case "/":
                result = n1 / n2;
                break;
            case "%":
                result = n1 % n2;
                break;
            default:
                break;
        }
        System.out.printf("%.0f %s %.0f = %.2f", n1, operation, n2, result);
    }
}
