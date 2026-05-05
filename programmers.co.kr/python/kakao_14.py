#  https://school.programmers.co.kr/learn/courses/30/lessons/17679#

def solution(m, n, board):
    answer = 0
    list_board = []
    for line in board:
        list_board.append(list(line))
    
    while True:    
        block_coords = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if list_board[i][j] and list_board[i][j] == list_board[i+1][j] == list_board[i][j+1] == list_board[i+1][j+1]:
                    for elem in [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]:
                        block_coords.add(elem)
        if (l := len(block_coords)) == 0:
            return answer
        answer += l

        for coord in block_coords:
            x, y = coord
            list_board[x][y] = None
            
        for j in range(n):
            col_blocks = []
            for i in range(m):
                if list_board[i][j] is not None:
                    col_blocks.append(list_board[i][j])
            empty_count = m - len(col_blocks)
            
            for i in range(empty_count):
                list_board[i][j] = None
                
            for i in range(len(col_blocks)):
                list_board[empty_count + i][j] = col_blocks[i]

        for i in range(m - 1):
            for j in range(n):
                if list_board[i][j] and list_board[i+1][j] is None:
                    list_board[i][j], list_board[i+1][j] = None, list_board[i][j]



