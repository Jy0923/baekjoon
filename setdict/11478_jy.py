import sys
input = sys.stdin.readline
s = input().strip()
n = len(s)
results = set()
for i in range(1, n + 1):
    for j in range(n-i+1):
        results.add(s[j:j+i])
print(len(results))