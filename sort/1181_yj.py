n = int(input(""))
arr = [input("") for _ in range(n)]

answer = sorted(list(set(arr)), key=lambda x: (len(x),x))

for word in answer:
    print(word)