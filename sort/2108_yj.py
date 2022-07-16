import sys
from collections import Counter

n = int(input(""))
arr =  list(int(sys.stdin.readline()) for _ in range(n))

arr.sort()
counters = sorted(list(Counter(arr).items()), key=lambda x: x[1], reverse=True)

range = arr[-1] - arr[0]
median = arr[len(arr)//2]
mean = round(sum(arr)/len(arr))

if len(counters) > 1:
    if counters[0][1] > counters[1][1]:
        mode=counters[0][0]
    else:
        mode=counters[1][0]
else:
    mode=counters[0][0]


print(mean)
print(median)
print(mode)
print(range)