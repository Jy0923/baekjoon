import sys
n = int(sys.stdin.readline())
lst = list()
counter = dict()
for i in range(n):
    number = int(sys.stdin.readline())
    lst.append(number)
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
lst.sort()
max_count = max(counter.values())
modes = []
for v,k in counter.items():
    if k == max_count:
        modes.append(v)
if len(modes) == 1:
    mode = modes[0]
else:
    mode = sorted(modes)[1]

print(round(sum(lst)/n))
print(lst[n//2])
print(mode)
print(max(lst) - min(lst))