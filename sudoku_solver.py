""" given a sudoku board solve the puzzle. youtube tutorail:https://www.youtube.com/watch?v=NuodN41aK3g"""

def sudokusolver(board):
    def is_Full(board):
        for x in range(0, 9):
            for y in range (0, 9):
                if board[x][y] == 0:
                    return False
        return True

    def possiblentries(board, i, j):
        # generate a possibilities array
        possibilities = {}

        # initializing the key value pairs
        for x in range(1, 10):
            possibilities[x] = 0

        # horizontal entries
        # if the position is not 0 , assign the key the the value of 1
        for y in range(0, 9):
            if not board[i][y] == 0:
                possibilities[board[i][y]] = 1

        # vertical entries
        for y in range(0, 9):
            if not board[x][j] == 0:
                possibilities[board[x][j]] = 1

        k = 0
        l = 0

        if i >= 0 and i <= 2:
            k = 0
        elif i >= 3 and i <=5:
            k = 3
        else:
            k = 6
        if j >= 0 and j <= 2:
            l = 0
        elif j >= 3 and j <= 5:
            l = 3
        else:
            l = 6

        for x in range(k, k + 3):
            for y in range(l, l + 3):
                if not board[x][y] == 0:
                    possibilities[board[x][y]] = 1

        for x in range(1, 10):
            if possibilities[x] == 0:
                possibilities[x] = x
            else:
                possibilities[x] = 0

        return possibilitiess

        def solver(board):
            i = 0
            j = 0
            possibilities = {}

        if isFull(board):
            print("board solved")
            print (board)
            return
        else:

            for x in range(0, 9):
                for y in range (0, 9):
                    if board[x][y] == 0:
                        i = x
                        j = y
                        break
                else:
                    continue
                break

        possibles = possiblentries(board, i ,j)

            for x in range(1, 10):
                if not possibilities[x] == 0:
                    board[i][j] = possibilities[x]
                    sudokusolver(board)
            boards[i][j] = 0
