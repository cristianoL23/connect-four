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

    def checkForWin(self, moveCol, currentRow):
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

        # check win positive diagonal
        win = 0
        for c in range(self.board_class.getCols()):
            for r in range(self.board_class.getRows() - 1, -1, -1):
                if r - 3 >= 0 and c + 3 < self.board_class.getCols():
                    if board[r][c] == self.turn and board[r-1][c+1] == self.turn and board[r-2][c+2] == self.turn and board[r-3][c+3] == self.turn:
                        win = 4

        #check negative diagonal
        win = 0
        for c in range(self.board_class.getCols()):
            for r in range(self.board_class.getRows()):
                if r + 3 < self.board_class.getRows() and c + 3 < self.board_class.getCols():
                    if board[r][c] == self.turn and board[r+1][c+1] == self.turn and board[r+2][c+2] == self.turn and board[r+3][c+3] == self.turn:
                        win = 4

        return win
