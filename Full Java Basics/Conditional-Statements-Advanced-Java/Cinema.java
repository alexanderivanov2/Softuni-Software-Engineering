import java.util.Scanner;

public class Cinema {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String movieType = sc.nextLine();
        int rows = sc.nextInt();
        int seatsPerRow = sc.nextInt();
        int seats = rows * seatsPerRow;
        double cost = 0;
        switch(movieType){
            case "Premiere":
                cost = seats * 12;
                break;
            case "Normal":
                cost = seats * 7.50;
                break;
            default:
                cost = seats * 5;
                break;
        }
        System.out.printf("%.2f", cost);
    }
}
