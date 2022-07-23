# 1002 터렛
"""
원의 방정식을 이용하여 풀이
각 사람의 위치와 적과의 거리를 보면, 원을 떠올릴 수 있음.
그렇다면 다음과 같이 경우의 수를 나눌 수 있음.

1. 원이 접하는 경우 -> 적의 위치가 하나로 특정됨.
다만, 내접과 외접 두 가지 경우의 수가 있으므로 이 부분 고려해줘야함.
1-1) 내접인 경우에는 두 원의 반지름 간의 차이가 두 원의 중심거리 d와 동일할 때.
1-2) 외접인 경우에는 두 반지름의 합이 d와 동일할 때.

2. 원이 두 점에서 만나는 경우 -> 적의 위치가 2개로 특정됨.
|r1-r2| < d < r1 + r2

3. 원이 만나지 않는 경우
한 원이 다른 원 내부에 있거나, 혹은 두 원의 반지름을 합해도 d보다 작을 경우 (정말 아예 만나지 않는 경우)
"""
import math

n = int(input())

def get_enemy_loc(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dist == 0 and r1 == r2: # 적의 위치가 무한히 많은 경우
        return -1
    elif abs(r1-r2) == dist or r1 + r2 == dist:
        return 1
    elif abs(r1-r2) < dist < r1 + r2:
        return 2
    else:
        return 0

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    answer = get_enemy_loc(x1, y1, r1, x2, y2, r2)
    print(answer)
