def recursive(n, s, i, j):
    if n == 3:
        for r in range(3):
            for c in range(3):

                if r == 1 and c == 1:
                    s[i+r][c+j] = " "
                else:
                    s[i+r][c+j] = "*"
        
    else:
        for r in range(3):
            for c in range(3):

                if r ==1 and c == 1:
                    for ir in range(n//3):
                        for ic in range(n//3):
                            s[i + r * (n // 3) + ir][j + c * (n // 3) + ic] = " "
                else:
                    s = recursive(n // 3, 
                                  s, #s[r * (n // 3) : (r + 1) * (n // 3)][c * (n // 3) : (c + 1) * (n // 3)],
                                  i + r * (n // 3), 
                                  j + c * (n // 3))
    return s

n = int(input())
s = [['_' for _ in range(n)] for _ in range(n)]
s = recursive(n, s, 0, 0)
for i in s:
    for j in i:
        print(j, end = "")
    print()