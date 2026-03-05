from collections import defaultdict, deque


def solution(computers: dict[int, set[int]]) -> int:
    visited = set()
    infected = set()
    q = deque([1])
    count = 0
    while q:
        comp = q.popleft()
        for new in computers[comp]:
            if new not in visited and new not in infected:
                q.append(new)
                count += 1
                visited.add(comp)
                infected.add(new)
    return count

input()
computers = defaultdict(set)
for _ in range(int(input())):
    a, b = map(int, input().split())
    computers[a].add(b)
    computers[b].add(a)
print(solution(computers))
    
