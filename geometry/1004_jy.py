import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input().strip())
    cnt = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        d1 = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (0.5)
        d2 = ((x2 - x) ** 2 + (y2 - y) ** 2) ** (0.5)
        if d1 < r and d2 < r:
            continue
        elif d1 < r or d2 < r:
            cnt += 1
    print(cnt)