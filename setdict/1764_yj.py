n,m = map(int, input().split(" "))
never_heard = set(input() for _ in range(n))
never_seen = set(input() for _ in range(m))

never_hs = never_seen.intersection(never_heard)

print(len(never_hs))
for name in sorted(list(never_hs)): # set이 항상 사전 순 정렬을 보장하지는 않는다는 점
    print(name)