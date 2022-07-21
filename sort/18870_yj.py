n = int(input())
points = list(map(int, input().split(" ")))
answer = [-1 for _ in range(n)]

values = {k:v for v,k in enumerate(sorted(list(set(points))))}

for i, num in enumerate(points):
    answer[i] = values[num]

print(*answer)