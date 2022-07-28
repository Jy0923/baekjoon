import math
n = int(input())
lst = list(map(int, input().split()))
for i in lst[1:]:
    gcd = math.gcd(lst[0], i)
    print(str(lst[0] // gcd) + "/" + str(i // gcd))