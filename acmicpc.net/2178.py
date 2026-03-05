from collections import deque


def solution(n: int, m: int, matrix: list[list[str]]) -> int:
    visited = set((0, 0))
    q = deque([(0, 0, 1)])
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]

    while q:
        i, j, count = q.popleft()
        for index in range(4):
            if i == n and j == m:
                return count
            new_i = i + di[index]
            new_j = j + dj[index]
            if (new_i, new_j) not in visited and 0 <= new_i <= n and 0 <= new_j <= m and matrix[new_i][new_j] == '1':
                q.append((new_i, new_j, count + 1))
                visited.add((new_i, new_j))

n, m = map(int, input().split()) 
matrix = []
for _ in range(n):
    matrix.append([char for char in input()])
print(solution(n - 1, m - 1, matrix))




