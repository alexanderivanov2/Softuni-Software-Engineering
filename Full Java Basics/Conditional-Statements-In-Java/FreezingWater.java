import java.util.Scanner;

public class FreezingWater {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int celsius = scanner.nextInt();
        if (celsius <= 0){
            System.out.println("Freezing weather!");
        }
    }
}
