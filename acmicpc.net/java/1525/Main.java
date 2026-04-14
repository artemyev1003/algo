import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.List;
import java.util.ArrayDeque;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;

class Main {
    private static String finalString = "123456780";
    private static StringBuffer inputMapBuffer = new StringBuffer();
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Reader reader = new Reader();
        for (int i = 0; i < 9; i++) {
            inputMapBuffer.append(reader.next());
        }

        if (inputMapBuffer.toString().equals(finalString)) {
            System.out.println(0);
            return;
        }

        Deque<List<Object>> queue = new ArrayDeque<>();
        Map<String, Integer> visited = new HashMap<>();
        queue.addFirst(List.of(0, inputMapBuffer.toString()));
        
        while (!queue.isEmpty()) {
            List<Object> data = queue.poll();
            int count = (int) data.get(0);
            String currentString = (String) data.get(1);
            int indexOfZero = currentString.indexOf("0");
            int currentX = indexOfZero / 3;
            int currentY = indexOfZero % 3;
            for (int i = 0; i < 4; i++) {
                int newX = currentX + dx[i];
                int newY = currentY + dy[i];
                if (newX >= 0 && newX < 3 && newY >= 0 && newY < 3) {

                    int nearNumberIndex = newX * 3 + newY;
                    String nearNumber = String.valueOf(currentString.charAt(nearNumberIndex));

                    String newString = currentString.replace("0", "a");
                    newString = newString.replace(nearNumber, "0");
                    newString = newString.replace("a", nearNumber);

                    int newCount = count + 1;

                    if (newString.equals(finalString)) {
                        System.out.println(newCount);
                        return;
                    }

                    Set<String> visitedKeys = visited.keySet();
                    if (!visitedKeys.contains(newString) || visited.get(newString) > newCount) {
                        visited.put(newString, newCount);
                        queue.add(List.of(newCount, newString));
                    }
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
    }
}
