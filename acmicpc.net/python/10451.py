def solve(perm: list[int], n: int) -> int:
    count = 0
    indices = [i + 1 for i in range(n)]
    visited = set()
    for i in indices:
        next = i
        while True:
            if next in visited:
                break
            visited.add(next)
            next = perm[next - 1]
            if next in visited:
                count += 1
                break
    return count

t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))
    print(solve(perm, n))

