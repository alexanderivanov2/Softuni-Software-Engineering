import java.util.Scanner;

public class GreaterNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOne = scanner.nextInt();
        int numberTwo = scanner.nextInt();
        if (numberOne > numberTwo)
            System.out.println("Greater number: " + numberOne);
        else
            System.out.println("Greater number: " + numberTwo);
    }
}
