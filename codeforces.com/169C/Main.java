import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        Reader reader = new Reader();
        long result = 0;
        int n = reader.nextInt();
        int q = reader.nextInt();
        long[] elements = new long[n + 1];
        long[] queries = new long[n + 2];
        long[] queriesSum = new long[n + 2];

        for (int i = 1; i <= n; i++) {
            elements[i] = reader.nextInt();
        }

        for (int i = 0; i < q; i++) {
            int l = reader.nextInt();
            int r = reader.nextInt();
            queries[l] += 1;
            queries[r + 1] -= 1;
        }

        for (int i = 1; i <= n + 1; i++) {
            queriesSum[i] = queriesSum[i - 1] + queries[i];
        }
        Arrays.sort(elements);
        Arrays.sort(queriesSum);

        for (int i = 1; i <= n; i++) {
            result += elements[i] * queriesSum[i + 1];
        }

        System.out.println(result);

    }

    static class Reader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public Reader() {
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

        Integer nextInt() {
            return Integer.valueOf(next());
        }
    }
}
