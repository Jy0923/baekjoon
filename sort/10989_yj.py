# 단순 python sort를 이용하면 메모리 초과 발생 -> 카운팅 정렬 구현 (정렬 알고리즘 정리해볼 것.)
import sys

n = int(input(""))
counts = [0 for _ in range(10001)] # 수의 범위가 작은 걸 고려해줬어야 했음.

for _ in range(n):
    counts[int(sys.stdin.readline())] += 1

for i in range(len(counts)):
    for _ in range(counts[i]):
        print(i)