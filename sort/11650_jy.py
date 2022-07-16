n = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(n)])
for a,b in lst:
    print(a,b)