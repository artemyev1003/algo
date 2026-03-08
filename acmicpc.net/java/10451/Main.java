import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            scanner.nextLine();
            String permString = scanner.nextLine();
            int[] permIntArr = Arrays.stream(permString.split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println(solve(permIntArr, n)); 
        }
        scanner.close();
    }

    private static int solve(int[] perm, int n) {
        int count = 0;
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                continue;
            }
            int next = i;
            while (!visited[next]) {
                visited[next] = true;
                next = perm[next] - 1;
                if (visited[next]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
