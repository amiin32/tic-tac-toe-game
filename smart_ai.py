

import random
# printing game board

board = ["_"] *9
currentPlayer = "X"
winner = None
gameRunning = True

# take player input
def printBoard(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    while True:
        inp = input("Enter a number 1-9: ")
        
        if inp.isdigit():  # check if input is all digits
            inp = int(inp)
            if 1 <= inp <= 9:
                if board[inp-1] == "_":
                    board[inp-1] = currentPlayer
                    break  # valid input, exit loop
                else:
                    print("Oops! That spot is already taken. Try again.")
            else:
                print("Number must be between 1 and 9. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")
  

# check for win or tie

def checkHorizantle(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != "_":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] !="_":
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != "_":
    winner = board[6]
    return True
  

def checkRow(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "_":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "_":
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "_":
    winner = board[2]
    return True


def checkDiag(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] !="_":
    winner = board[0]
    return True
  elif board[2] == board[4] == board [6] and board[2] !="_":
    winner = board[2]
    return True

def checkTie(board):
  global gameRunning
  if "_" not in board:
    print("It is a tie!")
    printBoard(board)
    gameRunning = False

def checkWin():
  global gameRunning
  if checkDiag(board) or checkHorizantle(board) or checkRow(board):
    printBoard(board)
    gameRunning = False
    print(f"The Winner is {winner}")

# switch the player

def switchPlayer():
  global currentPlayer

  if currentPlayer == "X":
    currentPlayer = "O"
  else:
    currentPlayer = "X"


# check for win or tie again

# computer 
def computer(board):
    global currentPlayer
    if not gameRunning or currentPlayer != "O":
        return

    # 1. Try to win
    for i in range(9):
        if board[i] == "_":
            board[i] = "O"
            if checkDiag(board) or checkRow(board) or checkHorizantle(board):
                return switchPlayer()
            board[i] = "_"

    # 2. Try to block player's win
    for i in range(9):
        if board[i] == "_":
            board[i] = "X"
            if checkDiag(board) or checkRow(board) or checkHorizantle(board):
                board[i] = "O"
                return switchPlayer()
            board[i] = "_"

    # 3. Take center if available
    if board[4] == "_":
        board[4] = "O"
        return switchPlayer()

    # 4. Take corners if available
    for i in [0, 2, 6, 8]:
        if board[i] == "_":
            board[i] = "O"
            return switchPlayer()

    # 5. Take sides
    for i in [1, 3, 5, 7]:
        if board[i] == "_":
            board[i] = "O"
            return switchPlayer()


#start game

def start_game():
    global board, currentPlayer, winner, gameRunning

    board = ["_"] * 9
    currentPlayer = "X"
    winner = None
    gameRunning = True

    while gameRunning:
        printBoard(board)

        if currentPlayer == "X":
            playerInput(board)
            switchPlayer()
        else:
            print("Computer's Turn")
            computer(board)

        checkWin()
        checkTie(board)


    
if __name__ == "__main__":
    start_game()
