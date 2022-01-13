import java.util.Locale;
import java.util.Scanner;

public class VowelOrConsonant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char letter = sc.nextLine().charAt(0);
        switch (letter){
            case 'A':
            case 'a':
            case 'E':
            case 'e':
            case 'O':
            case 'o':
            case 'U':
            case 'u':
            case 'i':
            case 'I':
                System.out.println("Vowel");
                break;
            default:
                System.out.println("Consonant");
                break;
        }

    }
}
