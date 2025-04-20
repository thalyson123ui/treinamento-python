import pygame
import sys

# Inicialização
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WALL-E e EVE andando")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Cores
BACKGROUND = (240, 240, 240)

# Carregar imagens
walle_img = pygame.image.load("WALL‽E.webp").convert_alpha()
eve_img = pygame.image.load("Eve_walle_render.webp").convert_alpha()

# Redimensionar imagens
walle_img = pygame.transform.scale(walle_img, (100, 100))
eve_img = pygame.transform.scale(eve_img, (80, 120))

# Posições iniciais
walle_x, walle_y = -100, HEIGHT - 150
eve_x, eve_y = -80, HEIGHT - 250

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar posições
    walle_x += 2
    eve_x += 4
    eve_y += 0.5 * pygame.math.sin(pygame.time.get_ticks() * 0.005)  # Flutuação leve

    # Resetar posições se saírem da tela
    if walle_x > WIDTH:
        walle_x = -100
    if eve_x > WIDTH:
        eve_x = -80

    # Desenhar
    screen.fill(BACKGROUND)
    screen.blit(walle_img, (walle_x, walle_y))
    screen.blit(eve_img, (eve_x, eve_y))

    pygame.display.flip()
    clock.tick(FPS)
