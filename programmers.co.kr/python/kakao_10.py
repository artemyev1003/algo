#  https://school.programmers.co.kr/learn/courses/30/lessons/17684#

def solution(msg):
    answer = []
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {l: s.index(l) + 1 for l in s}
    last_index = len(s)
    i = 0
    l = len(msg)
    while i < l:
        j = i + 1
        while j < l and msg[i:j+1] in dictionary:
            j += 1
        answer.append(dictionary[msg[i:j]])
        last_index += 1
        dictionary[msg[i:j+1]] = last_index
        i = j
    return answer
