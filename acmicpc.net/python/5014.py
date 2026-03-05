from collections import deque


def solution(f: int, s: int, g: int, u: int, d: int) -> int | str:
    visited = {s}
    q = deque([(s, 0)])

    if s == g:
        return 0

    while q:
        curr, count = q.popleft()
        # print(f"got curr = {curr}, count = {count}")
        for new in [curr + u, curr - d]:
            if 1 <= new <= f and new not in visited:
                if new == g:
                    return count + 1
                q.append((new, count + 1))
                visited.add(new)
    return "use the stairs"


f, s, g, u, d = map(int, input().split())
print(solution(f, s, g, u, d))
