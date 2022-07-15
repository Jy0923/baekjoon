# 단순 python sort를 이용하면 메모리 초과 발생
import sys
from collections import Counter

n = int(input(""))
arr =  list(int(sys.stdin.readline()) for _ in range(n))
counts = Counter(arr)


arr_set = set(arr)

for elem in arr_set:
    for _ in range(counts[elem]):
        print(elem)

