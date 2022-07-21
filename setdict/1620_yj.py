n,m = map(int, input().split(" "))
poke = [input() for _ in range(n)]
test = [input() for _ in range(m)]


poke_dict = {idx+1:name for idx, name in enumerate(poke)}
poke_reverse = {name:idx+1 for idx, name in enumerate(poke)}


for poke_test in test:
    if poke_test.isdigit():
        print(poke_dict[int(poke_test)])
    else:
        print(poke_reverse[poke_test])