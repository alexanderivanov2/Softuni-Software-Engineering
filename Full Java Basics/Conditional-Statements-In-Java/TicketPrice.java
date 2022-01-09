import java.util.Scanner;

public class TicketPrice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String ticketType = scanner.nextLine();
        if (ticketType.equals("student"))
            System.out.println("$1.00");
        else if (ticketType.equals("regular"))
            System.out.println("$1.60");
        else
            System.out.println("Invalid ticket type!");
    }
}
