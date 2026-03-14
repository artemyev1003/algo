import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main {

    static int n;
    static int[][] map;
    static boolean[] visited;
    static long bestResult = Long.MAX_VALUE;

    public static void main(String[] args) {
        FastReader fastReader = new FastReader();
        n = fastReader.nextInt();
        map = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = fastReader.nextInt();
            } 
        }
        visited[0] = true;
        dfs(0, 0, 1, 0);
        System.out.println(bestResult);
    }

    private static void dfs(int startNode, int currNode, int count, int currResult) {
        if (count == n) {
            if (map[currNode][startNode] != 0) {
                bestResult = Math.min(bestResult, currResult + map[currNode][startNode]);
            }
            return;
        } 

        for (int i = 0; i < n; i++) {
            if (!visited[i] && map[currNode][i] != 0) {
                if (currResult + map[currNode][i] < bestResult) {
                    visited[i] = true;
                    dfs(startNode, i, count + 1, currResult + map[currNode][i]);
                    visited[i] = false;
                }
            }
        }
    }

    static class FastReader {
        BufferedReader reader;
        StringTokenizer tokenizer;
        
        FastReader() {
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
