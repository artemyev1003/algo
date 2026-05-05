def solution(n, t, m, p):
    answer = ''
    all_nums = ''
    curr_num = 0
    pos = p
    while True:
        all_nums += to_base(curr_num, n)
        curr_num += 1
        print(f"all_nums: {all_nums}")
        if len(all_nums) >= pos:
            print(f"pos: {pos - 1}")
            answer += all_nums[pos - 1]
            pos = pos + m
            print(f"answer: {answer}")
        if len(answer) == t:
            break
    return answer

def to_base(number, base):
    base_string = "0123456789ABCDEF"
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"

print(solution(16, 16, 2, 2))
