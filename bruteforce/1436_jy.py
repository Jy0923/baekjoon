n = int(input())
counter = 0
number = 666
while True:
    if "666" in str(number):
        counter += 1
        if counter == n:
            break
    number += 1
print(number)