import sys
n, m = map(int, sys.stdin.readline().split())
S = set([sys.stdin.readline() for _ in range(n)])
cnt = 0 
for _ in range(m):
    word = sys.stdin.readline()
    if word in S:
        cnt += 1  
print(cnt)