t = int(input())
for i in range(t):
    n = int(input())
    arr = input().split()
    count = ones = twos = zeroes = 0
    for j in range(n):
        num = int(arr[j])
        if num == 0:
            zeroes += 1
        elif num == 1:
            ones += 1
        else:
            twos += 1

    count += zeroes

    pairs = min(ones, twos)
    count += pairs
    ones -= pairs
    twos -= pairs

    count += ones // 3
    count += twos // 3
    print(count)

