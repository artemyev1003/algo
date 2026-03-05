from collections import deque


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i: int, j: int, visited: list[list[bool]]) -> None:
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny)) 

def solution(grid: list[list[int]]) -> int:
    year = 0
    while True:
        count = 0
        visited = [[True if cell == 0 else False for cell in row] for row in grid]
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and grid[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    count += 1
                    if count > 1:
                        return year
                    bfs(i, j, visited)

        sea = [[True if cell == 0 else False for cell in row] for row in grid]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    sea_count = 0
                    for s in range(4):
                        nx = i + dx[s]
                        ny = j + dy[s]
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and sea[nx][ny]:
                            sea_count += 1
                    grid[i][j] -= sea_count 
                    if grid[i][j] < 0:
                        grid[i][j] = 0
        year += 1
        if count == 0:
            return 0

print(solution(grid))
