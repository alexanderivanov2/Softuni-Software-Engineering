import java.util.Scanner;

public class VacationExpenses {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String season = sc.nextLine();
        String accommodationType = sc.nextLine();
        int days = sc.nextInt();
        double expenses = 0;
        double discount = 0;
        switch (season){
            case "Spring":
                switch (accommodationType){
                    case "Hotel":
                        expenses = 30;
                        discount = 20;
                        break;
                    case "Camping":
                        expenses = 10;
                        discount = 20;
                    default:
                        break;
                }
                break;
            case "Summer":
                switch (accommodationType){
                    case "Hotel":
                        expenses = 50;
                        discount = 0;
                        break;
                    case "Camping":
                        expenses = 30;
                        discount = 0;
                        break;
                    default:
                        break;
                }
                break;
            case "Autumn":
                switch (accommodationType){
                    case "Hotel":
                        expenses = 20;
                        discount = 30;
                        break;
                    case "Camping":
                        expenses = 15;
                        discount = 30;
                        break;
                    default:
                        break;
                }
                break;
            case "Winter":
                switch (accommodationType){
                    case "Hotel":
                        expenses = 40;
                        discount = 10;
                        break;
                    case "Camping":
                        expenses = 10;
                        discount = 10;
                        break;
                    default:
                        break;
                }
                break;
            default:
                break;
        }
        expenses = expenses * days;
        if (discount > 0)
            expenses = expenses - (expenses * (discount / 100));
        System.out.printf("%.2f", expenses);
    }
}
