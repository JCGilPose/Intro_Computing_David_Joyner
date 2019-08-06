#Earlier in the course, you implemented a function that could
#find if someone had won a particular game of either tic-tac-
#toe or mancala based on a 2D list or tuple representing the
#current game board.
#
#In this problem, you'll do the same thing, but for the game
#Connect 4. Write a function called check_winner which takes
#as input a 2D list. It should return "X" if there are four
#adjacent "X" values anywhere in the list (row, column,
#diagonal); "O" if there are four adjacent "O" values
#anywhere in the list; and None if there are neither.
#
#Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
#To keep things simple, we'll still use "X" and "O" to
#represent the players, and None to represent empty spots.
#You may assume there will be only one winner per board,
#no characters besides "X", "O", and None, and you don't
#have to worry about whether the board is actually a
#valid game of Connect 4.
#
#Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.


#Write your function here!
def check_winner(table):
    #checking same 4 in line
    for line in table:
        if ("X" in line) or ("O" in line):
            line_1 = (line[0] == line[1] == line[2] == line[3] != None)
            line_2 = (line[1] == line[2] == line[3] == line[4] != None) 
            line_3 = (line[2] == line[3] == line[4] == line[5] != None) 
            line_4 = (line[3] == line[4] == line[5] == line[6] != None)
            if line_1:
                if line[0] == "X":
                    return "X"
                else:
                    return "O"
            if line_2:
                if line[1] == "X":
                    return "X"
                else:
                    return "O"
            if line_3:
                if line[2] == "X":
                    return "X"
                else:
                    return "O"
            if line_4:
                if line[3] == "X":
                    return "X"
                else:
                    return "O"

    #checking same 4 in column
    for i in range(0,7):
        column_1 = (table[0][i] == table[1][i] == table[2][i] == table[3][i] != None)  
        column_2 = (table[1][i] == table[2][i] == table[3][i] == table[4][i] != None)
        column_3 = (table[2][i] == table[3][i] == table[4][i] == table[5][i] != None)
        if column_1:
            if table[0][i] == "X":
                return "X"
            else:
                return "O"
        if column_2:
            if table[1][i] == "X":
                return "X"
            else:
                return "O"
        if column_3:
            if table[2][i] == "X":
                return "X"
            else:
                return "O"

    #checking one type of diagonal
    for i in range(0,3):
        for j in range(0,4):
            if table[i][j] == table[i+1][j+1] == table[i+2][j+2] == table[i+3][j+3] != None:
                if table[i][j] == "X":
                    return "X"
                else:
                    return "O"
        
    #checking other type of diagonal
    for i in range(0,3):
        for j in range(-1,-5, -1):
            if table[i][j] == table[i+1][j-1] == table[i+2][j-2] == table[i+3][j-3] != None:
                if table[i][j] == "X":
                    return "X"
                else:
                    return "O"
    return None
                      
#The code below tests your function on three Connect-4
#boards. Remember, the line breaks are not needed to create
#a 2D tuple; they're used here just for readability.
xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O", None),
         (None, "O" , "X" , "X" , "O" , "X", None),
         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
         
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))
