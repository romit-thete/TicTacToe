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
        if get_inp > 0 and get_inp < 10:
            for row in board:
                for col in row:
                    if col == get_inp:
                        row1, col1 = board.index(row), row.index(col)
                        if (row1, col1) in make_list_of_free_fields(board):
                            board[row1][col1] = user
                            return board
                    else:
                        continue
            return "Already occupied"
        else:
            return "Failed"
    except ValueError:
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
    if (board[0][0], board[1][0], board[2][0]) == (sign, sign, sign) or (board[0][1], board[1][1], board[2][1]) == (sign, sign, sign) or (board[0][2], board[1][2], board[2][2]) == (sign, sign, sign):
        return sign
    if (board[0][0], board[1][1], board[2][2]) == (sign, sign, sign) or (board[0][2], board[1][1], board[2][0]) == sign:
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


comp = "X"
user = "O"
first_move = True

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

draw_move(board)
display_board(board)
while make_list_of_free_fields(board) != []:
    # print(make_list_of_free_fields(board))
    enter_move(board)
    if victory_for(board, 'O') == 'O':
        print('You Won')
        break
    draw_move(board)
    if victory_for(board, 'X') == 'X':
        print('Computer Won')
        break
    display_board(board)
    if make_list_of_free_fields(board) == []:
        print("It's a tie")
