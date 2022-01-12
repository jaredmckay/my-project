game_runs = True
winner = None
player = "X"
count = 0

## board list
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

## creates the game board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])


##plays the game of tic tac toe
def main():
    ## displays the game board
    display_board()

    while game_runs:

        move_choice(player)

        #checks if the last turn played has finished the game
        check_if_game_done()

        # changes the player after every turn 
        change_player()

    if winner =="X" or winner == "O":
        print(f"And the winner is {winner}")
    elif winner == None:
        print("The game was a tie")

## asks and dictates players choice
def move_choice(player):
    print(f"It is {player}'s turn")
    move = input("Choose a position from 1-9: ")
    
    
    # checks choice against board list to verify choice is valid
    # repeats input unitl a valid choice is made 
    while move not in board:
        move = input("invalid choice! Choose a position from 1-9: ")

    move = int(move) - 1
    board[move] = player
    display_board()

def check_if_game_done():

    check_winner()

    check_tie()

def check_winner():

    global winner

    ## will check rows
    row_win = check_rows()

    ## will check columns
    column_win = check_columns()

    ## will check diagonal
    diagonal_win = check_diagonal()

    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    return

def check_rows():
    global game_runs

    #checks row for three of a kind

    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    
    if row_1 or row_2 or row_3:
        game_runs = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_runs

    #checks column for three of a kind

    column_1 = board[0] == board[3] == board[6]
    column_2 = board[1] == board[4] == board[7]
    column_3 = board[2] == board[5] == board[8]
    
    # finds out what row has one and returns the symbol for the winner line
    # this will return the x or o that one and return it to show who won
    if column_1 or column_2 or column_3:
        game_runs = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_diagonal():
    global game_runs

    #checks diagonal for three of a kind

    diagonal_1 = board[0] == board[4] == board[8]
    diagonal_2 = board[2] == board[4] == board[6]
    
    if diagonal_1 or diagonal_2:
        game_runs = False
    if diagonal_1 or diagonal_2:
        return board[4]

#check for a count if the count gets to 9 then all possible turns have
# been played and game ends in a tie
def check_tie():
    global count
    global game_runs
    if count >= 8:
        game_runs = False
    return    

## changes player every turn
def change_player():
    global player
    global count
    count += 1
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return

if __name__ == "__main__":
    main()
