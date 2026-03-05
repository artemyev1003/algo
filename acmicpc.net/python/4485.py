from heapq import heapify, heappop, heappush


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 1

while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    distances = [[float("inf")] * n for _ in range(n)]
    pq = [(grid[0][0], (0, 0))]
    heapify(pq) 

    while pq:
        curr_val, coords = heappop(pq)
        if coords in visited:
            continue
        x, y = coords
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_val = curr_val + grid[nx][ny]
                if new_val < distances[nx][ny]:
                    distances[nx][ny] = new_val
                    heappush(pq, (new_val, (nx, ny)))
    print(f"Problem {count}: {distances[n-1][n-1]}")
    count += 1

