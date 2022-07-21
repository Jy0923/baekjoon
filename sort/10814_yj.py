n = int(input())
members = []

for i in range(n):
    age, name = input().split(" ")
    age = int(age)
    members.append((i, age, name))

members.sort(key=lambda x: (x[1], x[0]))

for _, age, name in members:
    print(f"{age} {name}")
