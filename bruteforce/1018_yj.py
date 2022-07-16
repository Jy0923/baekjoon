# 1018 체스판 다시 칠하기 (최소 개수를 구해야함.)
# 비교할 체스판을 2개 만들어놓고 걔랑 비교하면 될 것 같음.

global chess_w, chess_b
chess_w = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
chess_b = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

m,n = map(int, input("").split(" "))

board = [input("") for _ in range(m)]
min_count = float('inf')


def count_recolor(cut_board):
    w_count, b_count = 0, 0
    for r_board, r_chess in zip(cut_board, chess_w):
        for b, c in zip(r_board, r_chess):
            if b != c:
                w_count += 1
    
    for r_board, r_chess in zip(cut_board, chess_b):
        for b, c in zip(r_board, r_chess):
            if b != c:
                b_count += 1

    return min(w_count, b_count)

for i in range(m-7):
    for j in range(n-7):
        cut_board = list(map(lambda x: x[j:j+8], board[i:i+8])) # 이 cut_board 부분 만들어주는 부분이 단순 인덱싱으로 구현이 안된다는 점.
        min_count = min(count_recolor(cut_board), min_count)


print(min_count)

