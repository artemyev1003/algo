def solution(s):
    min_len = len(s)
    n = len(s)
    for k in range(1, n // 2 + 1):
        compressed_len = 0
        l = 0
        curr = s[l : l + k]
        count = 1
        while l + k < n:
            l += k
            next_unit = s[l : l + k]
            if curr == next_unit:
                count += 1
            else:
                if count > 1:
                    compressed_len += len(str(count)) + k
                else:
                    compressed_len += k
                
                curr = next_unit
                count = 1


        if count > 1:
            compressed_len += len(str(count)) + k
        else:
            compressed_len += len(curr)
        min_len = min(min_len, compressed_len)

    return min_len
