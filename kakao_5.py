#  https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    participants = {name: set() for name in id_list}
    reports = {name: 0 for name in id_list}
    banned = set()
    for elem in report:
        user, reported = elem.split()
        if reported not in participants[user]:
            participants[user].add(reported)
            reports[reported] += 1
        if reports[reported] == k:
            banned.add(reported)
    for reported in participants.values():
        answer.append(len(reported.intersection(banned)))


    return answer



def solution_optimal(id_list, report, k):
    answer = [0] * len(id_list)
    clean_report = set(report)
    reports = {name: 0 for name in id_list}
    for elem in clean_report:
        reports[elem.split()[1]] += 1

    for elem in clean_report:
        if reports[elem.split()[1]] >= k:
            answer[id_list.index(elem.split()[0])]+= 1

    return answer



