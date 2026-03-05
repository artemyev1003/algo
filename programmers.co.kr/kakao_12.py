# https://school.programmers.co.kr/learn/courses/30/lessons/17686

from collections import defaultdict


def get_num_key(file_name):
    key = ''
    num_flag = False
    count = 0
    for char in file_name:
        if char.isdigit():
            key += char
            count += 1
            num_flag = True
            if count == 5:
                break
        elif num_flag is True:
            break
    return int(key)
            
def solution(files):
    answer = []
    files_dict = defaultdict(list)
    for file in files:
        head = ''
        for char in file:
            if not char.isdigit():
                head += char
            else:
                break
        files_dict[head.lower()].append(file)
                    
    for name in sorted(files_dict):
        answer += sorted(files_dict[name], key=get_num_key)
    
    return answer
