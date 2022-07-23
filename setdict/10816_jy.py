import sys
from collections import Counter

input = sys.stdin.readline
n = input()
cards = Counter(input().split())
m = input()
nums = [cards[num] for num in input().split()]
print(*nums)