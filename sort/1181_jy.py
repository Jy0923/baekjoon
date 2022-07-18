import sys
n = int(sys.stdin.readline())
lst = dict()
for i in range(n):
    word = sys.stdin.readline().strip()
    lst[word] = len(word)
lst = list(lst.items())
lst.sort(key = lambda x : [x[1], x[0]])
for i in lst:
    print(i[0])