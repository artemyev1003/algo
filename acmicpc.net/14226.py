from collections import deque


def solution(s):
    visited = {(1, 0)}
    q = deque([(1, 0, 0)])
    
    while q:
        curr_node, clipboard, count = q.popleft()
        for new_node, new_clipboard, count in [
            (curr_node, curr_node, count), 
            (curr_node + clipboard, clipboard, count),
            (curr_node - 1, clipboard, count)
        ]:
            if new_node == s:
                return count + 1
            if (new_node, new_clipboard) not in visited and 1 <= new_node <= 1000:
                visited.add((new_node, new_clipboard))
                q.append((new_node, new_clipboard, count + 1))


print(solution(int(input())))
