# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        ans_row = format(i | j, f'0{n}b')
        ans_row = ans_row.replace('0', ' ')
        ans_row = ans_row.replace('1', '#')
        answer.append(ans_row)
    return answer

