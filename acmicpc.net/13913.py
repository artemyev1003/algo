#  https://www.acmicpc.net/problem/13913


from collections import deque


n, k = map(int, input().split())

def solution():
    if k <= n:
        return n - k, range(n, k - 1, -1)

    max_pos = 10 ** 5 + 1
    parent = [0] * max_pos

    q = deque([n])
    visited = {n}
    while q:
        curr_pos = q.popleft()
        for new_pos in [curr_pos * 2, curr_pos + 1, curr_pos - 1]:
            if new_pos not in visited and 0 <= new_pos < max_pos:
                if new_pos == k:
                    parent[new_pos] = curr_pos
                    route = []
                    temp = k
                    while temp != n:
                        print("Started reconstructing route")
                        print(f"route = {route}, temp = {temp}")
                        route.append(temp)
                        temp = parent[temp]
                    route.append(n)
                    return len(route) - 1, reversed(route)
                else:
                    visited.add(new_pos)
                    parent[new_pos] = curr_pos
                    print(f"parent = {parent[:100]}")
                    q.append(new_pos)

count, route = solution()
print(count)
print(*route)
