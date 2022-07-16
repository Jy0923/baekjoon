import sys
n = int(sys.stdin.readline())
counter = [0] * 10000
for _ in range(n):
    counter[int(sys.stdin.readline()) - 1] += 1

for i, n in enumerate(counter):
    for _ in range(n):
        print(i + 1)