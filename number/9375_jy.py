import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        n, k = input().split()
        if k in clothes:
            clothes[k] += 1
        else:
            clothes[k] = 1
    result = 1
    for i in clothes.values():
        result *= i+1
    print(result - 1)