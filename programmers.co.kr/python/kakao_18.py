#  https://school.programmers.co.kr/learn/courses/30/lessons/60058


from collections import deque


def is_correct(line):
    queue = deque()
    for char in line:
        if queue and char == ")" and queue[-1] == "(":
            queue.pop()
        else:
            queue.append(char)
    return not queue
            

def convert_line(line):
    if not line:
        return ""
    
    count_open = count_close = 0
    for i, char in enumerate(line):
        if char == "(":
            count_open += 1
        else:
            count_close += 1
        if count_open == count_close:
            u = line[:i+1]
            v = line[i+1:]
            break
            
    if is_correct(u):
        return u + convert_line(v)
    else:
        new_line = "(" + convert_line(v) + ")"
        transformed_u = ""
        for char in u[1:-1]:
            transformed_u += ")" if char == "(" else "("
        
        return new_line + transformed_u
        
    
def solution(p):
    return convert_line(p)
