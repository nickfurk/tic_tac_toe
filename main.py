# GAME LOGIC.
# board
# display board
# play game
    # handle turn function
# check win
    # check rows function
    # check columns function
    # check diagonals function
# check tie function
# flip player function

#----Global Variables----

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whos turn is it?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    #display the board first
    display_board()

    # While the game is still going
    while game_still_going:

        # Handle a single turn of an player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")

# Handle single turn of a player
def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position from 1 to 9: ")

    #valid = False
    #while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1 to 9: ")

    position = int(position) - 1

    if board[position] == "-":
        valid = True
    else:
        print("That spot is already taken! Go again, choose a position from 1 to 9: ")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # accss global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else: # there was no win
        return

def check_rows():
    # Set up global variables
    global game_still_going
    # Checking if rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If there is a full row, then there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    # Set up global variables
    global game_still_going
    # Checking if columns have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If there is a full column, then there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # Set up global variables
    global game_still_going
    # Checking if columns have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If there is a full column, then there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    # add global variable
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # add global variables
    global current_player
    # if the current player was X, then change to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()