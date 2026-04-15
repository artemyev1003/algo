
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.ArrayDeque;

class Main {
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Reader reader = new Reader();
        int t = reader.nextInt();
        for (int testCase = 0; testCase < t; testCase++) {
            int m = reader.nextInt();
            int n = reader.nextInt();
            int k = reader.nextInt();
            int[][] map = new int[m][n];
            boolean[][] visited = new boolean[m][n];
            Deque<int[]> queue = new ArrayDeque<>();
            int count = 0;

            for (int cabbage = 0; cabbage < k; cabbage++) {
                int x = reader.nextInt();
                int y = reader.nextInt();
                map[x][y] = 1;
            }

                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (map[i][j] == 1 && !visited[i][j]) {
                            queue.add(new int[] {i, j});
                            count++;
                            while (!queue.isEmpty()) {
                                int[] coords = queue.poll();
                                int currX = coords[0];
                                int currY = coords[1];
                                visited[currX][currY] = true;
                                for (int z = 0; z < 4; z++) {
                                    int newX = currX + dx[z];
                                    int newY = currY + dy[z];
                                    if (
                                            newX >= 0 
                                            && newX < m
                                            && newY >= 0
                                            && newY < n
                                            && map[newX][newY] == 1
                                            && !visited[newX][newY]
                                        ) {
                                            queue.addLast(new int[] {newX, newY});
                                        }
                                }
                            }
                        }
                    }
                }
            
            System.out.println(count);
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
