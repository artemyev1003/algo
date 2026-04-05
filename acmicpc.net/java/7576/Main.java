import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.ArrayDeque;

class Main {
    private static int m, n;
    private static int count = 0;
    private static boolean[][] visited;
    private static int[][] map;
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) {
        Reader reader = new Reader();
        n = reader.nextInt();
        m = reader.nextInt();
        Deque<int[]> queue = new ArrayDeque<>();
        map = new int[m][n];
        visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int num = reader.nextInt();
                map[i][j] = num;
                if (num == 1) {
                    visited[i][j] = true;
                    queue.addLast(new int[] {i, j, 0});
                } else if (num == 0) {
                    count++;
                }
            }
        }

        if (count == 0) {
            System.out.println(0);
            return;
        }
        
        while (!queue.isEmpty()) {
            int[] nextElement = queue.poll();
            int x = nextElement[0];
            int y = nextElement[1];
            int days = nextElement[2];

            for (int d = 0; d < 4; d++) {
                int newX = x + dx[d];
                int newY = y + dy[d];

                if (
                        newX >= 0 &&
                        newX < m &&
                        newY >= 0 &&
                        newY < n &&
                        !visited[newX][newY] &&
                        map[newX][newY] == 0
                    ) {
                        count--;
                        if (count == 0) {
                            System.out.println(days + 1);
                            return;
                    }
                    queue.addLast(new int[] {newX, newY, days + 1});
                    visited[newX][newY] = true;
                }
            }
        }
        System.out.println(-1);
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
