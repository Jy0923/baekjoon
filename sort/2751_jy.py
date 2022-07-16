import sys
n = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for _ in range(n)])
print("\n".join([str(i) for i in lst]))