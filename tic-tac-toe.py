
# Nested loop outer (1st) loop iterates rows
# inner (1st) loop iterates columns of the row



xPlayer = "x"
oPlayer = "o"
#occupiedSpaces = []
gameBoard=[[1,2,3],[4,5,6],[7,8,9]]

# Draw game board

    # should accept 1 parameter containing current status of board
    # print board status to console
def display_board(board):

    # initialize second row/ center column with "X" (PCgets first of game)
    board[1][1] = xPlayer
    
    #Check board status
    #rows
    for i in range(len(board)):        
        #columns
        for j in range(len(board[i])):
            if board[i][j] == xPlayer or  board[i][j] == oPlayer:
                print("Choose an available space on the board")
    return board
        
            
            # print gameBoard[rowNum][columnNum]
##            print(board[i][j])
    
    # i is for ROW num
    #for i in range(len(board)):
    #    print("+-------+")
        
        # j is for column num
     #   for j in range(len(board[i])):
            
            # print gameBoard[rowNum][columnNum]
##            print(board[i][j])
      #      return board    



# enter_move()
# Accepts board status (x)
# requests move from user: PC ALWAYS GETS 1ST MOVE W/ X @ board[1][1] (x)
# checks validity of userinput
# update board per user input
# return updated gameBoard
def enter_move(board) ->tuple[list, int]:
    
    num_Moves = 1 # num_moves
    if num_Moves % 2 == 1: # PC plays as X
        player = oPlayer
        print("PLAYER" + player + "make your move!")
        i = int(input("row number 0-2: "))
        j = int(input("column number 0-2: "))
        board[i][j] = oPlayer

    elif num_Moves % 2 == 0: # human plays as O
        player = xPlayer
        print("PLAYER" + player + "make your move!")
        i = int(input("row number 0-2: "))
        j = int(input("column number 0-2: "))
        board[i][j] = xPlayer
    
    num_Moves = num_Moves + 1
    return board, num_Moves

""" def countMoves(board):
    count = 0
    #rows
    for i in range(len(board)):        
        #columns
        for j in range(len(board[i])):
            if board[i][j] == 'x' or  board[i][j] == 'o':
                count = count + 1
    print("number of moves: ", count) """
            
            # print gameBoard[rowNum][columnNum]
##            print(board[i][j])





##myList =["x",2,3]
####print(myList[0])
##for i in range(len(myList)):
####    print(myList[i])
##    if myList[i] == "x" or myList[i] == "o":
##        print("found " + myList[i] + " at indexPos", i)
##    else:
##        print("available spaces are" ,i)

def make_lisf_of_free_fields(board):
    None
    # analyzes board status to build list of fields available to play

# Main Function
def main():
    board = display_board(gameBoard)
    print("STARTING GAME: game board" , board)
    print("I,(the computer) have taken the firstmove. You have no say in the matter!")

    # return updated game board after PC makes first move
    boardStatus, totalMoves = enter_move(board) 
    print("game board after first move", boardStatus)
    print("total # of moves ", totalMoves)

    #countMoves(board)

main()


    
                        

