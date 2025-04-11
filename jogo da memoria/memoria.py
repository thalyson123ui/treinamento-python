import pygame
import random
import time

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 4, 4
CARD_WIDTH = WIDTH // COLS
CARD_HEIGHT = HEIGHT // ROWS

# Cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
HIDDEN_COLOR = GRAY

# Lista de cores para os pares
COLOR_LIST = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (255, 165, 0), (128, 0, 128)
]

# Criar pares e embaralhar
colors = COLOR_LIST * 2
random.shuffle(colors)

# Criar janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Memória")

clock = pygame.time.Clock()

# Criar cartas
cards = [{
    'color': colors[i],
    'rect': pygame.Rect((i % COLS) * CARD_WIDTH, (i // COLS) * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT),
    'revealed': False,
    'matched': False
} for i in range(ROWS * COLS)]

selected = []
running = True
waiting = False
wait_start_time = 0

# Desenhar cartas
def draw_cards():
    screen.fill(WHITE)
    for card in cards:
        color = card['color'] if card['revealed'] or card['matched'] else HIDDEN_COLOR
        pygame.draw.rect(screen, color, card['rect'])
        pygame.draw.rect(screen, BLACK, card['rect'], 2)
    pygame.display.flip()

# Loop do jogo
while running:
    draw_cards()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not waiting and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for card in cards:
                if card['rect'].collidepoint(pos) and not card['revealed'] and not card['matched']:
                    card['revealed'] = True
                    selected.append(card)
                    if len(selected) == 2:
                        waiting = True
                        wait_start_time = time.time()

    if waiting and time.time() - wait_start_time >= 1:
        if selected[0]['color'] == selected[1]['color']:
            selected[0]['matched'] = True
            selected[1]['matched'] = True
        else:
            selected[0]['revealed'] = False
            selected[1]['revealed'] = False
        selected = []
        waiting = False

    clock.tick(30)

pygame.quit()
