#  https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    final_names = {}
    answer = []
    
    for entry in record:
        if entry.startswith("Enter") or entry.startswith("Change"):
            _, uid, name = entry.split()
            final_names[uid] = name
            
    for entry in record:
        if entry.startswith("Enter"):
            _, uid, _ = entry.split()
            answer.append(f"{final_names[uid]}님이 들어왔습니다.")
        if entry.startswith("Leave"):
            _, uid = entry.split()
            answer.append(f"{final_names[uid]}님이 나갔습니다.")
    
    return answer
