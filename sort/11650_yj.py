import sys

n = int(input(""))
arr = list(list(map(int, sys.stdin.readline().split(" "))) for _ in range(n))

arr.sort(key=lambda x: (x[0], x[1]))

for elem in arr:
    print(*elem)