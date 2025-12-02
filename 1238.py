from heapq import heapify, heappush, heappop


def calc_distances(f: int) -> dict[int, int]:
    visited = set()
    pq = [(0, f)]
    heapify(pq)

    distances = {i: float("inf") for i in range(1, n + 1)}
    distances[f] = 0

    while pq:
        print(f"pq = {pq}")
        distance, curr = heappop(pq)
        print(f"curr = {curr}, visited = {visited}")
        if curr in visited:
            continue
        visited.add(curr)

        for dest in graph[curr]:
            new_distance = distance + graph[curr][dest]
            if new_distance < distances[dest]:
                distances[dest] = new_distance
                heappush(pq, (new_distance, dest))
                print(distances)
    print(distances)

    return distances

ans = 0
n, m, x = map(int, input().split())

graph = {f: {} for f in range(1, n+1)}

for _ in range(m):
    f, to, distance = map(int, input().split())
    graph[f][to] = distance

return_distances = calc_distances(x)
for i in range(1, n+1):
    if i == x:
        continue
    s = calc_distances(i)[x] + return_distances[i]
    ans = max(s, ans)

print(ans)

