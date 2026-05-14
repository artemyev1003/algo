n = int(input())
a = list(map(int, input().split()))
current_result = 1
current_count = 1
previous_count = 0
current = a[0]
previous = -1

for i in range(1, n):
    next = a[i]
    if next == current:
        current_count += 1
    elif next == previous:
        previous_count += current_count;
        previous = current
        current = next
        current_count = 1
    else:
        current_result = max(current_result, current_count + previous_count)
        previous = current
        previous_count = current_count
        current = next
        current_count = 1

print(max(current_result, current_count + previous_count))
