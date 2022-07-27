import sys, math

input = sys.stdin.readline
n = int(input().strip())
lst = [int(input().strip()) for _ in range(n)]
lst = [lst[i+1]-lst[i] for i in range(n-1)]
gcd = math.gcd(*lst)

results = []
for i in range(1, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        results.append(i)
        results.append(gcd // i)

print(*sorted(set(results))[1:])