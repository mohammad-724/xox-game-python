import random

def print_board(board):
    """Prints the current state of the 3x3 board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if a player has won using clear mathematical index rows."""
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False
def is_board_full(board):
    """Returns True if there are no empty spaces left on the board."""
    return all(space in ['X', 'O'] for space in board)

def play_xox():
    board = [str(i) for i in range(1, 10)]
    human = 'X'
    bot = 'O'

    print("--- Welcome to XOX (Tic-Tac-Toe) ---")
    print("You are 'X' and the Bot is 'O'. Enter a number 1-9 to make a move.")
    print_board(board)
    
    while True:
        while True:
            try:
                move = int(input("Your turn (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                    board[move] = human
                    break
                else:
                    print("That spot is already taken or invalid. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
        
        print_board(board)
        
        if check_winner(board, human):
            print("🎉 Congratulations! You beat the bot!")
            break
            
        if is_board_full(board):
            print("🤝 It's a draw!")
            break
        print("Bot is thinking...")
        empty_spots = [i for i, space in enumerate(board) if space not in ['X', 'O']]
        bot_move = random.choice(empty_spots)
        board[bot_move] = bot
        
        print_board(board)
        
        if check_winner(board, bot):
            print("🤖 Game over! The bot wins!")
            break
            
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_xox()
