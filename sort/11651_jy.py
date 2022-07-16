n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([y, x])
    
lst = sorted(lst)
for y,x in lst:
    print(x,y)