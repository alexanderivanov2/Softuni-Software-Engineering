import java.util.Scanner;

public class PersonInfo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String firstName = scanner.nextLine();
        String lastName = scanner.nextLine();
        String country = scanner.nextLine();
        String town = scanner.nextLine();
        System.out.printf("%s %s from %s - %s!", firstName, lastName, country, town);
    }
}
