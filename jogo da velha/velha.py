import pygame
import sys

# Inicializa o pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
X_COLOR = (66, 66, 255)
O_COLOR = (255, 66, 66)

# Configurações da tela
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5

# Células
CELL_SIZE = WIDTH // 3

# Tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill(WHITE)

# Tabuleiro
board = [[None for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

def draw_grid():
    for i in range(1, 3):
        # Linhas horizontais
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        # Linhas verticais
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

def draw_x(x, y):
    margin = 30
    pygame.draw.line(screen, X_COLOR, (x + margin, y + margin), (x + CELL_SIZE - margin, y + CELL_SIZE - margin), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (x + CELL_SIZE - margin, y + margin), (x + margin, y + CELL_SIZE - margin), LINE_WIDTH)

def draw_o(x, y):
    center = (x + CELL_SIZE // 2, y + CELL_SIZE // 2)
    radius = CELL_SIZE // 2 - 30
    pygame.draw.circle(screen, O_COLOR, center, radius, LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if board[row][col] == 'X':
                draw_x(x, y)
            elif board[row][col] == 'O':
                draw_o(x, y)

def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full():
    return all(all(cell is not None for cell in row) for row in board)

def reset_game():
    global board, current_player, game_over
    board = [[None for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    screen.fill(WHITE)
    draw_grid()

# Inicia o jogo
draw_grid()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player
                if check_win(current_player):
                    game_over = True
                elif is_board_full():
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
                draw_figures()
        elif event.type == pygame.KEYDOWN and game_over:
            reset_game()
    pygame.display.update()