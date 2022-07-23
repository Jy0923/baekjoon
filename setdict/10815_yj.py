n = int(input())
cards = set(map(int, input().split(" ")))
m = int(input())
answer = list(map(int, input().split(" ")))

for card in answer:
    if card in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")