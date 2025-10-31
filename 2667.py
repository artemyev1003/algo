from collections import deque


def solution(n: int, matrix: list[str]) -> list[int]:
    print(matrix)
    ans = []
    visited = set()
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and matrix[i][j] == '1':
                count = 1
                q = deque([(i, j)])
                visited.add((i, j))
                while q:
                    x, y = q.popleft()
                    for s in range(4):
                        new_x = x + di[s]
                        new_y = y + dj[s]
                        if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                            if matrix[new_x][new_y] == '1':
                                count += 1
                                q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                ans.append(count)

    return ans

n = int(input())
m = []
for _ in range(n):
    m.append(input())

ans = sorted(solution(n, m))
print(len(ans))
for num in ans:
    print(num)
            
