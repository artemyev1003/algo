#  https://school.programmers.co.kr/learn/courses/30/lessons/72411


from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for course_len in course:
        combination_counts = defaultdict(int)
        for order in orders:
            order = sorted(order)
            
            for combo in combinations(order, course_len):
                combination_counts["".join(combo)] += 1
        if not combination_counts:
            continue
            
        max_count = 0
        for count in combination_counts.values():
            if count >= 2:
                max_count = max(max_count, count)
        
        if max_count < 2:
            continue
            
        for combo, count in combination_counts.items():
            if count == max_count and count >= 2:
                answer.append(combo)
    return sorted(answer)
    
            
