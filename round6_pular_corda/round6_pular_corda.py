# round6_glass_bridge_game.py
import pygame
import sys
import random

# Inicializa pygame
pygame.init()

# Tela
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Round 6 - Ponte de Vidro")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (180, 180, 180)
BLUE = (0, 0, 255)

# Fonte
font = pygame.font.SysFont("arial", 32)

# Ponte
TILE_WIDTH = 100
TILE_HEIGHT = 20
TILE_GAP = 20
TILE_ROWS = 10
bridge = [random.choice([0, 1]) for _ in range(TILE_ROWS)]  # 0 = esquerda segura, 1 = direita segura

# Jogador
player_pos = [WIDTH // 2 - TILE_WIDTH, HEIGHT - 60]
current_step = 0
alive = True
win = False

# Clock
FPS = 60
clock = pygame.time.Clock()

def draw_window():
    WIN.fill(WHITE)

    # Desenha ponte
    for i in range(TILE_ROWS):
        y = HEIGHT - (i + 1) * (TILE_HEIGHT + TILE_GAP)
        left_rect = pygame.Rect(WIDTH//2 - TILE_WIDTH - 10, y, TILE_WIDTH, TILE_HEIGHT)
        right_rect = pygame.Rect(WIDTH//2 + 10, y, TILE_WIDTH, TILE_HEIGHT)
        pygame.draw.rect(WIN, GRAY, left_rect)
        pygame.draw.rect(WIN, GRAY, right_rect)

    # Desenha jogador
    pygame.draw.circle(WIN, BLUE, (player_pos[0] + TILE_WIDTH // 2, player_pos[1]), 20)

    # Status
    if not alive:
        msg = font.render("Você caiu! Game Over", True, RED)
        WIN.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 20))
    elif win:
        msg = font.render("Você venceu!", True, GREEN)
        WIN.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 20))

    pygame.display.update()

# Loop principal
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and alive and not win:
            if event.key == pygame.K_LEFT:
                # Escolheu esquerda (0)
                if bridge[current_step] == 0:
                    current_step += 1
                    player_pos[0] = WIDTH // 2 - TILE_WIDTH - 10
                    player_pos[1] -= TILE_HEIGHT + TILE_GAP
                else:
                    alive = False
            elif event.key == pygame.K_RIGHT:
                # Escolheu direita (1)
                if bridge[current_step] == 1:
                    current_step += 1
                    player_pos[0] = WIDTH // 2 + 10
                    player_pos[1] -= TILE_HEIGHT + TILE_GAP
                else:
                    alive = False

            if current_step == TILE_ROWS:
                win = True

    draw_window()

pygame.quit()
