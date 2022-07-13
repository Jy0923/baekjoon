# 1436 영화감독 숌

n = int(input(""))

# 정말 단순하게 접근하면 while하고 count 세면서 n까지 계속 돌고, 666부터 차근차근 세는 방식이 있지...
count = 0
cp = str(666)

while True:
    if '666' in cp:
        count += 1
    if count == n:
        print(cp)
        break

    cp = str(int(cp)+1)
