# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    for char in new_id.lower():
        if (char.isalnum() or char in ("-", "_", ".")) and not (answer.endswith(".") and char == "."):
            answer += char
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    if answer == "":
        answer = "a"
    answer = answer[:15]
    if answer.endswith('.'):
        answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer
