import pygame
import random

# Inicializa o Pygame
pygame.init()

# Constantes
LARGURA, ALTURA = 600, 600
TAMANHO_BLOCO = 30
FPS = 10

# Cores
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)

# Cria tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")

# Labirinto simples (1 = parede, 0 = espaço livre)
labirinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

linhas = len(labirinto)
colunas = len(labirinto[0])

# Pac-Man e Fantasma
pacman_pos = [1, 1]
fantasma_pos = [5, 18]

# Funções de utilidade
def desenhar_labirinto():
    for y in range(linhas):
        for x in range(colunas):
            if labirinto[y][x] == 1:
                pygame.draw.rect(tela, AZUL, (x*TAMANHO_BLOCO, y*TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

def mover_fantasma():
    direcoes = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(direcoes)
    for dx, dy in direcoes:
        novo_x = fantasma_pos[1] + dx
        novo_y = fantasma_pos[0] + dy
        if 0 <= novo_y < linhas and 0 <= novo_x < colunas and labirinto[novo_y][novo_x] == 0:
            fantasma_pos[0], fantasma_pos[1] = novo_y, novo_x
            break

# Loop principal
relogio = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentos do Pac-Man
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    if teclas[pygame.K_LEFT]: dx = -1
    if teclas[pygame.K_RIGHT]: dx = 1
    if teclas[pygame.K_UP]: dy = -1
    if teclas[pygame.K_DOWN]: dy = 1

    novo_x = pacman_pos[1] + dx
    novo_y = pacman_pos[0] + dy
    if 0 <= novo_y < linhas and 0 <= novo_x < colunas and labirinto[novo_y][novo_x] == 0:
        pacman_pos = [novo_y, novo_x]

    mover_fantasma()

    # Checa colisão
    if pacman_pos == fantasma_pos:
        print("Você perdeu!")
        rodando = False

    tela.fill(PRETO)
    desenhar_labirinto()
    pygame.draw.circle(tela, AMARELO, (pacman_pos[1]*TAMANHO_BLOCO+TAMANHO_BLOCO//2, pacman_pos[0]*TAMANHO_BLOCO+TAMANHO_BLOCO//2), TAMANHO_BLOCO//2)
    pygame.draw.circle(tela, VERMELHO, (fantasma_pos[1]*TAMANHO_BLOCO+TAMANHO_BLOCO//2, fantasma_pos[0]*TAMANHO_BLOCO+TAMANHO_BLOCO//2), TAMANHO_BLOCO//2)
    
    pygame.display.flip()
    relogio.tick(FPS)

pygame.quit()
