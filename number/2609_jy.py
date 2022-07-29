def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
gcd = get_gcd(a, b)
print(gcd, a * b // gcd)