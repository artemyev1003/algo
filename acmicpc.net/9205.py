from collections import deque


def can_go(x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
    print("checking: ", x_1, x_2, y_1, y_2)
    return abs(x_1 - x_2) + abs(y_1 - y_2) <= 1000

def is_happy() -> bool:
    n = int(input())
    shops = []
    home_x, home_y = map(int, input().split())
    for _ in range(n):
        shops.append(tuple(map(int, input().split())))
    fest_x, fest_y = map(int, input().split())
    
    q = deque([(home_x, home_y)]) 
    visited = set() 
    print(f"shops = {shops}")
    while q:
        curr_x, curr_y = q.popleft()
        print(f"checking {curr_x}, {curr_y}")
        if can_go(curr_x, curr_y, fest_x, fest_y):
            print("can go")
            return True 
        visited.add((curr_x, curr_y))
        for shop in shops:
            print("getting shop from list: ", shop)
            if shop not in visited and can_go(curr_x, curr_y, *shop):
                print("appending", shop)
                q.append(shop)
        print(f"q = {q}")
    return False

t = int(input())
ans = []

for test in range(t):
   ans.append(is_happy()) 

for a in ans:
    print("happy" if a else "sad")
