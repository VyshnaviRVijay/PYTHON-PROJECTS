
#the game board displaying function
def show_board(board):
    print(board[0], "|" , board[1], "|" , board[2])
    print("--+---+--")
    print(board[3], "|" , board[4], "|" , board[5])
    print("--+---+--")
    print(board[6], "|" , board[7], "|" , board[8])

#player win checking function
def check_win(board,symbol):
    #Checking the rows
    if board[0] == board[1] == board[2] == symbol:
        return True
    elif board[3] == board[4] == board[5] == symbol:
        return True
    elif board[6] == board[7] == board[8] == symbol:
        return True

    #checking the columns
    elif board[0] == board[3] == board[6] == symbol:
        return True
    elif board[1] == board[4] == board[7] == symbol:
        return True
    elif board[2] == board[5] == board[8] == symbol:
        return True

    #checking the diagonals
    elif board[0] == board[4] == board[8] == symbol:
        return True
    elif board[2] == board[4] == board[6] == symbol:
        return True
    
    else:
        return False

#Getting a valid move from the player
def take_move(board,player_name,symbol):

    while True:
        try:
            position = int(input("enter position (1-9): "))
    
            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
                continue

            if board[position-1] in ["X","O"]:
                print("Position already occupied. Try again!!")
                continue

            return position - 1

        except ValueError:
                    print("Invalid input. Enter a number.")

#Function to play the game
def play_game():

 # Creating game board 
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 

    # Get player names 
    player1 = input("Enter Player 1 name: ").upper().strip()
    player2 = input("Enter Player 2 name: ").upper().strip()

    if player1 == "": 
        player1 = "Player 1"

    if player2 == "": 
        player2 = "Player 2"

    # Get player symbol 
    player1_symbol = input( f"{player1}, choose a symbol X or O: " ).upper().strip() 

    # Validate Player 1 symbol and assign Player 2 symbol 
    
    if player1_symbol == "X":
         player2_symbol = "O" 
         
    elif player1_symbol == "O":
         player2_symbol = "X" 
         
    else: 
        print("Invalid symbol!! Please choose X or O")

    # Store player names and symbols in a list 
    players = [(player1, player1_symbol), 
        (player2, player2_symbol)] 



    print("\nWELCOME TO TIC-TAC-TOE!!!\n")
    print(player1, " uses ",player1_symbol)
    print(player2," uses ",player2_symbol)
   

    show_board(board)

# play_game()

#Two - Player logic
    for move in range(9):
        #player selecting
        if move % 2 == 0:
            player_name,symbol = players[0]
        else:
            player_name,symbol = players[1]

        print(player_name," 's turn")

        #getting position
        position = take_move(board,player_name,symbol)

        #placing the board symbol
        board[position] = symbol

        #updated board
        show_board(board)

        #checking current player's win
        
        if check_win(board,symbol):
            print("CONGRATULATIONS !!!" , player_name, " YOU WONN !")
            break

        #checking for a draw
        else:
            print("The game is a draw")


def main():
    while True:
        play_game()

        while True:
            answer = input("Would you like to play again?? (yes/no)").lower().strip()
            if answer == "yes":
                break
            elif answer == "no":
                print("Thank you for playing!!")
                exit()
            else:
                print("Please enter yes or no.")
main()








