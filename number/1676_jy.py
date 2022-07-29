n = int(input())
lst = [0, 0]
for i in range(1, n+1):
    while i % 2 == 0:
        i //= 2
        lst[0] += 1
    while i % 5 == 0:
        i //= 5
        lst[1] += 1
print(min(lst))