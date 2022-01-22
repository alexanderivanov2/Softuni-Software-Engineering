import java.util.Scanner;

public class BiggestOfFiveNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int n4 = sc.nextInt();
        int n5 = sc.nextInt();
        int num = 0;
        if (n1 >= n2 && n1 >= n3 && n1 >= n4 && n1 >= n5)
            num = n1;
        else if (n2 >= n1 && n2 >= n3 && n2 >= n4 && n2 >= n5)
            num = n2;
        else if (n3 >= n1 && n3 >= n2 && n3 >= n4 && n3 >= n5)
            num = n3;
        else if (n4 >= n1 && n4 >= n2 && n4 >= n3 && n4 >= n5)
            num = n4;
        else
            num = n5;
        System.out.println(num);
    }
}
