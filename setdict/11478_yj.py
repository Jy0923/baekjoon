# 11478. 서로 다른 부분 문자열의 개수

S = input()
answer = []


for i in range(len(S)):
    for j in range(0, len(S)-i):
        answer.append(S[j:j+i+1])

print(len(set(answer)))