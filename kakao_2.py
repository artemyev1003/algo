# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(n, stages):
    stages.sort()
    result = {k: 0 for k in range(1, n + 1)} 
    curr = stages[0] 
    count = 1
    for i in range(1, len(stages)):
        if stages[i] == curr:
            count += 1
        else:
            result[curr] = count / (len(stages) - i + count)
            count = 1
            curr = stages[i]
        if curr <= n:
            result[curr] = count / (len(stages) - i - 1 + count) 
    return sorted(result, key=result.get, reverse=True)

