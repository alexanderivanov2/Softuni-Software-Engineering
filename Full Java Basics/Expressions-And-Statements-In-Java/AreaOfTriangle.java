import java.util.Scanner;

public class AreaOfTriangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double sideA = Double.parseDouble(scanner.nextLine());
        double heightA = Double.parseDouble(scanner.nextLine());
        double area = sideA * heightA / 2;
        System.out.printf("%.2f", area);
    }
}
