import java.util.Scanner;

public class FourOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double numOne = Double.parseDouble(scanner.nextLine());
        double numTwo = Double.parseDouble(scanner.nextLine());
        double sum = numOne + numTwo;
        double divide = numOne - numTwo;
        double multiply = numOne * numTwo;
        double division = numOne / numTwo;
        System.out.printf("%.2f + %.2f = %.2f\n", numOne, numTwo, sum);
        System.out.printf("%.2f - %.2f = %.2f\n", numOne, numTwo, divide);
        System.out.printf("%.2f * %.2f = %.2f\n", numOne, numTwo, multiply);
        System.out.printf("%.2f / %.2f = %.2f", numOne, numTwo, division);
    }
}
