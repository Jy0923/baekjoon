# 약수
n = int(input())
factors = sorted((map(int, input().split(" ")))) # 항상 약수의 순서대로만 주어지는 것은 아니라는 점.

answer = factors[0] * factors[n-1]

print(answer)