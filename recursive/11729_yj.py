# 11729 하노이의 탑
global path
n = int(input("")) # 원판의 개수
path = []

def recursive(src, med, tgt, n):
    
    if n == 1:
        path.append([src, tgt])
        return
    
    else:
        recursive(src, tgt, med, n-1)
        path.append([src, tgt])
        recursive(med, src, tgt, n-1)

recursive(1,2,3,n)

print(len(path))
for p in path:
    print(*p)


