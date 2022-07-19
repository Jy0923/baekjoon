import sys
input = sys.stdin.readline
n, m = map(int, input().split())
kv = {input().strip() : str(i) for i in range(1, n+1)}
vk = {v : k for k,v in kv.items()}
for _ in range(m):
    q = input().strip()
    if q.isalpha():
        print(kv[q])
    else:
        print(vk[q])