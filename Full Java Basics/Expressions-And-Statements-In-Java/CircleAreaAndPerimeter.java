import java.util.Scanner;
import static java.lang.Math.pow;

public class CircleAreaAndPerimeter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double radius = scanner.nextDouble();
        double area = Math.PI * pow(radius, 2);
        double perimeter = 2 * Math.PI * radius;
        System.out.printf("Area = %.2f\nPerimeter = %.2f", area, perimeter);
    }
}
