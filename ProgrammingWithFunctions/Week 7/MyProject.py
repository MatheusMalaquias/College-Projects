def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, choose a line (0-2): "))
            col = int(input(f"Player {current_player}, choose a colun (0-2): "))

            if board[row][col] != " ":
                print("This position is already occupied! Please try again.")
                continue
            
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} won!")
                break
            
            if is_board_full(board):
                print_board(board)
                print("Draw!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid entry. Please try again.")

if __name__ == "__main__":
    main()