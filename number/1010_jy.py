import math, sys
input = sys.stdin.readline
t = int(input())
print("\n".join([str(math.comb(*list(map(int, input().split()))[::-1])) for _ in range(t)]))