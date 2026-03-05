n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    if grid[x][y] == 0:
        grid[x][y] = 2 
        count += 1

    cleaned_any = False

    for _ in range(4):
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            x, y = nx, ny
            cleaned_any = True
            break

    if cleaned_any:
        continue

    back = (d + 2) % 4
    bx = x + dx[back]
    by = y + dy[back]

    if grid[bx][by] == 1:
        break

    x, y = bx, by

print(count)

