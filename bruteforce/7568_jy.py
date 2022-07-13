n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

ranker = [1] * n
for i, (x, y) in enumerate(lst):
    for j, (p, q) in enumerate(lst):
        if i != j:
            if x < p and y < q:
                ranker[i] += 1

for r in ranker:
    print(r, end = " ")