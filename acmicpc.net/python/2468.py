import sys
from collections import deque


sys.setrecursionlimit(10 ** 5)

def dfs(x: int, y: int, level: int, n: int) -> None:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > level and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, level, n)

def bfs(x: int, y: int, level: int, n: int) -> None:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(x, y)])
    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > level and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))



n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
levels = set()
for row in grid:
    levels |= set(row)

ans = 1


for level in levels:
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > level and not visited[i][j]:
                count += 1
                visited[i][j] = True
                bfs(i, j, level, n)
    ans = max(ans, count)

print(ans)
