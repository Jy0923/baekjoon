# 7568 덩치
import sys

n = int(input(""))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ranks = [1 for _ in range(n)]

def compare(arr1, arr2):
    if (arr1[0] < arr2[0]) and (arr1[1] < arr2[1]):
        return 1
    else:
        return 0

for i in range(len(arr)):
    for j in range(len(arr)):
        ranks[i] += compare(arr[i], arr[j])

print(*ranks)