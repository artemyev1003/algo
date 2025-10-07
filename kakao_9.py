# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    numbers = to_base(n, k).split('0')
    for n in numbers:
        if n and is_prime(int(n)):
            answer += 1
    return answer

def to_base(number, base):
    ans = ''
    while number:
        ans += str(number % base)
        number //= base
    return ans[::-1]

def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
