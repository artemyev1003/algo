#  https://school.programmers.co.kr/learn/courses/30/lessons/17683#

def replace_notes(melody):
    return melody.replace("C#", "W").replace("D#", "X").replace("F#", "Y").replace("G#", "Z").replace("A#", "V").replace("B#", "U")

def solution(m, musicinfos):
    fit_melodies = []
    m = replace_notes(m)
    
    for index, info in enumerate(musicinfos):
        start_time, end_time, name, melody = info.split(",")
        start_hours, start_mins = start_time.split(":")
        end_hours, end_mins = end_time.split(":")
        time = int(end_hours) * 60 + int(end_mins) - int(start_hours) * 60 - int(start_mins)
        melody = replace_notes(melody)
        
        
        while len(melody) < time:
            melody += melody
        melody = melody[:time]
        
        if m in melody:
            fit_melodies.append((name, time, index))
    
    if not fit_melodies:
        return "(None)"
    return sorted(fit_melodies, key=lambda x: (-x[1], x[2]))[0][0]
