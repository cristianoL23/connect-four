class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def printBoard(self):
        board = self.getBoard()
        print('\n'.join([''.join(['{:4}'.format(colItem) for colItem in row])
                         for row in board]))

    def placeMove(self, move, turn):
        board = self.getBoard()
        rowVal = self.getRows() - 1

        for row in range(rowVal, -1, -1):
            if board[row][move] == 0:
                board[row][move] = turn
                self.setBoard(board)
                currentRow = row
                break
            else:
                continue
        return currentRow
