import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        FastReader fastReader = new FastReader();
        int n = fastReader.nextInt();
        int m = fastReader.nextInt();

        if (m == 0) {
            System.out.println(n);
            return;
        }
        
        Graph graph = new Graph(n);

        while (m-- > 0) {
            int u = fastReader.nextInt() - 1;
            int v = fastReader.nextInt() - 1;
            graph.addEdge(u, v);
        }
        System.out.println(graph.BFS());
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
    
    static class Graph {
        private int v;
        private LinkedList<Integer>[] adj;

        Graph(int v) {
            this.v = v;
            adj = new LinkedList[v];
            for (int i = 0; i < v; i++) {
                adj[i] = new LinkedList<>();
            }
        }

        void addEdge(int u, int v) {
            adj[u].add(v);
            adj[v].add(u);
        }

        int BFS() {
            int result = 0;
            boolean[] visited = new boolean[v];

            for (int i = 0; i < v; i++) {
                if (visited[i]) {
                    continue;
                }

                visited[i] = true;
                LinkedList<Integer> queue = new LinkedList<>();
                queue.add(i);
                result++;
                while (queue.size() != 0) {
                    int node = queue.poll();
                    for (int adjNode : adj[node]) {
                        if (!visited[adjNode]) {
                            visited[adjNode] = true;
                            queue.add(adjNode);
                        }
                    }
                }
            }
            return result;
        }
    }
}
