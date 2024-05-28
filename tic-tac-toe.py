
# Nested loop outer (1st) loop iterates rows
# inner (1st) loop iterates columns of the row



xPlayer = "x"
oPlayer = "o"
#occupiedSpaces = []

# Draw game board
def display_board():
    # should accept 1 parameter containing current status of board
    # print board status to console
    board=[[1,2,3],[4,5,6],[7,8,9]]
    
    # i is for ROW num
    for i in range(len(board)):
        print("+-------+")
        
        # j is for column num
        for j in range(len(board[i])):
            
            # print gameBoard[rowNum][columnNum]
##            print(board[i][j])
            return board    



# makeMove()
# Computer always gets first move @ center of board  with symbol 'x' (gameBoard[1][1])
def firstMove(board):
    board[1][1] = xPlayer
    board[0][1] = oPlayer
    # no need to pop value from board, we can track winner based on index positions
    return board

def checkBoardStatus(board):
    count = 0
    #rows
    for i in range(len(board)):        
        #columns
        for j in range(len(board[i])):
            if board[i][j] == 'x' or  board[i][j] == 'o':
                print("Choose another space.")
            
            # print gameBoard[rowNum][columnNum]
##            print(board[i][j])
                

def countMoves(board):
    count = 0
    #rows
    for i in range(len(board)):        
        #columns
        for j in range(len(board[i])):
            if board[i][j] == 'x' or  board[i][j] == 'o':
                count = count + 1
    print("number of moves: ", count)
            
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

# Main Function
def main():
    board = display_board()
    print("STARTING GAME: game board" , board)

    boardStatus= firstMove(board) #return game board after PC makes first moves
    print("game board after first move", boardStatus)

    checkBoardStatus(board)

    countMoves(board)

    

main()


    
                        

