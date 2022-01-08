import java.util.Scanner;

public class SpeedInfo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double speed = sc.nextDouble();
        if (speed <= 30)
            System.out.println("Slow");
        else
            System.out.println("Fast");
    }
}
