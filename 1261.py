from collections import deque


m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs():
    di = [1, 0, -1, 0]
    dj = [0, -1, 0, 1]

    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        i, j, count = queue.popleft()

        if i == n - 1 and j == m - 1:
            return count

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = True
                if graph[ni][nj] == '0':
                    queue.appendleft((ni, nj, count))
                else:
                    queue.append((ni, nj, count + 1))

print(bfs())
