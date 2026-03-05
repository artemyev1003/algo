import java.util.Scanner;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.IntStream;

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
        int[] indices = IntStream.rangeClosed(1, n).toArray();
        HashSet<Integer> visited = new HashSet<>();

        for (int i : indices) {
            int next = i;
            while (true) {
                if (visited.contains(next)) {
                    break;
                }

                visited.add(next);
                next = perm[next - 1];

                if (visited.contains(next)) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
