import sys
input = sys.stdin.readline
n, m = map(int, input().split())
set1 = {input().strip() for _ in range(n)}
set2 = {input().strip() for _ in range(m)}
set3 = set1 & set2
print(len(set3))
print("\n".join(sorted(set3)))