from player import Player, Board, Symbol 
import time

#importing helper functions
from Helpers import display_instructions, choose_symbol1, assigned_symbol2,get_dimension
from Helpers import choose_symbol2, assigned_symbol1 
from Helpers import get_row, get_column, play_game
from Helpers import check_rows, check_columns, check_diagonal1, check_diagonal2, check_tie

#unicodes for symbols representing "O"
o_one = "\u25EF"
o_two ="\u273F"
o_three = "\u2605"
o_four = "\u2764"

#unicodes for symbols representing "X"
x_one = "\u2717" 
x_two = "\u2726"
x_three = "\u0394"
x_four = "\u2724"

def main():
    """
    calls other functions defined in the program and assigns variables for the return values of those functions

    None -> None
    """
    # Welcome and display instructions 
    print("Welcome to Padmaja's tic tac toe! You'll be able to customize your board and symbols for this game.")
    display_instructions()
    print()
    print("Now onto the game....")

    # prompting players' names
    print()
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    #creating a player class
    player = Player(player1, player2)
    
    # choosing a symbol for player 1
    player_one_choice = choose_symbol1(player)
    
    # choosing a symbol for player 2
    player_two_choice = choose_symbol2(player)

    # creating a Symbol class object
    symbol = Symbol(assigned_symbol1(player_one_choice), assigned_symbol2(player_two_choice))

    #printing the symbols the player's chose
    print(player1, "'s symbol", symbol.symbol_O)
    print(player2, "'s symbol", symbol.symbol_X)

    # prompts the user for dimension and gets the row and column numbers
    board_dimension = get_dimension()
    row = get_row(board_dimension)
    column = get_column(board_dimension)

    # create a board
    board = Board(row, column)   
       
    # display the board
    board.display_board()

    # calculate time taken for the game  
    start_time = time.time()
    play_game(board, symbol, player, row, column)
    end_time = time.time()
    time_taken = end_time - start_time

    # texts to display in the result 
    line1 = "Here are the results for this round of tic-tac-toe!" 
    line2 = "Time taken to finish this round: "+ str(time_taken) + " seconds"
    line3 = "Players involved in this round: " + str(player.getPlayerOne())+ " and " + str(player.getPlayerTwo())
    line4 = "Symbols chosen for this round: " + str(symbol.get_symbol_O()) + " and " + str(symbol.get_symbol_X())
    line5 = "Board size used for this round: " + str(board.get_row()) + "x" + str(board.get_column())
    lst_of_lines = [line1, line2, line3, line4, line5]

    # compare board size to the conventional 3x3
    if board > Board(3, 3):
        msg = "Yay! You chose a board size larger than the conventional 3x3 board!"
    if board < Board(3, 3):
        msg = "You chose a board size smaller than the conventional 3x3 board, you weren't allowed to do that!"
    if board == Board(3, 3):
        msg = "You chose a conventional 3x3 sized board!"
        
    
    # display results
    view_results = input("Enter 'show' to view your results!: ")  
    while view_results.lower() != "show":
        print("Enter the valid keyword!")
        view_results = input("Enter 'show' to view your results!: ")
    print() 
    print("This is what the board looked like at the end of this round:")
    print()
    board.display_board()
    print()
    print(msg)
    print()

    for item in lst_of_lines:
        print(item)

    #append msg to the list of lines
    lst_of_lines.append(msg)
        
    # append results to a file      
    try:
        with open("performance.txt", "a") as file2:
            file2.write("\n\n")
            for item in lst_of_lines:
                file2.write(item)
                file2.write("\n")
                
    except OSError:
        print("There was an error trying to access that file.")
        
# call the main function
main()
        
