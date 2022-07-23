def solution(x1, y1, r1, x2, y2, r2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    if d == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    if d > r1 + r2 or d < r1 - r2:
        return 0
    elif d == r1 + r2 or d == r1 - r2:
        return 1
    elif d > r1 - r2:
        return 2

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if r1 < r2:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
    print(solution(x1, y1, r1, x2, y2, r2))