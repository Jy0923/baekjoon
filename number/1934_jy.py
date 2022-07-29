import math, sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    a, b = map(int, input().split())
    print(math.lcm(a,b))