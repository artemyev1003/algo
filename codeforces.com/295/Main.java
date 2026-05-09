import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        Reader reader = new Reader();
        int n = reader.nextInt();
        int m = reader.nextInt();
        int k = reader.nextInt();
        long[] a = new long[n];
        long[] operationsDiff = new long[m + 2];
        long[] operationsSum = new long[m + 2];
        long[] arrayDiff = new long[n + 2];
        long[] arraySum = new long[n + 2];
        Map<Integer, int[]> operations = new HashMap<>();

        for (int i = 0; i < n; i++) {
            a[i] = reader.nextInt();
        }

        for (int i = 1; i <= m; i++) {
            int[] operation = new int[3];
            for (int j = 0; j < 3; j++) {
                operation[j] = reader.nextInt();
            }
            operations.put(i, operation);
        }

        for (int i = 1; i <= k; i++) {
            int x = reader.nextInt();
            int y = reader.nextInt();
            operationsDiff[x]++;
            operationsDiff[y + 1]--;
        }

        for (int i = 1; i <= m; i++) {
            operationsSum[i] = operationsSum[i - 1] + operationsDiff[i];
        }

        for (int i = 1; i <= m; i++) {
            if (operationsSum[i] > 0) {
                int[] currentOperation = operations.get(i);
                int l = currentOperation[0];
                int r = currentOperation[1];
                int d = currentOperation[2];
                long diff = d * operationsSum[i];
                arrayDiff[l] += diff;
                arrayDiff[r + 1] += diff * (-1);
            }
        }

        for (int i = 1; i <= n; i++) {
            arraySum[i] = arraySum[i - 1] + arrayDiff[i];
            a[i - 1] += arraySum[i];
        }

        for (long num: a) {
            System.out.print(num + " ");
        }
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
