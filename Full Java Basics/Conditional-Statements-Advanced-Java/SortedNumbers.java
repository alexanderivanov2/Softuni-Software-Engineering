import java.util.Scanner;

public class SortedNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n1 = sc.nextDouble();
        double n2 = sc.nextDouble();
        double n3 = sc.nextDouble();
        if (n1 < n2 && n2 < n3)
            System.out.println("Ascending");
        else if (n1 > n2 && n2 > n3)
            System.out.println("Descending");
        else
            System.out.println("Not sorted");
    }
}
