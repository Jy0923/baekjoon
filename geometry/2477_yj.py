num_melon = int(input())
rect = []

# 방향 1: 동쪽, 2: 서쪽, 3: 남쪽, 4: 북쪽
for i in range(6):
    d, l = map(int, input().split(" "))
    rect.append([d,l])

max_w, max_h = 0,0
argmax_w, argmax_h = 0,0
for i in range(len(rect)):
    d,l = rect[i]
    if d in [1,2]: # horizontal
        if max_w < l:
            max_w = l
            argmax_w = i
    
    else: # vertical
        if max_h < l:
            max_h = l
            argmax_h = i

small_w = abs(rect[(argmax_w-1)%6][1] - rect[(argmax_w+1)%6][1]) # 6으로 나머지 연산 안해주면 단순 인덱싱으로 구현이 안됨.
small_h = abs(rect[(argmax_h-1)%6][1] - rect[(argmax_h+1)%6][1])

answer = ((max_w*max_h) - (small_w*small_h))*num_melon

print(answer)