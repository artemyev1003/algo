import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
       Reader reader = new Reader(); 
       int n = reader.nextInt();
       int m = reader.nextInt();
       int c = reader.nextInt();

       int[] a = new int[n + 1];
       int[] aDiff = new int[n + 2];
       int[] aSums = new int[n + 2];
       int[] b = new int[m + 1];

       for (int i = 1; i <= n; i++) {
           a[i] = reader.nextInt();
       }

       for (int i = 1; i <= m; i++) {
           b[i] = reader.nextInt();
       }

       for (int i = 1; i <= m; i++) {
           aDiff[i] += b[i];
           aDiff[n - m + i + 1] -= b[i];
       }

       for (int i = 1; i <=n; i++) {
           aSums[i] = aSums[i - 1] + aDiff[i];
       }

       for (int i = 1; i <= n; i++) {
           a[i] = (a[i] + aSums[i]) % c;
           System.out.print(a[i] + " ");
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
