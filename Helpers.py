from player import Player, Board, Symbol

x_one = "\u2717" 
x_two = "\u2726"
x_three = "\u0394"
x_four = "\u2724"

o_one = "\u25EF"
o_two ="\u273F"
o_three = "\u2605"
o_four = "\u2764"

def display_instructions():
    """
    displays the instructions for playing tic tac toe

    None -> None
    """
    print()
    ans_for_hints = input("Are you familiar with this game?(y / n): ")
    print()
    while ans_for_hints.lower() not in ("y", "yes", "no", "n"):
        print("Enter a valid answer")
        print()
        ans_for_hints = input("Are you familiar with this game?(y / n): ")
    if ans_for_hints.lower() == "n" or ans_for_hints.lower() == "no":
        try:
            with open("rules.txt", "r") as file:
                contents = file.read()
                print(contents)
        except OSError:
            print("There was an error trying to access that file.")
            
def choose_symbol1(player):
    """
    prompts the user for the number of the choice of the player's symbol for the game and returns the choice

    Player(class) -> num
    """
    print()
    print("1." + o_one)
    print("2." + o_two)
    print("3." + o_three)
    print("4." + o_four)
    choice = int(input("Enter the symbol choice for " + player.getPlayerOne() + ": "))
    print()
    while choice not in (1, 2, 3, 4):
        print("Enter a valid choice!")
        choice = int(input("Enter the symbol choice for " + player.getPlayerOne() + ": "))
        print()
    return choice

def choose_symbol2(player):
    """
    prompts the user for the number of the choice of the player's symbol for the game and returns the choice

    Player(class) -> num    
    """
    print("1." + x_one)
    print("2." + x_two)
    print("3." + x_three)
    print("4." + x_four)
    choice = int(input("Enter the symbol choice for "+ player.getPlayerTwo() + ": "))
    print()
    while choice not in (1, 2, 3, 4):
        print("Enter a valid choice!")
        choice = int(input("Enter the symbol choice for "+ player.getPlayerTwo() + ": "))
        print()
    return choice

def assigned_symbol1(choice):
    """
    returns the symbol chosen by the player as per their number choice

    num -> str
    """
    if choice == 1:
        O = o_one
    elif choice == 2:
        O = o_two
    elif choice == 3:
        O = o_three
    else:
        O = o_four
    return O

def assigned_symbol2(choice):
    """
    returns the symbol chosen by the player as per their number choice

    num -> str
    """
    if choice == 1:
        X = x_one
    elif choice == 2:
        X = x_two
    elif choice == 3:
        X = x_three
    else:
        X = x_four
    return X

def get_dimension():
    """
    prompts user for the dimension of the tic tac toe board for the game (row, column) and returns it

    None -> tuple
    """
    print()
    dimension = input("Enter a dimension for the tic tac toe board(row, column): ")
    token = dimension.split(",")

    while int(token[0]) < 3 or int(token[1]) < 3:
            print()
            print("The minimum grid size should be (3, 3)")
            dimension = input("Enter a dimension for the tic tac toe board(row, column): ")
            token = dimension.split(",")
            
    while int(token[0]) != int(token[1]):
        print()
        print("Make sure the row is equal to column so that a square grid can be formed")
        dimension = input("Enter a dimension for the tic tac toe board(row, column): ")
        token = dimension.split(",")
        while int(token[0]) < 3 or int(token[1]) < 3:
            print()
            print("The minimum grid size should be (3, 3)")
            dimension = input("Enter a dimension for the tic tac toe board(row, column): ")
            token = dimension.split(",")
    return token

def get_row(dimension):
    """
    returns the row from the dimension entered by the user

    str -> num
    """   
    return int(dimension[0])

def get_column(dimension):
    """
    returns the column from the dimension entered by the user

    str -> num
    """
    return int(dimension[1])
    
def play_game(board, symbol, player, row, column):
    """
    prompts player 1 and player 2 for a position in the board to append their symbols into, and appends the symbols into the board

    Board(class), str, Player(class), num, num -> None
    """
    while True:
        print()
        position1 = input("Enter a position for " + player.getPlayerOne() + "(row, column): ")
        token = position1.split(",")
        
        while int(token[0]) > row or int(token[1]) > column:
            print()
            print("Your position exceeds the dimension of the board!")
            position1 = input("Enter a position for " + player.getPlayerOne() + "(row, column): ")
            token = position1.split(",")
            
        while board.tic_tac_toe[int(token[0]) -1][int(token[1]) - 1] != "-":
            print()
            print("Oops! That position is already taken. Please try another position.")
            position1 = input("Enter a position for " + player.getPlayerOne() + "(row, column): ")
            token = position1.split(",")
            while int(token[0]) > row or int(token[1]) > column:
                print()
                print("Your position exceeds the dimension of the board!")
                position1 = input("Enter a position for " + player.getPlayerOne() + "(row, column): ")
                token = position1.split(",")
                
        # append
        board.tic_tac_toe[int(token[0]) -1][int(token[1]) - 1] = symbol.symbol_O
        
       # display board
        board.display_board()

        # check rows, columns, diagonals and Tie
        if check_rows(board) or check_columns(board) or check_diagonal1(board) or check_diagonal2(board):
            print()
            print("Tic Tac Toe!")
            break
        if check_tie(board):
            print()
            print("Tie!")
            break
        
        position2 = input("Enter a position for " + player.getPlayerTwo() + "(row, column): ")
        token1 = position2.split(",")
        while int(token1[0]) > row or int(token1[1]) > column:
            print()
            print("Your position exceeds the dimension of the board!")
            position2 = input("Enter a position for " + player.getPlayerTwo() + "(row, column): ")
            token1 = position2.split(",")
            
        while board.tic_tac_toe[int(token1[0]) -1][int(token1[1]) - 1] != "-":
            print()
            print("Oops! That position is already taken. Please try another position")
            position2 = input("Enter a position for " + player.getPlayerTwo() + "(row, column): ")
            token1 = position2.split(",")
            while int(token1[0]) > row or int(token1[1]) > column:
                print()
                print("Your position exceeds the dimension of the board!")
                position2 = input("Enter a position for " + player.getPlayerTwo() + "(row, column): ")
                token1 = position2.split(",")
                
        #append
        board.tic_tac_toe[int(token1[0]) -1][int(token1[1]) - 1] = symbol.symbol_X
        
        #display board
        board.display_board()
        # check rows, columns, diagonals and Tie
        if check_rows(board) or check_columns(board) or check_diagonal1(board) or check_diagonal2(board):
            print()
            print("Tic Tac Toe!")
            break
        if check_tie(board):
            print()
            print("Tie!")
            break


def check_rows(board):
    """
    Returns a boolean value for whether a row consists of the same symbols along the line

    Board(class) -> Boolean
    """
    num = 0
    count = 0
    val = False
    for i in range(len(board.tic_tac_toe)):
        for j in range(len(board.tic_tac_toe)):
            if board.tic_tac_toe[num][0] == board.tic_tac_toe[i][j] != "-":
                count += 1 
        if count == len(board.tic_tac_toe[0]):
            val = True
        count = 0
        num += 1
    return val

def check_columns(board):
    """
    Returns a boolean value for whether a column consists of the same symbols along the line

    Board(class) -> Boolean
    """
    count = 0
    num1 = 0
    val = False
    for i in range(len(board.tic_tac_toe)):
        for j in range(len(board.tic_tac_toe)):
            if board.tic_tac_toe[0][num1] == board.tic_tac_toe[j][i] != "-":
                count += 1
        if count == len(board.tic_tac_toe[0]):
            val = True
        count = 0
        num1 += 1
    return val
            
def check_diagonal1(board):
    """
    Returns a boolean value for whether a left to right diagonal consists of the same symbols along the line

    Board(class) -> Boolean
    """
    count = 0
    num = 0
    val = False
    for i in range(len(board.tic_tac_toe)):
        if board.tic_tac_toe[0][0] == board.tic_tac_toe[i][num] != "-":
            count += 1
        num += 1
        if count == len(board.tic_tac_toe):
            val = True
    return val
    
def check_diagonal2(board):
    """
    Returns a boolean value for whether a right to left diagonal consists of the same symbols along the line

    Board(class) -> Boolean
    """
    count = 0
    num1 = -1
    val = False
    for j in range(len(board.tic_tac_toe)):
        if board.tic_tac_toe[0][-1] == board.tic_tac_toe[j][num1] != "-":
            count += 1
        num1 -= 1
    if count == len(board.tic_tac_toe[0]):
        val = True
    return val

def check_tie(board):
    """
    Returns a boolean value for whether all the spaces in the grid are occupied with symbols or not

    Board(class) -> Boolean
    """
    count = 0
    val = False
    for lst in board.tic_tac_toe:
        if "-" not in lst:
            count += 1
    if count == len(board.tic_tac_toe):
        val = True
    return val

