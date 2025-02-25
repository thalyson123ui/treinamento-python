import math

# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Verifica se alguém venceu
def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

# Verifica se ainda há jogadas possíveis
def is_moves_left(board):
    return any(" " in row for row in board)

# Função Minimax com poda alfa-beta
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 10 - depth
    if winner == 'O':
        return depth - 10
    if not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Encontra a melhor jogada para a IA
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

# Inicializa o jogo
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Jogo da Velha - IA com Minimax")
    print_board(board)
    
    while is_moves_left(board):
        row, col = map(int, input("Digite sua jogada (linha e coluna de 0 a 2, separado por espaço): ").split())
        if board[row][col] != " ":
            print("Posição ocupada! Tente novamente.")
            continue
        
        board[row][col] = 'O'
        print_board(board)
        
        if check_winner(board):
            print("Você venceu!")
            return
        
        if not is_moves_left(board):
            print("Empate!")
            return
        
        print("Vez da IA...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)
        
        if check_winner(board):
            print("A IA venceu!")
            return
    
    print("Empate!")

# Inicia o jogo
play_game()