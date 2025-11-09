from collections import deque


def solution(m: int, n: int, h: int, grid: list[list[list[str]]]) -> int:
    q = deque()
    count_zero = 0
    visited = set()
    dx = [0, 0, 0, 1, 0, -1]
    dy = [0, 0, 1, 0, -1, 0]
    dz = [1, -1, 0, 0, 0, 0]
    for layer in range(h):
        for column in  range(n):
            for row in  range(m):
                if grid[layer][column][row] == "1":
                    q.append([layer, column, row, 0])
                    visited.add((layer, column, row))
                elif grid[layer][column][row] == "0":
                    count_zero += 1

    if count_zero == 0:
        return 0
    
    while q:
        l, c, r, count = q.popleft()
        for d in range(6):
            curr_l = l + dz[d]
            curr_c = c + dy[d]
            curr_r = r + dx[d]
            if 0 <= curr_l < h and 0 <= curr_c < n and 0 <= curr_r  < m:
                tomato = grid[curr_l][curr_c][curr_r]   
                if (curr_l, curr_c, curr_r) not in visited and tomato == "0":
                    count_zero -= 1
                    if count_zero == 0:
                        return count + 1
                    visited.add((curr_l, curr_c, curr_r))
                    q.append(((curr_l, curr_c, curr_r, count + 1))) 
    return -1 


m, n, h = map(int, input().split())

grid = [[list(input().split()) for j in range(n)] for i in range(h)]
print(solution(m, n, h, grid))

