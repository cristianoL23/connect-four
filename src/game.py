from board import Board


class Game:

    def __init__(self):
        self.turn = 1
        self.board_class = Board()

    def runGame(self):
        self.printTurn()
        self.board_class.printBoard()

        win = self.handleMove()
        while(win != 4):
            self.alternateTurn()
            self.printTurn()
            self.board_class.printBoard()
            win = self.handleMove()
        print("Player " + str(self.turn) + " has won the game")

    def handleMove(self):
        move = input("Enter your move based on columns (0-6): ")
        currentRow = self.board_class.placeMove(int(move), self.turn)
        win = self.checkForWin(int(move), currentRow)
        return win

    def printTurn(self):
        print("Player " + str(self.turn) + "\'s turn")

    def alternateTurn(self):
        if(self.turn == 1):
            self.turn = 2
        else:
            self.turn = 1

    # TODO: finsih win checking algorithm
    def checkForWin(self, moveCol, currentRow):
        #     #4 of the same number in a line vertical, horizontal, or
        #     #to check above board[col][i + 1]
        #     #to check below board[col][i - 1]
        #     #to check left board[col -1][i]
        #     #to check right board[col + 1][i]
        #     #Diagonals
        #     #to check up-left board[col -1][i + 1]
        #     #to check up-right board[col +1][i+ ]
        #     #to check down-left board[col -1][i- 1]
        #     #o check down-right board[col +1][i- 1]
        board = self.board_class.getBoard()
        win = 0

        # check win vertically
        for row in range(self.board_class.getRows()):
            if board[row][moveCol] == self.turn:
                win += 1
                if win == 4:
                    return win
            else:
                win = 0

        # check win horizontally
        for col in range(self.board_class.getCols()):
            if board[currentRow][col] == self.turn:
                win += 1
                if win == 4:
                    return win
            else:
                win = 0

        # for c in range(COLUMN_COUNT-3):
		# for r in range(ROW_COUNT-3):
		# 	if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
		# 		return True

        # check win positive diagonal
        for c in range(moveCol, self.board_class.getCols(), 1):
            for r in range(currentRow, -1, -1):
                if r - 3 <= self.board_class.getRows() and c + 3 <= self.board_class.getCols():
                    if board[r][c] == self.turn and board[r-1][c+1] == self.turn and board[r-2][c+2] == self.turn and board[r-3][c+3] == self.turn:
                        print("there is a diagonal")
                        win = 4
                    else: 
                        win = 0
                # if board[r][c] == self.turn:
                #     win += 1
                #     print(win)
                # else:
                #     win = 0 
                #     print(win)
                
        # if board[currentRow][moveCol] == self.turn and board[currentRow + 1][moveCol + 1] == self.turn and board[currentRow + 2][moveCol + 2] == self.turn and board[currentRow + 3][moveCol + 3] == self.turn:
        #     win = 4

        # for row in range(self.board_class.getRows()):
        #     for cols in range(self.board_class.getCols):
        #         if board[moveCol][row] == self.turn:
        #             win += 1
        #         else:
        #             win = 0

        return win
