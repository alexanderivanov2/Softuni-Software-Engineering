import java.util.Scanner;

public class DaysToMinutes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int day = scanner.nextInt();
        int minutes = day * 24 * 60;
        System.out.println(minutes);
    }
}
