def solution(dartResult):
    powers = {"S": 1, "D": 2, "T": 3}
    res_list = []

    dartResult = dartResult.replace('10', "A")  

    for char in dartResult:
        if char.isdigit():
            res_list.append(int(char))
        elif char == 'A':
            res_list.append(10)
        elif char in powers:
            res_list[-1] **= powers[char]
        elif char == "*":
            res_list[-2:] = [r * 2 for r in res_list[-2:]]
        else:
            res_list[-1] *= -1
    return sum(res_list)


print(solution("1T2D3D#"))
