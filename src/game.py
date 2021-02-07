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
        print("Player" + str(self.turn) + "had won the game")
    
    def handleMove(self):
        move = input("Enter your move based on columns: ")
        self.board_class.placeMove(int(move), self.turn)
        win = self.checkForWin(int(move))
        return win
        
    def printTurn(self):
        print("Player" + str(self.turn) + "\'s turn")
        
    def alternateTurn(self):
        if(self.turn == 1):
            self.turn = 2
        else:
            self.turn = 1

    #TODO: finsih win checking algorithm
    def checkForWin(self, col):
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

    #     #checking for win along a row
        win = 0
        # row = board[col].index(turn)
    
        # for col in range(7):
        #     if board[col][row] == turn:
        #         win += 1
        #     else:
        #         win = 0
        
        #for row in range(6):
        return win
