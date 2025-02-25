def print_solution(board):
    """função para imprimir o tabuleiro com as rainhas"""
    for row in board:
        print(" ".join("q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    """verifica se é seguro colocar uma rainha na posição (row, col)"""
    # verificar a coluna acima
    for i in range(row):
        if board[i][col]:
            return False
        
    # verificar diagonal principal(acima)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
        
    # verificar diagonal secundária(acima)
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
        
    return True

def solve_n_queens(board, row, n, solution):
    """resolve o problema das n rainhas"""
    if row == n:
        solution.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solution)
            board[row][col] = 0

def eight_queens(n):
    """função para resolver o problema das n rainhas"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solution = []
    solve_n_queens(board, 0, n, solution)
    
    print(f"Total de soluções: {len(solution)}")
    for i, sol in enumerate(solution):
        print(f"Solução {i + 1}:")
        print_solution(sol)

        eight_queens()