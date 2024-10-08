def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  
        return 1
    elif winner == "X": 
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:  
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else: 
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
    
def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    return best_move

def play_tic_tac_toe():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move! Try again.")
            continue
        
        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        print("AI is making a move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
        
        if check_winner(board) == "O":
            print_board(board)
            print("AI wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
play_tic_tac_toe()