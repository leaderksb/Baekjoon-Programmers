import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int x = Integer.parseInt(br.readLine());
        int y = Integer.parseInt(br.readLine());

        if (x > 0 && y > 0) {  // 1사분면 (+, +)
            System.out.println("1");
        } else if (x < 0 && y > 0) {  // 2사분면 (-, +)
            System.out.println("2");
        } else if (x < 0 && y < 0) {  // 3사분면 (-, -)
            System.out.println("3");
        } else if (x > 0 && y < 0) {  // 4사분면 (+, -)
            System.out.println("4");
        }
    }
}