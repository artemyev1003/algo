#  https://www.acmicpc.net/problem/13549


from collections import deque


def solution(n: int, k: int) -> int:
    if n >= k:
        return n - k
    max = 10 ** 5 + 1
    upper_bound = min(max, k * 2 - n)
    time = [max] * max
    time[n] = 0
    q = deque([(n, 0)])

    while q:
        curr, count = q.popleft()
        if curr == k:
            return count 
        
        new = curr * 2
        if new < upper_bound and count < time[new]:
            time[new] = count
            q.appendleft((new, count))

        for new, count in [(curr + 1, count + 1), (curr - 1, count + 1)]:
            if 0 <= new < upper_bound and count < time[new]:
                time[new] = count
                q.append((new, count))

n, k = map(int, input().split())
print(solution(n, k))
