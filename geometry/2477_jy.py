k = int(input())
s = [list(map(int, input().split()))[1] for i in range(6)]

max_idx = 0
max_rec = 0
for i in range(6):
    if s[i%6] * s[(i+1)%6] > max_rec:
        max_rec = s[i%6] * s[(i+1)%6]
        max_idx = i
min_rec = s[(max_idx+3)%6] * s[(max_idx+4)%6]

print(k * (max_rec - min_rec))