# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    combinations1 = {}
    combinations2 = {}

    i = 0
    while i < len(str1) - 1:
        duplet = str1[i:i+2].lower()
        if duplet.isalpha():
            if duplet in combinations1:
                combinations1[duplet] +=1 
            else:
                combinations1[duplet] = 1
        i += 1
                
    i = 0
    while i < len(str2) - 1:
        duplet = str2[i:i+2].lower()
        if duplet.isalpha():
            if duplet in combinations2:
                combinations2[duplet] +=1 
            else:
                combinations2[duplet] = 1
        i += 1

    intersection_len = union_len = 0

    for elem in set(combinations1.keys()).union(set(combinations2.keys())):
        intersection_len += min(combinations1.get(elem, 0), combinations2.get(elem, 0))
        union_len += max(combinations1.get(elem, 0), combinations2.get(elem, 0))

    if union_len == intersection_len:
        return 65536
    if union_len == 0:
        return 0

    return int(intersection_len / union_len * 65536)
# print(solution("E=M*C^2", "e=m*c^2"))
