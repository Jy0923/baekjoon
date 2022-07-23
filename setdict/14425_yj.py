n,m = map(int, input().split(" "))
S = set()
test = []

for _ in range(n):
    S.add(input())

for _ in range(m):
    test.append(input())

print(sum(test_s in S for test_s in test))