import java.util.Scanner;

public class BoilingWater {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double waterTemperature = sc.nextDouble();
        if (waterTemperature > 100)
            System.out.println("The water is boiling");
        else
            System.out.println("The water is not hot enough");
    }
}
