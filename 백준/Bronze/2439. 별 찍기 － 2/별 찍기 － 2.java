import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = N; i > 0; i--) {
            String escape = " ".repeat(i - 1);  // i - 1개의 공백
            String star = "*".repeat(N - i + 1);  // (N - i + 1)개의 별
            System.out.println(escape + star);
        }
    }
}