t = int(input())

for i in range(t):
    n, x1, x2, k = map(int, input().split())
    result = 0

    if n < 4:
        print(1)
    else:
        print(min(abs(x1 - x2), n - abs(x1 - x2)) + k)

