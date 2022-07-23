# 1269 대칭 차집합

n,m = map(int, input().split(" "))
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))

answer = len(A.difference(B).union(B.difference(A)))
print(answer)