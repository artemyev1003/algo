#  https://school.programmers.co.kr/learn/courses/30/lessons/17678


from collections import deque

def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def solution(n, t, m, timetable):
    waiting_queue = deque(sorted([to_minutes(time) for time in timetable]))
    
    last_boarding_time = 0
    
    for i in range(n):
        bus_time = 540 + i * t
        boarded_count = 0
        
        while boarded_count < m and waiting_queue and waiting_queue[0] <= bus_time:
            last_passenger_arrival = waiting_queue.popleft()
            boarded_count += 1
        
        if i == n - 1: 
            if boarded_count < m:
                last_boarding_time = bus_time
            else:
                last_boarding_time = last_passenger_arrival - 1
                
    hours = last_boarding_time // 60
    mins = last_boarding_time % 60
    
    return f"{hours:02d}:{mins:02d}"
