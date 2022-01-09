import java.util.Scanner;

public class AreaOfFigures {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String figure = sc.nextLine();
        double a = sc.nextDouble();
        double result = 0;
        if (figure.equals("square")){
            result = a * a;
        } else if (figure.equals("rectangle")) {
            double b = sc.nextDouble();
            result = a * b;
        } else if (figure.equals("circle")){
            result = Math.PI * Math.pow(a, 2);
        }
        System.out.printf("%.2f", result);
    }

}
