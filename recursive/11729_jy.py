def hanoi(n, start, end, another):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, another, end)
        print(start, end)
        hanoi(n-1, another, end, start)

n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3, 2)

# 틀린 풀이
# 이동 횟수의 규칙을 발견하지 못햇을 경우 이동 횟수를 카운트하는 방식 + result 를 더해나가는 방식으로 함수를 만들어봄
# result를 구할 때 같은 연산을 반복적으로 하게 되어 연산량이 기하급수적으로 많아져서 실패함
# DP 형식으로 풀어보려 햇으나 시작점과 끝지점의 조합도 생각해야 하므로 복잡함...
#def hanoi(n, start, end, another, counter, result):
#    if n == 1:
#        result += str(start) + " " + str(end) + "\n"
#        counter += 1
#    else:
#        counter, result = hanoi(n-1, start, another, end, counter, result)
#        result += str(start) + " " + str(end) + "\n"
#        counter += 1
#        counter, result = hanoi(n-1, another, end, start, counter, result)
#    return counter, result
#
#n = int(input())
#counter, result = hanoi(n, 1, 3, 2, 0, "")
#print(counter)
#print(result)