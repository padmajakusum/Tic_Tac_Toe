class Player:
    """
    Information about a Player

    Attributes:

    playerOne
        a string
    playerTwo
        a string
    """
    def __init__(self, playerOne, playerTwo):
        """
        Initialize self.

        Player, str, str -> None
        """
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        
    def getPlayerOne(self):
        """
        Returns the name of player one

        Player -> str
        """
        return self.playerOne
    def getPlayerTwo(self):
        """
        Returns the name of player two

        Player -> str
        """
        return self.playerTwo
         
    def __repr__(self):
        """
        Returns a representation of the Player object.
        
        Player -> str
        """
        return "Player(" + str(self.playerOne) + ", " + str(self.playerTwo) + ")"

    def __str__(self):
        """
        Returns the representation of the Player object in a string format for the user

        Player -> str

        """
        return "The players for this round of Tic Tac Toe game are " + str(self.playerOne) + " and " + str(self.playerTwo) + "."
 
        
class Board:
    """
    Information about a Tic Tac Toe Board

    Attributes:

    row
        a num
    column
        a num
    tic_tac_toe
        a list
    """

    def __init__(self, row, column, tic_tac_toe = None):
        """
        Initialize self.

        Board, num, num, list -> None
        """
        self.row = row
        self.column = column
        if tic_tac_toe == None:
            tic_tac_toe = [[] for i in range(self.row)]
        self.tic_tac_toe = tic_tac_toe
        for i in range(self.row):
            for j in range(self.column):
                self.tic_tac_toe[i].insert(self.row, '-')
                
        
    def display_board(self):
        """
        Displays the Tic Tac Toe board of size (row, column)

        Board -> None
        """
        display_row = self.row
        display_col = self.column

        for display_row in self.tic_tac_toe:
            for display_col in display_row:
                print(display_col, end=' | ')
            print()
            
    def get_row(self):
        """
        Returns the row size of the board

        Board -> num
        """
        return self.row

    def get_column(self):
        """
        Returns the column size of the board

        Board -> num
        """
        return self.column
        

    def __gt__(self, other):
        """
        Returns True if self represents a board larger than the other

        Board, Board -> Boolean
        """
        if self.get_row() > other.get_row() and self.get_column() > other.get_column():
            return True
        else:
            return False
        
    def __lt__(self, other):
        """
        Returns True if self represents a board smaller than the other

        Board, Board -> Boolean   
        """
        if self.get_row() < other.get_row() and self.get_column() < other.get_column():
            return True
        else:
            return False
        
    def __eq__(self, other):
        """
        Returns True if self represents a board equal in size with the other

        Board, Board -> Boolean
        """
        if self.get_row() == other.get_row() and self.get_column() == other.get_column():
            return True
        else:
            return False
    
    def __repr__(self):
        """
        Returns a representation of the Board object.
        
        Board -> str
        """
        return "Board(" + str(self.row) + ", " + str(self.column) + " ," + str(self.tic_tac_toe) + ")"

    def __str__(self):
        """
        Returns the representation of the Board object in a string format for the user

        Board -> str
        """
        return "A Tic Tac Toe board with dimension " + "(" + str(self.row) + ", " + str(self.column) + ")"
          

   
class Symbol:
    """
    Information about a Tic Tac Toe symbol

    Attributes:

    symbol_O
        a str
    symbol_X
        a str      
    """
    
    def __init__(self, symbol_O, symbol_X):
        """
        Initialize self.

        Symbol, str, str -> None
        """
        self.symbol_O = symbol_O
        self.symbol_X = symbol_X
        
    def get_symbol_O(self):
        """
        Returns the symbol

        Symbol -> str
        """
        return self.symbol_O
    
    def get_symbol_X(self):
        """
        Returns the symbol

        Symbol -> str
        """
        return self.symbol_X

    def __repr__(self):
        """
        Returns a representation of the Symbol object.
        
        Symbol -> str
        """
        return "Symbol(" + str(self.symbol_O) + ", " + str(self.symbol_X) + ")"

    def __str__(self):
        """
        Returns the representation of the Symbol object in a string format for the user

        Symbol -> str

        """
        return "Symbol 1 is " + str(self.symbol_O) + " and " + "Symbol 2 is " + str(self.symbol_X) + "."
    
        
        
    
