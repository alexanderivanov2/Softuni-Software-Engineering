import java.util.Scanner;

public class CalculateSpeed {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double distance = Double.parseDouble(scanner.nextLine());
        double time = Double.parseDouble(scanner.nextLine());
        double speed = distance / time;
        System.out.printf("%.2f", speed);
    }
}
