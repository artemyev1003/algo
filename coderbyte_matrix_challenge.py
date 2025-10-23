#  https://www.chegg.com/homework-help/questions-and-answers/matrix-challenge-function-matrixchallenge-strarr-read-strarr-array-consisting-locations-qu-q63602323


import pprint


def matrix_challenge(positions: list[str]) -> int:
    count = 0
    queen_pos = positions[0]
    queen_x = int(queen_pos[1]) - 1
    queen_y = int(queen_pos[3]) - 1
    
    king_pos = positions[1]
    king_x = int(king_pos[1]) - 1
    king_y = int(king_pos[3]) - 1

    board = []
    for i in range(8):
        if i == queen_x:
            board.append([False for _ in range(8)])
        else:
            board.append([False if j == queen_y or abs(queen_x - i) == abs(queen_y - j) else True for j in range(8)])

    pprint.pprint(board)

    if board[king_x][king_y]:
        return -1

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(8):
        cell_x = king_x + dx[i]
        cell_y = king_y + dy[i]

        if cell_x == queen_x and cell_y == queen_y:
            return 1

        if 0 < cell_x < 8 and 0 < cell_y < 8 and board[cell_x][cell_y]:
            count += 1
        
    return count

print(matrix_challenge(["(1,1)", "(2,2)"]))
