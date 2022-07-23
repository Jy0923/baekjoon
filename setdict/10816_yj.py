from collections import Counter

n = int(input())
user_cards = Counter(map(int, input().split(" ")))
m = int(input())
test_cards = list(map(int, input().split(" ")))

for card in test_cards:
    print(user_cards[card], end = " ")
