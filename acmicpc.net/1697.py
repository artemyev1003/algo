#  https://www.acmicpc.net/problem/1697


from collections import deque


n, k = map(int, input().split())

def solution():
    if k <= n:
        return n - k
    q = deque([(n, 0)])
    visited = {n} 
    while q:
        curr_pos, count = q.popleft()
        print(f"Got curr_pos = {curr_pos }, count = {count}")
        for new_pos in [curr_pos * 2, curr_pos + 1, curr_pos - 1]:
            if new_pos not in visited and 0 <= new_pos <= 10 ** 5 + 1:
                if new_pos == k:
                    return count + 1
                visited.add(new_pos)
                q.append((new_pos, count + 1))

print(solution())

            
