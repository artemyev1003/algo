from collections import defaultdict, deque


def solution(s, f, relations: defaultdict[int, list[int]]) -> int:
    visited = set() 
    q = deque([(s, 0)])
    while q:
        current, count = q.popleft()
        visited.add(current)
        for relative in relations[current]:
            if relative == f:
                return count + 1
            elif relative not in visited:
                q.append((relative, count + 1))
    return -1
    

input()
s, f = map(int, input().split())
m = int(input())
relations = defaultdict(list)
for _ in range(m):
    parent, child = map(int, input().split())
    relations[parent].append(child)
    relations[child].append(parent)

print(solution(s, f, relations))
