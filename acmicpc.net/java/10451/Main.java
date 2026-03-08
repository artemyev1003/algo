import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    private static int[] perm;
    private static boolean[] visited;
    public static void main(String[] args) {
        FastReader fastReader = new FastReader();
        int t = fastReader.nextInt();
        while (t-- > 0) {
            int n = fastReader.nextInt();
            perm = new int[n];
            for (int i = 0; i < n; i++) {
                perm[i] = fastReader.nextInt();
            }
            System.out.println(solve(perm, n)); 
        }
    }

    private static int solve(int[] perm, int n) {
        int count = 0;
        visited = new boolean[n];

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

    static class FastReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public FastReader() {
            reader = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (tokenizer == null || !tokenizer.hasMoreElements()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    return null;
                }
            }
            return tokenizer.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
