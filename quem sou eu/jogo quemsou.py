import pygame
import sys
import random

# Inicialização
pygame.init()
pygame.font.init()

# Configurações
WIDTH, HEIGHT = 800, 400
ROWS, COLS = 10, 10
CELL_SIZE = 30
MARGIN = 20
GRID_OFFSET = 50
SHIP_SIZES = [5, 4, 3, 3, 2]

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalha Naval")

FONT = pygame.font.SysFont(None, 24)

class Board:
    def __init__(self, x_offset):
        self.grid = [['~'] * COLS for _ in range(ROWS)]
        self.shots = [[''] * COLS for _ in range(ROWS)]
        self.x_offset = x_offset
        self.ships = []

    def draw(self, show_ships=False):
        for y in range(ROWS):
            for x in range(COLS):
                rect = pygame.Rect(self.x_offset + x * CELL_SIZE, GRID_OFFSET + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)

                if self.shots[y][x] == 'hit':
                    pygame.draw.rect(screen, RED, rect)
                elif self.shots[y][x] == 'miss':
                    pygame.draw.rect(screen, WHITE, rect)

                if show_ships and self.grid[y][x] == 'S':
                    pygame.draw.rect(screen, GREEN, rect)

    def place_ships_randomly(self):
        for size in SHIP_SIZES:
            placed = False
            while not placed:
                x = random.randint(0, COLS - 1)
                y = random.randint(0, ROWS - 1)
                direction = random.choice(['H', 'V'])

                if self.valid_ship_position(x, y, size, direction):
                    self.add_ship(x, y, size, direction)
                    placed = True

    def valid_ship_position(self, x, y, size, direction):
        if direction == 'H' and x + size > COLS:
            return False
        if direction == 'V' and y + size > ROWS:
            return False

        for i in range(size):
            xi = x + i if direction == 'H' else x
            yi = y if direction == 'H' else y + i
            if self.grid[yi][xi] == 'S':
                return False
        return True

    def add_ship(self, x, y, size, direction):
        ship_coords = []
        for i in range(size):
            xi = x + i if direction == 'H' else x
            yi = y if direction == 'H' else y + i
            self.grid[yi][xi] = 'S'
            ship_coords.append((xi, yi))
        self.ships.append(ship_coords)

    def receive_shot(self, x, y):
        if self.shots[y][x] != '':
            return 'repeat'
        if self.grid[y][x] == 'S':
            self.shots[y][x] = 'hit'
            return 'hit'
        else:
            self.shots[y][x] = 'miss'
            return 'miss'

    def all_ships_sunk(self):
        for ship in self.ships:
            if any(self.shots[y][x] != 'hit' for x, y in ship):
                return False
        return True

# Instanciar tabuleiros
player_board = Board(MARGIN)
enemy_board = Board(WIDTH // 2 + MARGIN)

player_board.place_ships_randomly()
enemy_board.place_ships_randomly()

player_turn = True
game_over = False
winner = ""

def draw_text(text, x, y, color=BLACK):
    img = FONT.render(text, True, color)
    screen.blit(img, (x, y))

# Loop principal
while True:
    screen.fill((180, 220, 255))

    player_board.draw(show_ships=True)
    enemy_board.draw(show_ships=False)

    draw_text("Jogador", MARGIN + 100, 10)
    draw_text("Inimigo", WIDTH // 2 + MARGIN + 100, 10)

    if game_over:
        draw_text(f"{winner} venceu!", WIDTH // 2 - 50, HEIGHT - 30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player_turn:
            mx, my = pygame.mouse.get_pos()
            grid_x = (mx - enemy_board.x_offset) // CELL_SIZE
            grid_y = (my - GRID_OFFSET) // CELL_SIZE

            if 0 <= grid_x < COLS and 0 <= grid_y < ROWS:
                result = enemy_board.receive_shot(grid_x, grid_y)
                if result != 'repeat':
                    if enemy_board.all_ships_sunk():
                        game_over = True
                        winner = "Jogador"
                    player_turn = False

    # Turno do computador
    if not player_turn and not game_over:
        pygame.time.delay(500)
        while True:
            x, y = random.randint(0, COLS-1), random.randint(0, ROWS-1)
            result = player_board.receive_shot(x, y)
            if result != 'repeat':
                if player_board.all_ships_sunk():
                    game_over = True
                    winner = "Inimigo"
                break
        player_turn = True

    pygame.display.flip()
