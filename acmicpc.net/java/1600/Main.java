import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    private static int k;
    private static int w;
    private static int h;
    private static Long result = Long.MAX_VALUE;
    private static boolean[][][] visited;
    private static int[][] map;
    
    private static int[] dx = {2, 1, -1, -2, -2, -1, 1, 2, 1, 0, -1, 0};
    private static int[] dy = {1, 2, 2, 1, -1, -2, -2, -1, 0, 1, 0, -1};
    private static int[] cost = {1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0};


    public static void main(String[] args) {
        Reader reader = new Reader();
        k = reader.nextInt();
        w = reader.nextInt();
        h = reader.nextInt();

        if (w == 1 && h == 1) {
            System.out.println(0);
            return;
        }

        Deque<int[]> queue = new ArrayDeque<>();

        map = new int[h + 4][w + 4];
        visited = new boolean[h][w][k + 1];
        visited[0][0][k] = true;

        int[] border = new int[w + 4];
        Arrays.fill(border, 1);
        int[] borderIndices = {0, 1, h + 2, h + 3};
        for (int i: borderIndices) {
            map[i] = border;
        }

        for (int i = 2; i < h + 2; i++) {
            map[i][0] = 1;
            map[i][1] = 1;
            for (int j = 2; j < w + 2; j++) {
                map[i][j] = reader.nextInt();
            }
            map[i][w + 2] = 1;
            map[i][w + 3] = 1;
        }

        queue.addLast(new int[] {2, 2, k, 0}); 
        while (!queue.isEmpty()) {
            int[] nextElem = queue.poll();
            int x = nextElem[0]; 
            int y = nextElem[1]; 
            int remainingJumps = nextElem[2]; 
            int moveCount = nextElem[3]; 

            if (moveCount == result) {
                return;
            }

            int startWith = remainingJumps > 0 ? 0 : 8;

            for (int i = startWith; i < 12; i++) {
                int newX = x + dx[i];
                int newY = y + dy[i];
                int newJumpCount = remainingJumps - cost[i];
                if (map[newX][newY] != 1 && !visited[newX - 2][newY - 2][newJumpCount]) {
                    if (newX - 1 == h  && newY - 1 == w) {
                        result = Math.min(result, moveCount + 1);
                        System.out.println(result);
                        return;
                    }

                    visited[newX - 2][newY - 2][newJumpCount] = true;
                    queue.add(new int[] {newX, newY, newJumpCount, moveCount + 1}); 
                }
            }

        }

        
        result = result == Long.MAX_VALUE ? -1 : result;
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

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
