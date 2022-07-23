import sys
input = sys.stdin.readline
input()
A = set(input().split())
B = set(input().split())
print(len(B-A | A-B))