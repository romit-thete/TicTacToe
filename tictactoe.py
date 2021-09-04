"""
TIC TAC TOE: The Game
This code is an attempt to the world famous: Tic Tac Toe.
The computer plays as 'X' and the user plays 'O'.
The computer plays it's first move and drops an 'X' at the center.

Functions:
1. display_board(board):    Displays the Tic tac toe board in a specific format.
2. enter_move(board):    Accepts the board's current status, asks the user for their move, checks the input
                         and updates the board accordingly.
3. make_list_of_free_fields(board):    Browses the board and builds a list of all the free squares;
                                       the list consists of tuples, while each tuple is a pair of row and column numbers
4. victory_for(board):    The function analyzes the board status in order to check if the player
                          using 'O's or 'X's has won the game
5. draw_move(board):    The function draws the computer's move and updates the board
"""
from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print()
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for col in row:
            print("|   " + str(col) + "   ", end='')
        print("|\n" + "|       " * 3 + "|", end='')
    print("\n" + "+-------" * 3 + "+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    try:
        get_inp = int(input("Enter your move: "))
        if 0 < get_inp < 10:
            for row in board:
                for col in row:
                    if col == get_inp:
                        row1, col1 = board.index(row), row.index(col)
                        if (row1, col1) in make_list_of_free_fields(board):
                            board[row1][col1] = user
                            return board
                    else:
                        continue
            # Validation check for cases when board is already occupied with user's move
            return "Already occupied"
        else:
            # Validation fails if the user's input is beyond the limits
            return "Failed"
    except ValueError:
        # Validation check for non-integers
        print("Enter a valid numeric input!!")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list = []
    for row_entry in board:
        for col_entry in row_entry:
            if col_entry != 'X' and col_entry != 'O':
                free_list.append((board.index(row_entry), row_entry.index(col_entry)))
    return free_list


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    # Horizontal check
    if (board[0][0], board[0][1], board[0][2]) == (sign, sign, sign) or (board[1][0], board[1][1], board[1][2]) == (sign, sign, sign) or (board[2][0], board[2][1], board[2][2]) == (sign, sign, sign):
        return sign

    # Vertical check
    if (board[0][0], board[1][0], board[2][0]) == (sign, sign, sign) or (board[0][1], board[1][1], board[2][1]) == (sign, sign, sign) or (board[0][2], board[1][2], board[2][2]) == (sign, sign, sign):
        return sign

    # Diagonal check
    if (board[0][0], board[1][1], board[2][2]) == (sign, sign, sign) or (board[0][2], board[1][1], board[2][0]) == (sign, sign, sign):
        return sign


def draw_move(board):
    # The function draws the computer's move and updates the board.
    global first_move
    if first_move:
        board[1][1] = comp
        first_move = False
    else:
        # Assign 'X' to a random place where 'O' is not present
        while True:
            comp_move = randrange(1, 10)
            for row in board:
                for col in row:
                    if col == comp_move:
                        row1, col1 = board.index(row), row.index(col)
                        if (row1, col1) in make_list_of_free_fields(board):
                            board[row1][col1] = comp
                            return board
                    else:
                        comp_move = randrange(1, 10)
                        continue


# Function calls made from here..
print("\n"+"******" * 10, "TICTACTOE", "******" * 10)
print("Author: Romit Thete"
      "\nLast Revised date: 04-Sep-2021")
print("******" * 22)
print("Description:"
      "\nThis is an interactive game where you play as 'O' and the computer plays as 'X'."
      "\nThe computer gets the first chance and always claims it's place in the center."
      "\nEnter the number where you need to put a 'O'.")
print("******" * 22)
print("The Game starts now:")

comp = "X"
user = "O"
first_move = True

# Setup the initial board
my_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Draw computer's first move
draw_move(my_board)
display_board(my_board)

# Until we have an empty list of free fields, ask user for a move,
# If the move is valid, check if user/computer wins and continue until the end of the game.
while make_list_of_free_fields(my_board):
    # print(make_list_of_free_fields(my_board))
    x = enter_move(my_board)
    if x is not None and x != "Failed" and x != "Already occupied":
        if victory_for(my_board, 'O') == 'O':
            print('\n\nYou Won!!\n\n')
            break
        draw_move(my_board)
        if victory_for(my_board, 'X') == 'X':
            print('\n\nComputer Won!!\n\n')
            break
        display_board(my_board)
        if not make_list_of_free_fields(my_board):
            print("\n\nIt's a tie!\n\n")
    else:
        # The below is done because None is printed if x is None
        if x is not None:
            print(x)
print("Here's the final board:")
display_board(my_board)
