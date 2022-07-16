# 패턴만 업데이트시키면 됨.
global n
n = int(input(""))

def recursive(count, pattern):
    print(pattern)
    new_pattern = []
    count += 1
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                for _ in range(count-1):
                    for _ in range(count-1):
                        new_pattern.append(" ")
                continue
            new_pattern.append(pattern)
        new_pattern.append("\n")
    
    
    if count < (n//3):
        print("depth + 1")
        recursive(count, "".join(new_pattern))

    print("".join(new_pattern))

recursive(1, "*")
