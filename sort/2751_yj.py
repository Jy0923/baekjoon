import sys

n = int(input(""))
arr =  list(int(sys.stdin.readline()) for _ in range(n))

arr.sort()

for elem in arr:
    print(elem)