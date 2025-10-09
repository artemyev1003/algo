#  https://school.programmers.co.kr/learn/courses/30/lessons/150370

def date_to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 12 * 28 + month * 28 + day
    
 
def solution(today, terms, privacies):
    answer = []
    conditions = {}
    
    today_days = date_to_days(today)
    
    for t in terms:
        term, months = t.split()
        conditions[term] = int(months) * 28
    
    for index, privacy in enumerate(privacies, start=1):
        date, term = privacy.split()
        if date_to_days(date) + conditions[term] <= today_days:
            answer.append(index)
        
    return answer
