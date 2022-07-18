n = int(input())
lst = list(map(int, input().split()))
set_list = sorted(set(lst))
counter = {num:i for i,num in enumerate(set_list)}
for e in lst:
    print(counter[e], end = " ")