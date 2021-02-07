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
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))
    
    def placeMove(self, move, turn):
        board = self.getBoard()
        rowVal = self.getRows() -1
        
        for i in range(rowVal, 0, -1):
            if board[i][move] == 0:
                board[i][move] = turn
                self.setBoard(board)
                break
            else:
                continue