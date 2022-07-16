def counter(mn, start_r, start_c):
    startW = 0
    startB = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if mn[start_r + i][start_c + j] == "B": # W로 시작
                    startW += 1
                else: # B로 시작
                    startB += 1
            else:
                if mn[start_r + i][start_c + j] == "W": # W로 시작
                    startW += 1
                else: # B로 시작
                    startB += 1
    return min(startW, startB)

m, n = map(int, input().split())
mn = list()
for _ in range(m):
    mn.append(list(input()))

mi = m * n
for i in range(m-7):
    for j in range(n-7):
        c = counter(mn, i, j)
        if c < mi:
            mi = c
print(mi)