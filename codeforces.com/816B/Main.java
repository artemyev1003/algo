import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        int curr = 0;
        int[] elements = new int[200_002];
        int[] elementsSum = new int[200_002];
        int[] elementsPass = new int[200_002];
        
        Reader reader = new Reader();
        int n = reader.nextInt();
        int k = reader.nextInt();
        int q = reader.nextInt();

        for (int i = 0; i < n; i++) {
            int l = reader.nextInt();
            int r = reader.nextInt();
            elements[l]++;
            elements[r + 1]--;
        }

        for (int i = 1; i <= 200_001; i++) {
            elementsSum[i] = elementsSum[i - 1] + elements[i];
            if (elementsSum[i] >= k) {
                curr++;
            }
                elementsPass[i] = curr;
        }

        for (int i = 0; i < q; i++) {
            int a = reader.nextInt();
            int b = reader.nextInt();
            int result = elementsPass[b] - elementsPass[a - 1];
            result = result > 0 ? result : 0;
            System.out.println(result);
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
