class Solution {
    public static int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int w = board.length;
        int h = board[0].length;
        int[][] diff = new int[w + 1][h + 1];

        for (int[] s: skill) {
            int degree = s[0] == 1 ? s[5] * (-1) : s[5];
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];

            diff[r1][c1] += degree;
            diff[r1][c2 + 1] -= degree;
            diff[r2 + 1][c1] -= degree;
            diff[r2 + 1][c2 + 1] += degree;
        }

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                diff[i][j + 1] = diff[i][j] + diff[i][j + 1];
            }
        }

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                diff[i + 1][j] = diff[i][j] + diff[i + 1][j];
                if (board[i][j] + diff[i][j] > 0) {
                    answer++;
                }
            }
        }
        return answer;
    }
}
